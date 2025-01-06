Implementation Guidelines
==============================================================================
This document outlines the core design patterns and implementation guidelines for extending and maintaining the ``pyatlassian`` library. The library follows several key design patterns to ensure consistency, maintainability, and ease of use.


1. Source Code Organization Pattern
------------------------------------------------------------------------------
The ``pyatlassian`` library is organized using a hierarchical structure that reflects Atlassian's unified API approach. Since Atlassian uses a single API endpoint for all its cloud services (Confluence, Jira, etc.), the codebase mirrors this architecture.


Python Library Folder Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: text

    pyatlassian/
    ├── atlassian/              # Base package with core functionality
    │   ├── api.py              # Base API implementation
    │   └── model.py            # Base Atlassian model
    ├── atlassian_confluence/   # Confluence-specific package
    │   ├── api.py              # Confluence API implementation
    │   ├── model.py            # Confluence model
    │   └── utils.py            # Confluence utilities
    └── atlassian_jira/         # Jira-specific package (planned)
        ├── api.py              # Jira API implementation
        ├── model.py            # Jira model
        └── utils.py            # Jira utilities
        ...


Base Atlassian Implementation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The base ``Atlassian`` class serves as the foundation for all product-specific implementations:

.. dropdown:: atlassian/model.py

    .. literalinclude:: ../../../pyatlassian/atlassian/model.py
       :language: python
       :linenos:


Product-Specific Implementation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Each Atlassian product (like Confluence) extends the base class:

.. dropdown:: atlassian_confluence/model.py

    .. literalinclude:: ../../../pyatlassian/atlassian_confluence/model.py
       :language: python
       :linenos:


Utility Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Product-specific utilities are organized in dedicated modules:

.. dropdown:: atlassian_confluence/utils.py

    .. literalinclude:: ../../../pyatlassian/atlassian_confluence/utils.py
       :language: python
       :linenos:


I'll help expand the API Group Modularization Pattern section to clearly explain these relationships. Here's a comprehensive write-up:


2. API Group Modularization Pattern
------------------------------------------------------------------------------
The library uses a mixin-based modularization pattern to organize API endpoints into logical groups that mirror Atlassian's official API documentation structure.


API Group to Module Mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Each API group in Atlassian's REST API (e.g., pages, spaces, comments) corresponds to a dedicated Python module containing a mixin class:

.. code-block:: text

    Atlassian API Structure          Python Implementation
    ────────────────────────         ───────────────────────
    └── Confluence                   └── pyatlassian/atlassian_confluence/
        ├── Pages API Group              ├── page.py (PageMixin)
        └── Spaces API Group             └── space.py (SpaceMixin)


Mixin Implementation Pattern
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Each API group module implements a mixin class that encapsulates all endpoints within that group:

.. dropdown:: atlassian_confluence/page.py

    .. literalinclude:: ../../../pyatlassian/atlassian_confluence/page.py
       :language: python
       :linenos:


API Method to Python Method Mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Each REST API endpoint maps to a method within its corresponding mixin class:

.. code-block:: text

    REST API Endpoint                     Python Method
    ──────────────────                    ─────────────
    GET /spaces/{id}/pages          →     get_pages_in_space()
    GET /pages/{id}                 →     get_page_by_id()
    POST /pages                     →     create_page()


The Complete Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The main model class (e.g., Confluence) inherits from all relevant mixins to provide a unified API:

.. dropdown:: atlassian_confluence/model.py

    .. literalinclude:: ../../../pyatlassian/atlassian_confluence/model.py
       :language: python
       :linenos:

This pattern offers several benefits:

1. **Modularity**: Each API group is self-contained and independently maintainable
2. **Organization**: Clear mapping between Atlassian's API documentation and code structure
3. **Extensibility**: Easy to add new API groups or methods
4. **Reusability**: Mixins can be combined flexibly for different use cases
5. **Maintainability**: Changes to one API group don't affect others


