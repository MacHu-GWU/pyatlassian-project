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
class IssuesMixin:
    """
    For detailed API document, see:
    https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-group-issues
    """

    def get_issue(
        self: "Jira",
        issue_id_or_key: str,
        fields: list[T_ISSUE_FIELDS] = NA,
        fields_by_keys: bool = NA,
        expand: T_ISSUE_EXPAND = NA,
        properties: list[str] = NA,
        update_history: bool = NA,
        fail_fast: bool = NA,
    ) -> T_RESPONSE:
        """
        https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-issueidorkey-get

        The issue is identified by its ID or key, however, if the identifier doesn't match
        an issue, a case-insensitive search and check for moved issues is performed.
        If a matching issue is found its details are returned, a 302 or other redirect
        is not returned. The issue key returned in the response is the key of the issue found.

        Args:
            issue_id_or_key: The ID or key of the issue
            fields: List of fields to return. Defaults to all fields if not specified.
                Use "*all" for all fields, "*navigable" for navigable fields,
                or specific field names
            fields_by_keys: Whether to reference fields by keys instead of IDs
            expand: Additional information to include in response
            properties: List of issue properties to return
            update_history: Whether to add issue to user's "Recently viewed" list
            fail_fast: Whether to fail quickly on field loading errors

        Returns:
            Complete issue details as JSON response

        API Reference:
            https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-issueidorkey-get

        Example:
            >>> jira = Jira(url="https://your-domain.atlassian.net", username="email@example.com", password="api-token")
            >>> issue = jira.get_issue(
            ...     issue_id_or_key="PROJ-123",
            ...     fields=["summary", "description"],
            ...     expand="renderedFields"
            ... )
            >>> print(issue["fields"]["summary"])
        """
        params = {
            "fields": fields,
            "fieldsByKeys": fields_by_keys,
            "expand": expand,
            "properties": properties,
            "updateHistory": update_history,
            "failFast": fail_fast,
        }
        params = rm_na(**params)
        params = params if len(params) else None

        return self.make_request(
            method="GET",
            url=f"{self._root_url}/issue/{issue_id_or_key}",
            params=params,
        )