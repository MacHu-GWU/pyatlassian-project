# -*- coding: utf-8 -*-

from pyatlassian.atlassian_jira import api


def test():
    _ = api
    _ = api.Jira


if __name__ == "__main__":
    from pyatlassian.tests import run_cov_test

    run_cov_test(
        __file__,
        "pyatlassian.atlassian_jira.api",
        preview=False,
    )
