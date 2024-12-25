# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from claude_projects.tests import run_cov_test

    run_cov_test(
        __file__,
        "claude_projects.vendor.atlassian_confluence",
        is_folder=True,
        preview=False,
    )
