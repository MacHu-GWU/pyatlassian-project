# -*- coding: utf-8 -*-

import time

from pyatlassian.tests import jprint
from pyatlassian.tests.api_keys import esc_jira


def test_search_for_issues_using_jql_enhanced_search():
    # res = esc_jira.search_for_issues_using_jql_enhanced_search(
    #     jql="""
    #     project = PYATLASUT
    #     ORDER BY createdDate DESC
    #     """,
    #     fields=[
    #         # "*all",
    #         "summary",
    #         # "description",
    #         # "created",
    #         # "updated",
    #     ],
    # )
    # jprint(res)
    # print(f"n_issues = ", len(res["issues"]))
    # time.sleep(1)

    res = esc_jira.search_for_issues_using_jql_enhanced_search(
        jql="""
            project = AWD
            ORDER BY createdDate DESC
            """,
        fields=[
            # "*all",
            "summary",
            # "description",
            # "created",
            # "updated",
        ],
        paginate=True,
        max_results=3,
    )
    jprint(res)
    print(f"n_issues = ", len(res["issues"]))
    time.sleep(1)


if __name__ == "__main__":
    from pyatlassian.tests import run_cov_test

    run_cov_test(
        __file__,
        "pyatlassian.atlassian_jira.issue_search",
        preview=False,
    )
