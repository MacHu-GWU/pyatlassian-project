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
        req_kwargs: T.Optional[T_KWARGS] = None,
    ) -> T_RESPONSE:
        """
        For detailed parameter descriptions, see:
        https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/#api-rest-api-3-search-jql-get

        :param req_kwargs: additional ``requests.request()`` kwargs
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
            req_kwargs=req_kwargs,
        )

    def pagi_search_for_issues_using_jql_enhanced_search(
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
        req_kwargs: T.Optional[T_KWARGS] = None,
        total_max_results: int = 9999,
    ) -> T.Iterable[T_RESPONSE]:
        """
        For detailed parameter descriptions, see:
        https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/#api-rest-api-3-search-jql-get

        :param req_kwargs: additional ``requests.request()`` kwargs
        :param total_max_results: total max results to fetch in all response
        """

        def get_next_token(res):
            return res.get("nextPageToken")

        def set_next_token(kwargs, next_token):
            kwargs["next_page_token"] = next_token

        yield from _paginate(
            method=self.search_for_issues_using_jql_enhanced_search,
            list_key="issues",
            get_next_token=get_next_token,
            set_next_token=set_next_token,
            kwargs=dict(
                jql=jql,
                next_page_token=next_page_token,
                max_results=max_results,
                fields=fields,
                expand=expand,
                properties=properties,
                fields_by_keys=fields_by_keys,
                fail_fast=fail_fast,
                reconcile_issues=reconcile_issues,
                req_kwargs=req_kwargs,
            ),
            max_results=total_max_results,
        )
