# -*- coding: utf-8 -*-

import dataclasses
from functools import cached_property

from ..atlassian.api import (
    Atlassian,
)
from .issue_search import IssueSearchMixin
from .issues import IssuesMixin
from .projects import ProjectsMixin


@dataclasses.dataclass
class Jira(
    Atlassian,
    IssueSearchMixin,
    IssuesMixin,
    ProjectsMixin,
):
    """
    - https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#about
    """

    @cached_property
    def _root_url(self) -> str:
        return f"{self.url}/rest/api/3"
