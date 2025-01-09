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
        req_kwargs: T.Optional[T_KWARGS] = None,
    ) -> T_RESPONSE:
        """
        https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-issueidorkey-get

        :param req_kwargs: additional ``requests.request()`` kwargs
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
            req_kwargs=req_kwargs,
        )