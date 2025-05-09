# -*- coding: utf-8 -*-

import time

from pyatlassian.tests import jprint
from pyatlassian.tests.api_keys import esc_jira


def test_get_all_users():
    res = esc_jira.get_all_users()
    jprint(res)
    time.sleep(1)


if __name__ == "__main__":
    from pyatlassian.tests import run_cov_test

    run_cov_test(
        __file__,
        "pyatlassian.atlassian_jira.users",
        preview=False,
    )
