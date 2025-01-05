# -*- coding: utf-8 -*-

import time

from pyatlassian.tests import jprint
from pyatlassian.tests.api_keys import esc_jira


def test_get_projects_paginated():
    res = esc_jira.get_projects_paginated()
    jprint(res)
    time.sleep(1)


def test_get_all_status_for_project():
    res = esc_jira.get_all_status_for_project(project_id_or_key="PYATLASUT")
    jprint(res)
    time.sleep(1)


if __name__ == "__main__":
    from pyatlassian.tests import run_cov_test

    run_cov_test(
        __file__,
        "pyatlassian.atlassian_jira.projects",
        preview=False,
    )
