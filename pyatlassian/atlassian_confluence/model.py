# -*- coding: utf-8 -*-

"""
"""

import typing as T
import dataclasses
from functools import cached_property

from ..atlassian.api import (
    Atlassian,
    NA,
    rm_na,
    T_RESPONSE,
    T_KWARGS,
)

from .children import ChildrenMixin
from .label import LabelMixin
from .page import PageMixin
from .space import SpaceMixin


@dataclasses.dataclass
class Confluence(
    Atlassian,
    ChildrenMixin,
    LabelMixin,
    PageMixin,
    SpaceMixin,
):
    """
    - https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#about
    """

    @cached_property
    def _root_url(self) -> str:
        return f"{self.url}/wiki/api/v2"
