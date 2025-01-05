# -*- coding: utf-8 -*-

import typing as T

T_ISSUE_FIELDS = T.Literal[
    "*all",
    "*navigable",
    "id",
    "summary",
    "description",
]

T_ISSUE_EXPAND = T.Literal[
    "renderedFields",
    "names",
    "schema",
    "transitions",
    "operations",
    "editmeta",
    "changelog",
    "versionedRepresentations",
]

T_PROJECT_ORDER_BY = T.Literal[
    "category",
    "-category",
    "+category",
    "key",
    "-key",
    "+key",
    "name",
    "-name",
    "+name",
    "owner",
    "-owner",
    "+owner",
    "issueCount",
    "-issueCount",
    "+issueCount",
    "lastIssueUpdatedDate",
    "-lastIssueUpdatedDate",
    "+lastIssueUpdatedDate",
    "archivedDate",
    "+archivedDate",
    "-archivedDate",
    "deletedDate",
    "+deletedDate",
    "-deletedDate",
]

T_PROJECT_ACTION = T.Literal["view", "browse", "edit", "create"]

T_PROJECT_STATUS = T.Literal["live", "archived", "deleted"]
