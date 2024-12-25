# -*- coding: utf-8 -*-

from pyatlassian import api


def test():
    _ = api


if __name__ == "__main__":
    from pyatlassian.tests import run_cov_test

    run_cov_test(__file__, "pyatlassian.api", preview=False)
