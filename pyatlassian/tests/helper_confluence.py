# -*- coding: utf-8 -*-

from rich.panel import Panel

from .helper import console


def debug_label_data(data: dict):
    id = data["id"]
    name = data["name"]
    prefix = data["prefix"]
    panel = Panel(f"{id = }, {name = }, {prefix = }")
    console.print(panel)


def debug_page_data(data: dict):
    id = data["id"]
    title = data["title"]

    more_attrs = []

    if "parentId" in data:
        parent_id = data["parentId"]
        more_attrs.append(f"{parent_id = }")

    if "parentType" in data:
        parent_type = data["parentType"]
        more_attrs.append(f"{parent_type = }")

    content = "\n".join(more_attrs)
    panel = Panel(content, title=f"page_title = {title}, {id = }")
    console.print(panel)


def debug_space_data(data: dict):
    id = data["id"]
    key = data["key"]
    name = data["name"]
    type = data["type"]
    content = "\n".join(
        [
            f"{type = }",
        ]
    )
    panel = Panel(content, title=f"space_name = {name}, {id = }, {key = }")
    console.print(panel)
