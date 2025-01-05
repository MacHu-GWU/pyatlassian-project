# -*- coding: utf-8 -*-

"""
Use this script to generate a prompt to let the AI implement an API method.
"""

import json
from pathlib import Path

from pyatlassian.paths import dir_project_root

api_group = """
Label
""".strip()
api_method = """
Get labels
""".strip()
api_path = """
/labels
""".strip()

p = dir_project_root.joinpath("genai", "tmp", "atlassian-confluence-openapi-spec.json")
data = json.loads(p.read_text())
spec = data["paths"][api_path]
openapi_json = {api_path: spec}

dir_here = Path(__file__).absolute().parent
path_tpl = dir_here.joinpath("implement_api_method_using_openapi_spec.md")
path_out = dir_here.joinpath("prompt.md")

md = path_tpl.read_text().format(
    API_GROUP_HERE=api_group,
    API_METHOD_HERE=api_method,
    OPENAPI_JSON_HERE=json.dumps(openapi_json, indent=4),
)
path_out.write_text(md)
