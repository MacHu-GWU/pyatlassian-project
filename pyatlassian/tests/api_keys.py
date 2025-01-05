# -*- coding: utf-8 -*-

from pathlib import Path

from pyatlassian.atlassian_confluence.api import Confluence
from pyatlassian.atlassian_jira.api import Jira

dir_home = Path.home()

path = dir_home.joinpath(".atlassian", "sanhehu", "sanhe-dev.txt")
api_token = path.read_text().strip()
url = "https://sanhehu.atlassian.net"
username = "husanhe@gmail.com"
sh_conf = Confluence(url=url, username=username, password=api_token)
sh_jira = Jira(url=url, username=username, password=api_token)

path = dir_home.joinpath(".atlassian", "easyscalecloud", "sanhe-dev.txt")
api_token = path.read_text().strip()
url = "https://easyscalecloud.atlassian.net"
username = "sanhehu@easyscalecloud.com"
esc_conf = Confluence(url=url, username=username, password=api_token)
esc_jira = Jira(url=url, username=username, password=api_token)
