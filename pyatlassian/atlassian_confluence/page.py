# -*- coding: utf-8 -*-

"""
"""

import typing as T
import dataclasses

from ..pagi import _paginate
from ..atlassian.api import (
    NA,
    rm_na,
    T_RESPONSE,
    T_KWARGS,
)
from .typehint import T_BODY_FORMAT, T_PAGE_STATUS, T_PAGE_SORT_ORDER

if T.TYPE_CHECKING:  # pragma: no cover
    from .model import Confluence


@dataclasses.dataclass
class PageMixin:
    """
    For detailed API document, see:
    https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-group-page
    """

    def get_pages_for_label(
        self: "Confluence",
        id: int,
        space_id: list[int] = NA,
        body_format: T_BODY_FORMAT = NA,
        sort: T_PAGE_SORT_ORDER = NA,
        cursor: str = NA,
        limit: int = NA,
        req_kwargs: T.Optional[T_KWARGS] = None,
        _url: str = None,
    ) -> T_RESPONSE:
        """
        For detailed parameter descriptions, see:
        https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-labels-id-pages-get

        :param req_kwargs: additional ``requests.request()`` kwargs
        """
        if _url is None:
            url = f"{self._root_url}/labels/{id}/pages"
        else:
            url = _url
        params = {
            "space-id": space_id,
            "body-format": body_format,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        params = rm_na(**params)
        params = params if len(params) else None
        return self.make_request(
            method="GET",
            url=url,
            params=params,
            req_kwargs=req_kwargs,
        )

    def pagi_get_pages_for_label(
        self: "Confluence",
        id: int,
        space_id: list[int] = NA,
        body_format: T_BODY_FORMAT = NA,
        sort: T_PAGE_SORT_ORDER = NA,
        cursor: str = NA,
        limit: int = NA,
        req_kwargs: T.Optional[T_KWARGS] = None,
        total_max_results: int = 9999,
    ) -> T.Iterable[T_RESPONSE]:
        """
        For detailed parameter descriptions, see:
        https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-labels-id-pages-get

        :param req_kwargs: additional ``requests.request()`` kwargs
        :param total_max_results: total max results to fetch in all response
        """

        def get_next_token(res):
            return res.get("_links", {}).get("next")

        def set_next_token(kwargs, next_token):
            kwargs["_url"] = f"{self.url}{next_token}"

        yield from _paginate(
            method=self.get_pages_for_label,
            list_key="results",
            get_next_token=get_next_token,
            set_next_token=set_next_token,
            kwargs=dict(
                id=id,
                space_id=space_id,
                body_format=body_format,
                sort=sort,
                cursor=cursor,
                limit=limit,
                req_kwargs=req_kwargs,
            ),
            max_results=total_max_results,
        )

    def get_pages(
        self: "Confluence",
        id: list[int] = NA,
        space_id: list[int] = NA,
        sort: T_PAGE_SORT_ORDER = NA,
        status: list[T_PAGE_STATUS] = NA,
        title: str = NA,
        body_format: T_BODY_FORMAT = NA,
        cursor: str = NA,
        limit: int = NA,
        req_kwargs: T.Optional[T_KWARGS] = None,
        _url: str = None,
    ) -> T_RESPONSE:
        """
        For detailed parameter descriptions, see:
        https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-pages-get

        :param paginate: If True, automatically handle pagination
        :param max_results: Maximum number of total results to return
            when ``paginate = True``
        :param req_kwargs: additional ``requests.request()`` kwargs
        """
        if _url is None:
            url = f"{self._root_url}/pages"
        else:
            url = _url
        params = {
            "id": id,
            "space-id": space_id,
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
            url=url,
            params=params,
            req_kwargs=req_kwargs,
        )

    def pagi_get_pages(
        self: "Confluence",
        id: list[int] = NA,
        space_id: list[int] = NA,
        sort: T_PAGE_SORT_ORDER = NA,
        status: list[T_PAGE_STATUS] = NA,
        title: str = NA,
        body_format: T_BODY_FORMAT = NA,
        cursor: str = NA,
        limit: int = NA,
        req_kwargs: T.Optional[T_KWARGS] = None,
        total_max_results: int = 9999,
    ) -> T.Iterable[T_RESPONSE]:
        """
        For detailed parameter descriptions, see:
        https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-pages-get

        :param req_kwargs: additional ``requests.request()`` kwargs
        :param total_max_results: total max results to fetch in all response
        """

        def get_next_token(res):
            return res.get("_links", {}).get("next")

        def set_next_token(kwargs, next_token):
            kwargs["_url"] = f"{self.url}{next_token}"

        yield from _paginate(
            method=self.get_pages,
            list_key="results",
            get_next_token=get_next_token,
            set_next_token=set_next_token,
            kwargs=dict(
                id=id,
                space_id=space_id,
                sort=sort,
                status=status,
                title=title,
                body_format=body_format,
                cursor=cursor,
                limit=limit,
                req_kwargs=req_kwargs,
            ),
            max_results=total_max_results,
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
        req_kwargs: T.Optional[T_KWARGS] = None,
    ):
        """
        For detailed parameter descriptions, see:
        https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-pages-id-get

        :param req_kwargs: additional ``requests.request()`` kwargs
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
            req_kwargs=req_kwargs,
        )

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
        req_kwargs: T.Optional[T_KWARGS] = None,
        _url: str = None,
    ) -> T_RESPONSE:
        """
        For detailed parameter descriptions, see:
        https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-spaces-id-pages-get

        :param req_kwargs: additional ``requests.request()`` kwargs
        """
        if _url is None:
            url = f"{self._root_url}/spaces/{id}/pages"
        else:
            url = _url
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
            url=url,
            params=params,
            req_kwargs=req_kwargs,
        )

    def pagi_get_pages_in_space(
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
        req_kwargs: T.Optional[T_KWARGS] = None,
        total_max_results: int = 9999,
    ) -> T.Iterable[T_RESPONSE]:
        """
        For detailed parameter descriptions, see:
        https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-spaces-id-pages-get

        :param req_kwargs: additional ``requests.request()`` kwargs
        :param total_max_results: total max results to fetch in all response
        """

        def get_next_token(res):
            return res.get("_links", {}).get("next")

        def set_next_token(kwargs, next_token):
            kwargs["_url"] = f"{self.url}{next_token}"

        yield from _paginate(
            method=self.get_pages_in_space,
            list_key="results",
            get_next_token=get_next_token,
            set_next_token=set_next_token,
            kwargs=dict(
                id=id,
                depth=depth,
                sort=sort,
                status=status,
                title=title,
                body_format=body_format,
                cursor=cursor,
                limit=limit,
                req_kwargs=req_kwargs,
            ),
            max_results=total_max_results,
        )
