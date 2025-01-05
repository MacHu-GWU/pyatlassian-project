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
from .typehint import (
    T_PROJECT_ORDER_BY,
    T_PROJECT_ACTION,
    T_PROJECT_STATUS,
)

if T.TYPE_CHECKING:  # pragma: no cover
    from .model import Jira


@dataclasses.dataclass
class ProjectsMixin:
    """
    For detailed API document, see:
    https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/#api-group-projects
    """

    def get_projects_paginated(
        self: "Jira",
        start_at: int = NA,
        max_results: int = NA,
        order_by: T_PROJECT_ORDER_BY = NA,
        id: T.List[int] = NA,
        keys: T.List[str] = NA,
        query: str = NA,
        type_key: str = NA,
        category_id: int = NA,
        action: T_PROJECT_ACTION = NA,
        expand: str = NA,
        status: T.List[T_PROJECT_STATUS] = NA,
        properties: T.List[str] = NA,
        property_query: str = NA,
    ) -> T_RESPONSE:
        """
        For detailed parameter descriptions, see:
        https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-search-get
        """
        base_url = f"{self._root_url}/project/search"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "orderBy": order_by,
            "id": id,
            "keys": keys,
            "query": query,
            "typeKey": type_key,
            "categoryId": category_id,
            "action": action,
            "expand": expand,
            "status": status,
            "properties": properties,
            "propertyQuery": property_query,
        }
        params = rm_na(**params)
        res = self.make_request(
            method="GET",
            url=base_url,
            params=params,
        )
        return res

    def get_all_status_for_project(
        self: "Jira",
        project_id_or_key: str,
    ) -> T_RESPONSE:
        """
        For detailed parameter descriptions, see:
        https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-projectidorkey-statuses-get
        """
        params = {
            "projectIdOrKey": project_id_or_key,
        }
        params = rm_na(**params)
        params = params if len(params) else None
        return self.make_request(
            method="GET",
            url=f"{self._root_url}/project/{project_id_or_key}/statuses",
            params=params,
        )
