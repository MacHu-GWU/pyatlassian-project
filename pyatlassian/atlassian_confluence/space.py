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
    ) -> T_RESPONSE:
        """
        For detailed parameter descriptions, see:
        https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space/#api-spaces-get

        :param req_kwargs: additional ``requests.request()`` kwargs
        """
        return self.make_request(
            method="GET",
            url=f"{self._root_url}/spaces",
            req_kwargs=req_kwargs,
        )
