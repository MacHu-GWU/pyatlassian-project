# -*- coding: utf-8 -*-

import time

from pyatlassian.tests import jprint
from pyatlassian.tests.api_keys import esc_jira


def test_get_issue():
    res = esc_jira.get_issue(
        issue_id_or_key="PYATLASUT-2",
    )
    jprint(res)
    time.sleep(1)


if __name__ == "__main__":
    from pyatlassian.tests import run_cov_test

    run_cov_test(
        __file__,
        "pyatlassian.atlassian_jira.issues",
        preview=False,
    )
