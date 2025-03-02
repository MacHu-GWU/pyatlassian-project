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
        req_kwargs: T.Optional[T_KWARGS] = None,
        _url: str = None,
    ) -> T_RESPONSE:
        """
        For detailed parameter descriptions, see:
        https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-label/#api-labels-get

        :param req_kwargs: additional ``requests.request()`` kwargs
        """
        if _url is None:
            url = f"{self._root_url}/labels"
        else:
            url = _url
        params = {
            "label-id": label_id,
            "prefix": prefix,
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

    def pagi_get_labels(
        self: "Confluence",
        label_id: T.List[int] = NA,
        prefix: T.List[str] = NA,
        sort: str = NA,
        cursor: str = NA,
        limit: int = NA,
        req_kwargs: T.Optional[T_KWARGS] = None,
        total_max_results: int = 9999,
    ) -> T.Iterable[T_RESPONSE]:
        """
        For detailed parameter descriptions, see:
        https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-label/#api-labels-get

        :param req_kwargs: additional ``requests.request()`` kwargs
        :param total_max_results: total max results to fetch in all response
        """

        def get_next_token(res):
            return res.get("_links", {}).get("next")

        def set_next_token(kwargs, next_token):
            kwargs["_url"] = f"{self.url}{next_token}"

        yield from _paginate(
            method=self.get_labels,
            list_key="results",
            get_next_token=get_next_token,
            set_next_token=set_next_token,
            kwargs=dict(
                label_id=label_id,
                prefix=prefix,
                sort=sort,
                cursor=cursor,
                limit=limit,
                req_kwargs=req_kwargs,
            ),
            max_results=total_max_results,
        )
