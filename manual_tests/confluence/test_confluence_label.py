# -*- coding: utf-8 -*-

import time

from pyatlassian.tests import jprint, debug_label_data
from pyatlassian.tests.api_keys import sh_conf, esc_conf


def test_get_labels():
    # res = sh_conf.get_labels()
    res = esc_conf.get_labels()
    jprint(res)
    print("Total Labels: ", len(res["results"]))
    for label_data in res.get("results", []):
        debug_label_data(label_data)
    time.sleep(1)


if __name__ == "__main__":
    from pyatlassian.tests import run_cov_test

    run_cov_test(
        __file__,
        "pyatlassian.atlassian_confluence.label",
        preview=False,
    )
