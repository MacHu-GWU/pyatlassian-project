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
from .typehint import T_ISSUE_FIELDS, T_ISSUE_EXPAND

if T.TYPE_CHECKING:  # pragma: no cover
    from .model import Jira


@dataclasses.dataclass
class IssueSearchMixin:
    """
    For detailed API document, see:
    https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/#api-group-issue-search
    """

    def search_for_issues_using_jql_enhanced_search(
        self: "Jira",
        jql: str = NA,
        next_page_token: str = NA,
        max_results: int = NA,
        fields: list[T_ISSUE_FIELDS] = NA,
        expand: T_ISSUE_EXPAND = NA,
        properties: list[str] = NA,
        fields_by_keys: bool = NA,
        fail_fast: bool = NA,
        reconcile_issues: list[int] = NA,
    ) -> T_RESPONSE:
        """
        For detailed parameter descriptions, see:
        https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/#api-rest-api-3-search-jql-get
        """
        params = {
            "jql": jql,
            "nextPageToken": next_page_token,
            "maxResults": max_results,
            "fields": fields,
            "expand": expand,
            "properties": properties,
            "fieldsByKeys": fields_by_keys,
            "failFast": fail_fast,
            "reconcileIssues": reconcile_issues,
        }
        params = rm_na(**params)
        params = params if len(params) else None

        return self.make_request(
            method="GET",
            url=f"{self._root_url}/search/jql",
            params=params,
        )