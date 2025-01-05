# -*- coding: utf-8 -*-

"""
"""

import dataclasses
from functools import cached_property

from ..atlassian.api import Atlassian

from .page import PageMixin
from .space import SpaceMixin


@dataclasses.dataclass
class Confluence(
    Atlassian,
    PageMixin,
    SpaceMixin,
):
    """
    - https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#about
    """

    @cached_property
    def _root_url(self) -> str:
        return f"{self.url}/wiki/api/v2"
