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
class LabelMixin:
    """
    For detailed API documentation, see:
    https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-label/#api-group-label
    """

    def get_labels(
        self: "Confluence",
        label_id: T.List[int] = NA,
        prefix: T.List[str] = NA,
        sort: str = NA,
        cursor: str = NA,
        limit: int = NA,
        paginate: bool = False,
        max_results: int = 9999,
        _url: str = None,
        _results: list[T_RESPONSE] = None,
    ) -> T_RESPONSE:
        """
        For detailed parameter descriptions, see:
        https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-label/#api-labels-get

        :param paginate: If True, automatically handle pagination
        :param max_results: Maximum number of total results to return
            when ``paginate = True``
        """
        base_url = f"{self._root_url}/labels"
        params = {
            "label-id": label_id,
            "prefix": prefix,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        return self._paginate(
            base_url=base_url,
            params=params,
            paginate=paginate,
            max_results=max_results,
            _url=_url,
            _results=_results,
        )
