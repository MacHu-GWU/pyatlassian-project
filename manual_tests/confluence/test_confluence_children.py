# -*- coding: utf-8 -*-

import time

from pyatlassian.tests import jprint, debug_page_data
from pyatlassian.tests.api_keys import sh_conf, esc_conf


def test_get_pages_in_space():
    # AI Empowerment Guide: Your Personal AI Assistant Onboarding Manual
    page_id = 36700240

    # no pagination
    res = esc_conf.get_child_pages(
        id=page_id,
        limit=1,
    )
    jprint(res)
    print("Total Pages: ", len(res["results"]))
    for page_data in res["results"]:
        debug_page_data(page_data)


def test_pagi_get_pages_in_space():
    # AI Empowerment Guide: Your Personal AI Assistant Onboarding Manual
    page_id = 36700240

    # auto pagination
    for res in esc_conf.pagi_get_child_pages(
        id=page_id,
        limit=1,
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
        "pyatlassian.atlassian_confluence.children",
        preview=False,
    )
