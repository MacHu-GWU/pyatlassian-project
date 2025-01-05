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
from .projects import ProjectsMixin

@dataclasses.dataclass
class Jira(
    Atlassian,
    ProjectsMixin,
):
    """
    - https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#about
    """

    @cached_property
    def _root_url(self) -> str:
        return f"{self.url}/rest/api/3"

    # --------------------------------------------------------------------------
    # Projects
    # https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/#api-group-projects
    # --------------------------------------------------------------------------
    __anchore_projects = None

    def get_projects(
        self,
        max_results: int = NA,
    ) -> T_RESPONSE:
        """
        - https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-search-get
        """
        params = {
            "maxResults": max_results,
        }
        params = rm_na(**params)
        params = params if len(params) else None
        return self.make_request(
            method="GET",
            url=f"{self._root_url}/project/search",
            params=params,
        )

    # --------------------------------------------------------------------------
    # Issues Search
    # https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/#api-group-issue-search
    # --------------------------------------------------------------------------
    __anchore_issues_search = None

    def search_for_issues_using_jql_enhanced_search(
        self,
        jql: str = NA,
        next_page_token: str = NA,
        max_results: int = NA,
        fields: T.List[str] = NA,
    ) -> T_RESPONSE:
        """
        - https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/#api-rest-api-3-search-jql-get
        """
        params = {
            "jql": jql,
            "nextPageToken": next_page_token,
            "maxResults": max_results,
            "fields": fields,
        }
        params = rm_na(**params)
        params = params if len(params) else None
        return self.make_request(
            method="GET",
            url=f"{self._root_url}/search/jql",
            params=params,
        )
