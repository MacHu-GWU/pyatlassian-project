# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from pyatlassian.tests import run_cov_test

    run_cov_test(
        __file__,
        "pyatlassian.atlassian_confluence",
        is_folder=True,
        preview=False,
    )
