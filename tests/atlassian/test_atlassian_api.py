# -*- coding: utf-8 -*-

from pyatlassian.atlassian import api


def test():
    _ = api
    _ = api.ParamError
    _ = api.REQ
    _ = api.NA
    _ = api.rm_na
    _ = api.BaseModel
    _ = api.T_RESPONSE
    _ = api.T_KWARGS
    _ = api.Atlassian


if __name__ == "__main__":
    from pyatlassian.tests import run_cov_test

    run_cov_test(
        __file__,
        "pyatlassian.atlassian.api",
        preview=False,
    )
