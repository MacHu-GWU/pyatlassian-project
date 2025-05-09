# -*- coding: utf-8 -*-

import time

from pyatlassian.tests import jprint, debug_page_data
from pyatlassian.tests.api_keys import sh_conf, esc_conf


def test_get_pages_for_label():
    label_id = 41943045  # "ai-esc-playbook"
    res = esc_conf.get_pages_for_label(
        id=label_id,
    )
    jprint(res)
    print("Total Pages: ", len(res["results"]))
    for page_data in res["results"]:
        debug_page_data(page_data)
    time.sleep(1)


def test_pagi_get_pages_for_label():
    label_id = 41943045  # "ai-esc-playbook"
    for res in esc_conf.pagi_get_pages_for_label(
        id=label_id,
        limit=3,
    ):
        jprint(res)
        print("Total Pages: ", len(res["results"]))
        for page_data in res["results"]:
            debug_page_data(page_data)
        time.sleep(1)


def test_get_pages():
    res = esc_conf.get_pages(
        body_format="atlas_doc_format",
        limit=250,
    )
    jprint(res)
    print("Total Pages: ", len(res["results"]))
    for page_data in res["results"]:
        debug_page_data(page_data)
    time.sleep(1)


def test_pagi_get_pages():
    for res in esc_conf.pagi_get_pages(
        body_format="atlas_doc_format",
        limit=5,
        total_max_results=10,
    ):
        jprint(res)
        print("Total Pages: ", len(res["results"]))
        for page_data in res["results"]:
            debug_page_data(page_data)
        time.sleep(1)


def test_get_page_by_id():
    page_id = 45383706  # Projects
    res = sh_conf.get_page_by_id(
        id=page_id,
        body_format="storage",
        include_labels=True,
        include_properties=True,
        include_operations=True,
        include_likes=True,
        include_versions=True,
        include_version=True,
        include_favorited_by_current_user_status=True,
    )
    jprint(res)
    time.sleep(1)


def test_get_pages_in_space():
    space_id = 45744130  # Job Work Template

    # no pagination
    res = sh_conf.get_pages_in_space(
        id=space_id,
        limit=5,
    )
    jprint(res)
    print("Total Pages: ", len(res["results"]))
    for page_data in res["results"]:
        debug_page_data(page_data)


def test_pagi_get_pages_in_space():
    space_id = 45744130  # Job Work Template
    for res in sh_conf.pagi_get_pages_in_space(
        id=space_id,
        limit=5,
        total_max_results=10,
    ):
        jprint(res)
        print("Total Pages: ", len(res["results"]))
        for page_data in res["results"]:
            debug_page_data(page_data)

        time.sleep(1)


if __name__ == "__main__":
    from pyatlassian.tests import run_cov_test

    run_cov_test(
        __file__,
        "pyatlassian.atlassian_confluence.page",
        preview=False,
    )
