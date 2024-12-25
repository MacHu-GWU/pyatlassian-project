# -*- coding: utf-8 -*-

import json
import time
from rich import print as rprint
from pyatlassian.tests.api_keys import sh_conf as conf


def _test_get_spaces():
    res = conf.get_spaces()
    # rprint(res)
    for space_data in res.get("results", []):
        space_id = space_data["id"]
        space_key = space_data["key"]
        space_name = space_data["name"]
        space_type = space_data["type"]
        print(f"{space_id = }, {space_key = }, {space_name = }, {space_type = }")
    time.sleep(1)


def _test_get_pages_in_space():
    space_id = 45744130  # space_id = '45744130', space_key = 'JWT1', space_name = 'Job Work Template', space_type = 'global'
    res = conf.get_pages_in_space(
        space_id=space_id,
        limit=10,
    )
    # rprint(res)
    for page_data in res["results"]:
        page_id = page_data["id"]
        page_title = page_data["title"]
        page_parent_id = page_data["parentId"]
        page_parent_type = page_data["parentType"]
        print(
            f"{page_id = }, {page_title = }, {page_parent_id = }, {page_parent_type = }"
        )
    time.sleep(1)


def _test_get_page_by_id():
    page_id = 45383706  # page_id = '45383706', page_title = 'Projects', page_parent_id = '45744459', page_parent_type = 'page'
    res = conf.get_page_by_id(
        page_id=page_id,
        body_format="storage",
        include_labels=True,
        include_properties=True,
        include_operations=True,
        include_likes=True,
        include_versions=True,
        include_version=True,
        include_favorited_by_current_user_status=True,
    )
    print(json.dumps(res, ensure_ascii=False))
    time.sleep(1)


def test():
    print("")
    _test_get_spaces()
    _test_get_pages_in_space()
    _test_get_page_by_id()


if __name__ == "__main__":
    from pyatlassian.tests import run_unit_test

    run_unit_test(__file__)
