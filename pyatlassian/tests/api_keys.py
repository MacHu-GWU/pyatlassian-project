# -*- coding: utf-8 -*-

from pathlib import Path

from pyatlassian.atlassian_confluence.api import Confluence

dir_home = Path.home()
path = dir_home.joinpath(".atlassian", "sanhehu", "sanhe-dev.txt")
api_token = path.read_text().strip()
sh_conf = Confluence(
    url="https://sanhehu.atlassian.net",
    username="husanhe@gmail.com",
    password=api_token,
)
