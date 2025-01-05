# -*- coding: utf-8 -*-

import typing as T

T_BODY_FORMAT = T.Literal[
    "storage",
    "atlas_doc_format",
    "view",
    "export_view",
    "anonymous_export_view",
    "styled_view",
    "editor",
]

T_PAGE_STATUS = T.Literal[
    "current",
    "archived",
    "deleted",
    "trashed",
]

T_PAGE_SORT_ORDER = T.Literal[
    "id",
    "-id",
    "title",
    "-title",
    "created-date",
    "-created-date",
    "modified-date",
    "-modified-date",
]
