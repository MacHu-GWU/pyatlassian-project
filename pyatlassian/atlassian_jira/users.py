# -*- coding: utf-8 -*-

"""
"""

import typing as T
import dataclasses

from ..atlassian.api import (
    NA,
    rm_na,
    T_RESPONSE,
    T_KWARGS,
)

if T.TYPE_CHECKING:  # pragma: no cover
    from .model import Jira


@dataclasses.dataclass
class UsersMixin:
    """
    For detailed API document, see:
    https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-users/#api-group-users
    """

    def get_all_users(
        self: "Jira",
        start_at: int = NA,
        max_results: int = NA,
        req_kwargs: T.Optional[T_KWARGS] = None,
    ) -> T_RESPONSE:
        """
        For detailed parameter descriptions, see:
        https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-users-search-get

        :param req_kwargs: additional ``requests.request()`` kwargs
        """
        params = {
            "startAt": start_at,
            "maxResults": max_results,
        }
        params = rm_na(**params)
        res = self.make_request(
            method="GET",
            url=f"{self._root_url}/users/search",
            params=params,
            req_kwargs=req_kwargs,
        )
        return res
