# -*- coding: utf-8 -*-

import time

from pyatlassian.tests import jprint
from pyatlassian.tests.api_keys import esc_jira


def test_search_for_issues_using_jql_enhanced_search():
    res = esc_jira.search_for_issues_using_jql_enhanced_search(
        jql="""
        project = PYATLASUT
        ORDER BY createdDate DESC
        """,
        fields=[
            # "*all",
            "summary",
            # "description",
            # "created",
            # "updated",
        ],
    )
    jprint(res)
    print(f"n_issues = ", len(res["issues"]))
    time.sleep(1)


def test_pagi_search_for_issues_using_jql_enhanced_search_1():
    for res in esc_jira.pagi_search_for_issues_using_jql_enhanced_search(
        jql="""
            project = AWD
            ORDER BY createdDate DESC
            """,
        fields=[
            "summary",
        ],
        max_results=1,
        total_max_results=3,
    ):
        jprint(res)
        print(f"n_issues = ", len(res["issues"]))
        time.sleep(1)


def test_pagi_search_for_issues_using_jql_enhanced_search_2():
    for res in esc_jira.pagi_search_for_issues_using_jql_enhanced_search(
        jql="""
            project = AWD
            ORDER BY createdDate DESC
            """,
        fields=[
            "summary",
        ],
        max_results=5,
        total_max_results=9999,
    ):
        jprint(res)
        print(f"n_issues = ", len(res["issues"]))
        time.sleep(1)


def test_pagi_search_for_issues_using_jql_enhanced_search_3():
    for res in esc_jira.pagi_search_for_issues_using_jql_enhanced_search(
        jql="""
            project = AWD
            ORDER BY createdDate DESC
            """,
        fields=[
            "summary",
        ],
        max_results=100,
        total_max_results=3,
    ):
        jprint(res)
        print(f"n_issues = ", len(res["issues"]))
        time.sleep(1)


def test_pagi_search_for_issues_using_jql_enhanced_search_4():
    for res in esc_jira.pagi_search_for_issues_using_jql_enhanced_search(
        jql="""
            project = AWD
            ORDER BY createdDate DESC
            """,
        fields=[
            "summary",
        ],
        max_results=100,
        total_max_results=9999,
    ):
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
