# -*- coding: utf-8 -*-

from pyatlassian.atlassian_jira.utils import *


def test():
    pass


if __name__ == "__main__":
    from pyatlassian.tests import run_cov_test

    run_cov_test(
        __file__,
        "pyatlassian.atlassian_jira.utils",
        preview=False,
    )