3. Method Naming Convention Pattern
------------------------------------------------------------------------------
The library follows a consistent method naming convention that converts Atlassian's REST API endpoints into Pythonic method names while preserving semantics and readability.


Method Name Transformation Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Methods are named by slugifying the method names found in the official Atlassian documentation, not the API paths. This ensures semantic clarity and alignment with official documentation.

.. code-block:: text

    # Official Doc: "Get pages in space"
    → get_pages_in_space()

    # Official Doc: "Get page by ID"
    → get_page_by_id()


Implementation Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. dropdown:: atlassian_confluence/page.py

    .. literalinclude:: ../../../pyatlassian/atlassian_confluence/page.py
       :language: python
       :linenos:


Parameter Naming Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. **Path Parameters**

.. code-block:: python

    # API: /spaces/{id}/pages
    def get_pages_in_space(
        self,
        id: int,
        ...
    ):  # 'id' matches path parameter
        pass

2. **Query Parameters**

    .. code-block:: python

      # API: ?body-format=storage&get-draft=true
      def get_page_by_id(
          self,
          id: int,
          body_format: str = NA,  # hyphen → underscore
          get_draft: bool = NA,   # get-draft → get_draft
          ...
      ):
          ...


4. Parameter Handling Pattern
------------------------------------------------------------------------------
The library makes a clear distinction between required and optional parameters using Python's type system and special singleton objects. Required parameters are enforced at initialization, while optional parameters can be omitted.

.. code-block:: python

    def get_pages_in_space(
        self,
        id: int,              # Required: no default value
        depth: str = NA,      # Optional: defaults to NA
        sort: str = NA,       # Optional: defaults to NA
        status: list = NA,    # Optional: defaults to NA
        ...
    ):
        params = {
            "depth": depth,
            "sort": sort,
            "status": status,
        }
        # Remove NA parameters before making request
        params = rm_na(params)
        params = params if len(params) else None
        res = self.make_request(
            method="GET",
            url=_url,
            params=params,
        )

Key Concepts:

- Required Parameters
    - Must be provided by the caller
    - No default value assigned
    - Enforced through Python's argument system
    - Example: id
- Optional Parameters
    - Can be omitted by the caller
    - Default value is ``NA`` singleton
    - Automatically filtered out using ``rm_na``
    - Example: limit, sort, status


5. Pagination Implementation Pattern
------------------------------------------------------------------------------
The library implements a consistent pagination pattern for API endpoints that return paginated results. This pattern handles both manual and automatic pagination while maintaining a clean interface.

The pagination implementation uses recursive calls with accumulation, controlled by specific pagination parameters:

1. **Control Parameters**
    - ``paginate: bool = False`` - Enables/disables automatic pagination
    - ``max_results: int = 9999`` - Maximum number of results to return
    - ``_url: str = None`` - Internal parameter for continuation URLs
    - ``_results: list = None`` - Internal parameter for result accumulation

2. **Base URL and Results Initia    lization**

.. code-block:: python

    if _url is None:
        _url = f"{self._root_url}/spaces/{id}/pages"
    if _results is None:
        _results = []
    if len(_results) >= max_results:
        return {"results": _results}

3. **Result Accumulation**

.. code-block:: python

    _results.extend(res.get("results", []))

4. **Pagination Control Flow**

.. code-block:: python

    if "next" in res["_links"] and paginate:
        _url = f"{self.url}{res['_links']['next']}"
        _res = self.get_pages_in_space(
            # ... pass through all original parameters ...
            _url=_url,
            _results=_results,
        )

**Key Benefits**

1. **Transparency**: Users can choose between single-page and automatic pagination
2. **Control**: ``max_results`` parameter prevents unbounded result sets
3. **Efficiency**: Results are accumulated incrementally
4. **Consistency**: Same method signature works for both paginated and non-paginated requests
5. **Clean Interface**: Internal pagination parameters are hidden from API documentation

**Implementation Notes**

- Internal parameters (``_url``, ``_results``) should not be exposed in public documentation
- Result accumulation preserves the original API response structure
- Error handling and rate limiting should be considered in the implementation
