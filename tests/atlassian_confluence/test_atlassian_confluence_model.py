# -*- coding: utf-8 -*-

from pyatlassian.atlassian_confluence.model import Confluence


class TestConfluence:
    def test(self):
        _ = Confluence


if __name__ == "__main__":
    from pyatlassian.tests import run_cov_test

    run_cov_test(
        __file__,
        "pyatlassian.atlassian_confluence.model",
        preview=False,
    )
