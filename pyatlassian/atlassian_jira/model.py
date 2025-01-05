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


@dataclasses.dataclass
class Jira(Atlassian):
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

    def get_all_status_for_project(
        self,
        project_id_or_key: str,
    ) -> T_RESPONSE:
        """
        - https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-projectidorkey-statuses-get
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

    def get_page_by_id(
        self,
        page_id,
        body_format: T.Optional[str] = None,
        get_draft: T.Optional[bool] = None,
        status: T.Optional[T.List[str]] = None,
        version: T.Optional[int] = None,
        include_labels: T.Optional[bool] = None,
        include_properties: T.Optional[bool] = None,
        include_operations: T.Optional[bool] = None,
        include_likes: T.Optional[bool] = None,
        include_versions: T.Optional[bool] = None,
        include_version: T.Optional[bool] = None,
        include_favorited_by_current_user_status: T.Optional[bool] = None,
    ):
        """
        - https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-pages-id-get
        """
        params = {
            "body-format": body_format,
            "get-draft": get_draft,
            "status": status,
            "version": version,
            "include-labels": include_labels,
            "include-properties": include_properties,
            "include-operations": include_operations,
            "include-likes": include_likes,
            "include-versions": include_versions,
            "include-version": include_version,
            "include-favorited-by-current-user-status": include_favorited_by_current_user_status,
        }
        params = rm_na(**params)
        params = params if len(params) else None
        return self.make_request(
            method="GET",
            url=f"{self._root_url}/pages/{page_id}",
            params=params,
        )
