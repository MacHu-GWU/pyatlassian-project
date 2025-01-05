# -*- coding: utf-8 -*-

import json
import time
import textwrap
from rich import print as rprint
from pyatlassian.tests.api_keys import esc_jira as jira


def _test_get_projects():
    res = jira.get_projects(max_results=1)
    # rprint(res)
    for proj_data in res.get("values", []):
        proj_id = proj_data["id"]
        proj_key = proj_data["key"]
        proj_name = proj_data["name"]
        proj_type = proj_data["projectTypeKey"]
        print(f"{proj_id = }, {proj_key = }, {proj_name = }, {proj_type = }")
    time.sleep(1)


def _test_search_for_issues_using_jql_enhanced_search():
    jql = textwrap.dedent(
        """
        project = ESCPORTAL
        """
    )
    res = jira.search_for_issues_using_jql_enhanced_search(
        jql=jql,
        fields="*all",
    )
    print(json.dumps(res, ensure_ascii=False))
    for issue_data in res["issues"]:
        issue_id = issue_data["id"]
        issue_key = issue_data["key"]
        issue_summary = issue_data["fields"]["summary"]
        issue_description = issue_data["fields"]["description"]
        print(f"{issue_id = }, {issue_key = }, {issue_summary = }")
        print(json.dumps(issue_description, ensure_ascii=False, indent=4))
    time.sleep(1)


def test():
    print("")
    # _test_get_projects()
    # _test_get_all_status_for_project()
    _test_search_for_issues_using_jql_enhanced_search()


if __name__ == "__main__":
    from pyatlassian.tests import run_unit_test

    run_unit_test(__file__)
