# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

from ..atlassian.api import (
    ParamError,
    REQ,
    NA,
    rm_na,
    BaseModel,
    T_RESPONSE,
    Atlassian,
)


@dataclasses.dataclass
class Confluence(Atlassian):
    """
    - https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#about
    """
    @cached_property
    def _root_url(self) -> str:
        return f"{self.url}/wiki/api/v2"

    # --------------------------------------------------------------------------
    # Spaces
    # --------------------------------------------------------------------------
    __anchore_spaces = None

    def get_spaces(self) -> T_RESPONSE:
        """
        - https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space/#api-spaces-get
        """
        return self.make_request(
            method="GET",
            url=f"{self._root_url}/spaces",
        )

    # --------------------------------------------------------------------------
    # Pages
    # --------------------------------------------------------------------------
    __anchore_pages = None

    def get_pages_in_space(
        self,
        space_id: int,
        depth: str = NA,
        sort: str = NA,
        status: T.List[str] = NA,
        title: str = NA,
        body_format: str = NA,
        cursor: str = NA,
        limit: int = NA,
    ) -> T_RESPONSE:
        """
        - https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-spaces-id-pages-get
        """
        params = {
            "depth": depth,
            "sort": sort,
            "status": status,
            "title": title,
            "body-format": body_format,
            "cursor": cursor,
            "limit": limit,
        }
        params = rm_na(**params)
        params = params if len(params) else None
        return self.make_request(
            method="GET",
            url=f"{self._root_url}/spaces/{space_id}/pages",
            params=params,
        )

    def get_page_by_id(
        self,
        page_id,
        body_format: T.Optional[str] = None,
        get_draft: T.Optional[bool] = None,
        status: T.Optional[T.List[str]] = None,
        version: T.Optional[int] = None,
        include_labels: T.Optional[bool] = None,
        include_properties: T.Optional[bool] = None,
        include_operations: T.Optional[bool] = None,
        include_likes: T.Optional[bool] = None,
        include_versions: T.Optional[bool] = None,
        include_version: T.Optional[bool] = None,
        include_favorited_by_current_user_status: T.Optional[bool] = None,
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
            url=f"{self._root_url}/pages/{page_id}",
            params=params,
        )
