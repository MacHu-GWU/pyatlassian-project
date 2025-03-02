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
class SpaceMixin:
    """
    For detailed API document, see:
    https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space/#api-group-space
    """

    def get_spaces(
        self: "Confluence",
        req_kwargs: T.Optional[T_KWARGS] = None,
        _url: str = None,
    ) -> T_RESPONSE:
        """
        For detailed parameter descriptions, see:
        https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space/#api-spaces-get

        :param req_kwargs: additional ``requests.request()`` kwargs
        """
        if _url is None:
            url = f"{self._root_url}/spaces"
        else:
            url = _url
        return self.make_request(
            method="GET",
            url=url,
            req_kwargs=req_kwargs,
        )

    def pagi_get_spaces(
        self: "Confluence",
        req_kwargs: T.Optional[T_KWARGS] = None,
        total_max_results: int = 9999,
    ) -> T.Iterable[T_RESPONSE]:
        """
        For detailed parameter descriptions, see:
        https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space/#api-spaces-get

        :param req_kwargs: additional ``requests.request()`` kwargs
        :param total_max_results: total max results to fetch in all response
        """

        def get_next_token(res):
            return res.get("_links", {}).get("next")

        def set_next_token(kwargs, next_token):
            kwargs["_url"] = f"{self.url}{next_token}"

        yield from _paginate(
            method=self.get_spaces,
            list_key="results",
            get_next_token=get_next_token,
            set_next_token=set_next_token,
            kwargs=dict(
                req_kwargs=req_kwargs,
            ),
            max_results=total_max_results,
        )
