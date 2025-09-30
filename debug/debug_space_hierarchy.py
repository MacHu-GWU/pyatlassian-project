# -*- coding: utf-8 -*-

import diskcache
from pyatlassian.atlassian.model import T_RESPONSE
from pyatlassian.paths import dir_project_root
from pyatlassian.tests.api_keys import esc_conf
from rich import print as rprint


dir_cache = dir_project_root / ".cache"
cache = diskcache.Cache(dir_cache)
space_id = 65697 # BD
# res_list = list()
# for i, res in enumerate(esc_conf.pagi_get_pages_in_space(id=space_id), start=1):
#     res_list.append(res)
# res = list(esc_conf.pagi_get_pages_in_space(id=space_id))[0]
# cache.set("BD", res_list)
# res_list = cache.get("BD")
#
id_to_page_data: dict[str, T_RESPONSE] = dict()
for res in res_list:
    for page_data in res["results"]:
        id = page_data["id"]
        id_to_page_data[id] = page_data

mapping = dict(id_to_page_data)

for ith_round in range(1, 1+10):
    print(f"=== {ith_round = }, {len(id_to_page_data) = }, {len(mapping) = }")
    if len(id_to_page_data) == 0:
        break
    else:
        for id, page_data in list(id_to_page_data.items()):
            title = page_data["title"]
            # print(f"--- {id = }, {title = !r}")
            parentId = page_data["parentId"]
            if parentId is None:
                path = id
                page_data["path"] = path
                id_to_page_data.pop(id)
            else:
                if parentId in mapping:
                    parent_page_data = mapping[parentId]
                    if "path" in parent_page_data:
                        parent_path = parent_page_data["path"]
                        path = f"{parent_path}/{id}"
                        page_data["path"] = path
                        id_to_page_data.pop(id)
                    else:
                        pass
                else:
                    id_to_page_data.pop(id)
                    mapping.pop(id)

mapping = dict(
    sorted(
        mapping.items(),
        key=lambda x: x[1]["path"],
    )
)
for id, page_data in mapping.items():
    rprint(page_data)
    title = page_data["title"]
    path = page_data["path"]
    position = page_data["position"]
    print(f"--- {path = }, {title = !r}, {position = }")
    rprint(page_data)


for res in esc_conf.pagi_get_pages(space_id=space_id, body_format="atlas_doc_format"):
    for page_data in res["results"]:
        rprint(page_data)
        break