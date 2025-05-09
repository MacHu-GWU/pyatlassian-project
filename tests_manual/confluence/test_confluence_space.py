# -*- coding: utf-8 -*-

import time

from pyatlassian.tests import jprint, debug_space_data
from pyatlassian.tests.api_keys import sh_conf, esc_conf


def test_get_spaces():
    # res = sh_conf.get_spaces()
    res = esc_conf.get_spaces()
    jprint(res)
    print("Total Spaces: ", len(res["results"]))
    for space_data in res.get("results", []):
        debug_space_data(space_data)
    time.sleep(1)


if __name__ == "__main__":
    from pyatlassian.tests import run_cov_test

    run_cov_test(
        __file__,
        "pyatlassian.atlassian_confluence.space",
        preview=False,
    )
