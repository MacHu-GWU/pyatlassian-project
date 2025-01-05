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
    # Children
    # --------------------------------------------------------------------------
    __anchore_children = None

    def get_child_pages(
        self,
        page_id: int,

        paginate: bool = False,
        _url: str = None,
        _results: list[T_RESPONSE] = None,
    ):
        pass

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
        max_results: int = 9999,
        paginate: bool = False,
        _url: str = None,
        _results: list[T_RESPONSE] = None,
    ) -> T_RESPONSE:
        """
        - https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-spaces-id-pages-get

        :param paginate: If True, will auto paginate until all pages are fetched.
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
        if _url is None:
            _url = f"{self._root_url}/spaces/{space_id}/pages"
        res = self.make_request(
            method="GET",
            url=_url,
            params=params,
        )
        if _results is None:
            _results = []
        _results.extend(res.get("results", []))
        if "next" in res["_links"] and paginate:
            _url = f"{self.url}{res['_links']['next']}"
            _res = self.get_pages_in_space(
                space_id=space_id,
                depth=depth,
                sort=sort,
                status=status,
                title=title,
                body_format=body_format,
                cursor=cursor,
                limit=limit,
                paginate=True,
                _url=_url,
                _results=_results,
            )
        else:
            _res = None

        if _res is None:
            res["results"] = _results
        else:
            res = {"results": _results}
        return res

    def get_page_by_id(
        self,
        page_id,
        body_format: T.Optional[str] = NA,
        get_draft: T.Optional[bool] = NA,
        status: T.Optional[T.List[str]] = NA,
        version: T.Optional[int] = NA,
        include_labels: T.Optional[bool] = NA,
        include_properties: T.Optional[bool] = NA,
        include_operations: T.Optional[bool] = NA,
        include_likes: T.Optional[bool] = NA,
        include_versions: T.Optional[bool] = NA,
        include_version: T.Optional[bool] = NA,
        include_favorited_by_current_user_status: T.Optional[bool] = NA,
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
