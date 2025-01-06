# -*- coding: utf-8 -*-

import typing as T
import re
from pyatlassian.paths import dir_project_root
import pyatlassian.api as pyatlassian


def get_doc_url(doc_str: str) -> str:
    lines = doc_str.split("\n")
    doc_url = None
    for line in lines:
        line = line.strip()
        if line.startswith("https://"):
            doc_url = line
            break
    if doc_url is None:
        raise ValueError(f"Cannot find doc URL in {doc_str}")
    return doc_url


Atlassian = pyatlassian.atlassian.Atlassian
Confluence = pyatlassian.confluence.Confluence
Jira = pyatlassian.jira.Jira


_ignore_methods = [
    "request",
    "make_request",
]


def get_api_ref_doc(
    klass: T.Type[Atlassian],
) -> list[str]:
    class_name = klass.__name__
    methods = list()
    lines = []
    lines.append(f"{class_name}")
    lines.append("-" * 78)
    for method_name in dir(klass):
        if method_name.startswith("_") or (method_name in _ignore_methods):
            continue
        method = getattr(klass, method_name)
        if method.__class__.__name__ == "function":
            try:
                doc_url = get_doc_url(method.__doc__)
                methods.append((method_name, method, doc_url))
                line = f"- :meth:`~{method.__module__}.{method.__qualname__}` (`Atlassian Document <{doc_url}>`_)"
                lines.append(line)
            except ValueError as e:
                print(f"Cannot find doc URL in {class_name}.{method_name}")
                raise e
    lines.append("\n")
    return lines


lines = list()
lines.append("pyatlassian Public APIs")
lines.append("=" * 78)
lines.append("\n")
lines.extend(get_api_ref_doc(Confluence))
lines.extend(get_api_ref_doc(Jira))

path = dir_project_root.joinpath("docs", "source", "02-Public-APIs", "index.rst")
path.write_text("\n".join(lines))