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
        paginate: bool = False,
        max_results: int = NA,
        fields: list[T_ISSUE_FIELDS] = NA,
        expand: T_ISSUE_EXPAND = NA,
        properties: list[str] = NA,
        fields_by_keys: bool = NA,
        fail_fast: bool = NA,
        reconcile_issues: list[int] = NA,
        req_kwargs: T.Optional[T_KWARGS] = None,
        _issues: list[T_RESPONSE] = None,
    ) -> T_RESPONSE:
        """
        For detailed parameter descriptions, see:
        https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/#api-rest-api-3-search-jql-get

        :param paginate: If True, automatically handle pagination
            the ``max_results`` is a JIRA API original parameter. Let's say you have
            100 issues in total and you set ``max_results = 3``, the API will return 3 issues
            when paginate is False. If you set paginate = True, then it will return all 100 issues.
        :param req_kwargs: additional ``requests.request()`` kwargs
        """
        if _issues is None:
            _issues = []
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
        res = self.make_request(
            method="GET",
            url=f"{self._root_url}/search/jql",
            params=params,
            req_kwargs=req_kwargs,
        )
        _issues.extend(res.get("issues", []))
        if ("nextPageToken" in res) and paginate:
            _res = self.search_for_issues_using_jql_enhanced_search(
                jql=jql,
                next_page_token=res["nextPageToken"],
                paginate=paginate,
                max_results=max_results,
                fields=fields,
                expand=expand,
                properties=properties,
                fields_by_keys=fields_by_keys,
                fail_fast=fail_fast,
                reconcile_issues=reconcile_issues,
                req_kwargs=req_kwargs,
                _issues=_issues,
            )
        else:
            _res = None

        # Return results
        if _res is None:
            res["issues"] = _issues
        else:
            res = {"issues": _issues}
        return res
