# -*- coding: utf-8 -*-

"""
"""

import typing as T
import dataclasses

from ..atlassian.api import (
    NA,
    rm_na,
    T_RESPONSE,
)

if T.TYPE_CHECKING:  # pragma: no cover
    from .model import Confluence


@dataclasses.dataclass
class ChildrenMixin:
    """
    - https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-children/#api-group-children
    """

    def get_child_pages(
        self: "Confluence",
        id: int,
        cursor: str = NA,
        limit: int = NA,
        sort: str = NA,
        paginate: bool = False,
        max_results: int = 9999,
        _url: str = None,
        _results: list[T_RESPONSE] = None,
    ) -> T_RESPONSE:
        """
        - https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-children/#api-pages-id-children-get
        """
        base_url = f"{self._root_url}/pages/{id}/children"
        params = {
            "cursor": cursor,
            "limit": limit,
            "sort": sort,
        }
        return self._paginate(
            base_url=base_url,
            params=params,
            paginate=paginate,
            max_results=max_results,
        )
