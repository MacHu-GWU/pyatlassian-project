# -*- coding: utf-8 -*-

import json
import time
from rich import print as rprint
from rich.console import Console
from rich.panel import Panel

from pyatlassian.tests import jprint
from pyatlassian.tests.api_keys import sh_conf, esc_conf

console = Console()


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


# ------------------------------------------------------------------------------
#
# ------------------------------------------------------------------------------
def test_get_spaces():
    # res = sh_conf.get_spaces()
    res = esc_conf.get_spaces()
    jprint(res)
    print("Total Spaces: ", len(res["results"]))
    for space_data in res.get("results", []):
        debug_space_data(space_data)
    time.sleep(1)


def test_get_pages_in_space():
    space_id = 45744130  # Job Work Template

    # no pagination
    # res = sh_conf.get_pages_in_space(
    #     space_id=space_id,
    #     limit=5,
    # )
    # jprint(res)
    # print("Total Pages: ", len(res["results"]))
    # for page_data in res["results"]:
    #     debug_page_data(page_data)

    # auto pagination
    res = sh_conf.get_pages_in_space(
        space_id=space_id,
        limit=5,
        max_results=10,
        paginate=True,
    )
    jprint(res)
    print("Total Pages: ", len(res["results"]))
    for page_data in res["results"]:
        debug_page_data(page_data)

    time.sleep(1)


# def test_get_page_by_id():
#     page_id = 45383706  # page_id = '45383706', page_title = 'Projects', page_parent_id = '45744459', page_parent_type = 'page'
#     res = sh_conf.get_page_by_id(
#         page_id=page_id,
#         body_format="storage",
#         include_labels=True,
#         include_properties=True,
#         include_operations=True,
#         include_likes=True,
#         include_versions=True,
#         include_version=True,
#         include_favorited_by_current_user_status=True,
#     )
#     jprint(res)
#     time.sleep(1)


if __name__ == "__main__":
    from pyatlassian.tests import run_unit_test

    run_unit_test(__file__)
