# -*- coding: utf-8 -*-

from rich.panel import Panel

from .helper import console


def debug_page_data(data: dict):
    id = data["id"]
    title = data["title"]
    parent_id = data["parentId"]
    parent_type = data["parentType"]
    content = "\n".join(
        [
            f"{parent_id = }",
            f"{parent_type = }",
        ]
    )
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
