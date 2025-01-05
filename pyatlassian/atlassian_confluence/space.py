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
class SpaceMixin:
    """
    - https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space/#api-group-space
    """

    def get_spaces(self: "Confluence") -> T_RESPONSE:
        """
        - https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space/#api-spaces-get
        """
        return self.make_request(
            method="GET",
            url=f"{self._root_url}/spaces",
        )
