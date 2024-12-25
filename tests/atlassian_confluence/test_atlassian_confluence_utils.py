# -*- coding: utf-8 -*-

from pyatlassian.atlassian_confluence.utils import extract_page_id_and_space_key_from_url


def test_extract_page_id_and_space_key_from_url():
    expect = (123456, "ABC")

    url = "https://mycompany.atlassian.net/wiki/spaces/ABC/pages/edit-v2/123456"
    assert expect == extract_page_id_and_space_key_from_url(url)

    url = "https://mycompany.atlassian.net/wiki/spaces/ABC/pages/123456/This+Document+Is+Awesome"
    assert expect == extract_page_id_and_space_key_from_url(url)


if __name__ == "__main__":
    from pyatlassian.tests import run_cov_test

    run_cov_test(
        __file__,
        "pyatlassian.atlassian_confluence.utils",
        preview=False,
    )
