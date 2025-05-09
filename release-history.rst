.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.3.2 (2025-05-09)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- ``Confluence.get_spaces`` now supports all parameter.
- ``Confluence.pagi_get_spaces`` now supports all parameter.


0.3.1 (2025-03-02)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add a lot paginator version of "list" methods:
    - ``Confluence.pagi_get_child_pages``
    - ``Confluence.pagi_get_labels``
    - ``Confluence.pagi_get_pages``
    - ``Confluence.pagi_get_pages_for_label``
    - ``Confluence.pagi_get_pages_in_space``
    - ``Confluence.pagi_get_projects_paginated``
    - ``Confluence.pagi_get_space``


0.2.2 (2025-01-12)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Minor Improvements**

- Add the ``req_kwargs`` argument to all API method to allow user to pass custom parameters to  python ``requests.request()``.


0.2.1 (2025-01-05)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add support for Jira
- Add a lot more Confluence api methods.
- Add the following public API:
    - ``Confluence.get_child_pages``
    - ``Confluence.get_labels``
    - ``Confluence.get_pages``
    - ``Confluence.get_pages_for_label``
    - ``Jira.get_all_status_for_project``
    - ``Jira.get_all_users``
    - ``Jira.get_issue``
    - ``Jira.get_projects_paginated``
    - ``Jira.search_for_issues_using_jql_enhanced_search``


0.1.1 (2024-12-25)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- First release
- Add the following public API:
    - ``Confluence``
    - ``Confluence.get_page_by_id``
    - ``Confluence.get_pages_in_space``
    - ``Confluence.get_spaces``
