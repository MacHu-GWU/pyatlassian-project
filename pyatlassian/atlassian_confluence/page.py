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
from .typehint import T_BODY_FORMAT

if T.TYPE_CHECKING:  # pragma: no cover
    from .model import Confluence


@dataclasses.dataclass
class PageMixin:
    """
    - https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-group-page
    """

    def get_pages_in_space(
        self: "Confluence",
        id: int,
        depth: str = NA,
        sort: str = NA,
        status: list[
            T.Literal[
                "current",
                "archived",
                "trashed",
                "deleted",
            ]
        ] = NA,
        title: str = NA,
        body_format: T_BODY_FORMAT = NA,
        cursor: str = NA,
        limit: int = NA,
        paginate: bool = False,
        max_results: int = 9999,
        _url: str = None,
        _results: list[T_RESPONSE] = None,
    ) -> T_RESPONSE:
        """
        - https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-spaces-id-pages-get

        :param paginate: If True, will auto paginate until all pages are fetched.
        """
        base_url = f"{self._root_url}/spaces/{id}/pages"
        params = {
            "depth": depth,
            "sort": sort,
            "status": status,
            "title": title,
            "body-format": body_format,
            "cursor": cursor,
            "limit": limit,
        }
        return self._paginate(
            base_url=base_url,
            params=params,
            paginate=paginate,
            max_results=max_results,
        )

    def get_page_by_id(
        self: "Confluence",
        id: int,
        body_format: T_BODY_FORMAT = NA,
        get_draft: bool = NA,
        status: list[
            T.Literal[
                "current",
                "archived",
                "trashed",
                "deleted",
                "historical",
                "draft",
            ]
        ] = NA,
        version: int = NA,
        include_labels: bool = NA,
        include_properties: bool = NA,
        include_operations: bool = NA,
        include_likes: bool = NA,
        include_versions: bool = NA,
        include_version: bool = NA,
        include_favorited_by_current_user_status: bool = NA,
    ):
        """
        - https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-pages-id-get
        """
        params = {
            "body-format": body_format,
            "get-draft": get_draft,
            "status": status,
            "version": version,
            "include-labels": include_labels,
            "include-properties": include_properties,
            "include-operations": include_operations,
            "include-likes": include_likes,
            "include-versions": include_versions,
            "include-version": include_version,
            "include-favorited-by-current-user-status": include_favorited_by_current_user_status,
        }
        params = rm_na(**params)
        params = params if len(params) else None
        return self.make_request(
            method="GET",
            url=f"{self._root_url}/pages/{id}",
            params=params,
        )
