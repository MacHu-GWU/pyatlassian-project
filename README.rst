
.. image:: https://readthedocs.org/projects/pyatlassian/badge/?version=latest
    :target: https://pyatlassian.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://github.com/MacHu-GWU/pyatlassian-project/actions/workflows/main.yml/badge.svg
    :target: https://github.com/MacHu-GWU/pyatlassian-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/MacHu-GWU/pyatlassian-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/pyatlassian-project

.. image:: https://img.shields.io/pypi/v/pyatlassian.svg
    :target: https://pypi.python.org/pypi/pyatlassian

.. image:: https://img.shields.io/pypi/l/pyatlassian.svg
    :target: https://pypi.python.org/pypi/pyatlassian

.. image:: https://img.shields.io/pypi/pyversions/pyatlassian.svg
    :target: https://pypi.python.org/pypi/pyatlassian

.. image:: https://img.shields.io/badge/Release_History!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/pyatlassian-project/blob/main/release-history.rst

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/pyatlassian-project

------

.. image:: https://img.shields.io/badge/Link-Document-blue.svg
    :target: https://pyatlassian.readthedocs.io/en/latest/

.. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://pyatlassian.readthedocs.io/en/latest/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/pyatlassian-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/pyatlassian-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/pyatlassian-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/pyatlassian#files


Welcome to ``pyatlassian`` Documentation
==============================================================================
.. image:: https://pyatlassian.readthedocs.io/en/latest/_static/pyatlassian-logo.png
    :target: https://pyatlassian.readthedocs.io/en/latest/

``pyatlassian`` provides a clean, intuitive, and fully-typed Python interface for interacting with Atlassian's cloud services like Confluence and Jira. While other Python clients exist for Atlassian's APIs, many are based on outdated APS specifications. PyAtlassian is built from the ground up to work seamlessly with the latest REST API versions.

**Key Features**

- Modern Python Support: Built for modern Python with full type hints
- Cloud-First Design: Optimized for Atlassian cloud services
- REST API Focused: Direct interface with the latest Atlassian REST APIs
- Products Supported:
    - Confluence Cloud
    - JIRA Cloud
    - More products coming soon...

**Development Philosophy**

While the initial vision for ``pyatlassian`` included automatic code generation from OpenAPI specifications, we chose a pragmatic approach focused on delivering immediate value. Here's why:

- Focus on Immediate Needs: Rather than waiting for a complete OpenAPI-based solution, we're manually implementing the most critical API endpoints to provide a working solution sooner.
- Quality Over Automation: Hand-crafted implementations allow us to provide a more Pythonic and intuitive interface, optimized for real-world usage patterns.
- Parallel Development: While this project delivers immediate value through manual implementation, we maintain a separate project focused on OpenAPI-based generation for future scalability.


.. _install:

Install
------------------------------------------------------------------------------

``pyatlassian`` is released on PyPI, so all you need is to:

.. code-block:: console

    $ pip install pyatlassian

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade pyatlassian
