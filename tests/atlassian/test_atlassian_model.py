# -*- coding: utf-8 -*-

from pyatlassian.atlassian.model import _get_site_url, Atlassian


def test_get_site_url():
    expect = "https://mycompany.atlassian.net"

    url = "https://mycompany.atlassian.net/wiki/spaces/SPACEKEY/..."
    assert _get_site_url(url) == expect

    url = "https://mycompany.atlassian.net/jira/core/projects/PROJECTKEY/board/..."
    assert _get_site_url(url) == expect


class TestAtlassian:
    pass


if __name__ == "__main__":
    from pyatlassian.tests import run_cov_test

    run_cov_test(
        __file__,
        "pyatlassian.atlassian.model",
        preview=False,
    )
