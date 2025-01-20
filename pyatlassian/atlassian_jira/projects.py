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
        req_kwargs: T.Optional[T_KWARGS] = None,
        _url: str = None,
    ) -> T_RESPONSE:
        """
        For detailed parameter descriptions, see:
        https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-search-get

        :param req_kwargs: additional ``requests.request()`` kwargs
        """
        if _url is None:
            url = f"{self._root_url}/project/search"
        else:
            url = _url
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
        return self.make_request(
            method="GET",
            url=url,
            params=params,
            req_kwargs=req_kwargs,
        )

    def pagi_get_projects_paginated(
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
        req_kwargs: T.Optional[T_KWARGS] = None,
        total_max_results: int = 9999,
    ) -> T.Iterable[T_RESPONSE]:
        """
        For detailed parameter descriptions, see:
        https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-search-get

        :param req_kwargs: additional ``requests.request()`` kwargs
        :param total_max_results: total max results to fetch in all response
        """

        def get_next_token(res):
            return res.get("nextPage")

        def set_next_token(kwargs, next_token):
            kwargs["_url"] = next_token

        yield from _paginate(
            method=self.get_projects_paginated,
            list_key="values",
            get_next_token=get_next_token,
            set_next_token=set_next_token,
            kwargs=dict(
                start_at=start_at,
                max_results=max_results,
                order_by=order_by,
                id=id,
                keys=keys,
                query=query,
                type_key=type_key,
                category_id=category_id,
                action=action,
                expand=expand,
                status=status,
                properties=properties,
                property_query=property_query,
                req_kwargs=req_kwargs,
            ),
            max_results=total_max_results,
        )

    def get_all_status_for_project(
        self: "Jira",
        project_id_or_key: str,
        req_kwargs: T.Optional[T_KWARGS] = None,
    ) -> T_RESPONSE:
        """
        For detailed parameter descriptions, see:
        https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-projectidorkey-statuses-get

        :param req_kwargs: additional ``requests.request()`` kwargs
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
            req_kwargs=req_kwargs,
        )
