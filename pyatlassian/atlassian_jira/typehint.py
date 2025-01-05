# -*- coding: utf-8 -*-

import typing as T

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
