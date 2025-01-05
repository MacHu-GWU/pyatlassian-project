# -*- coding: utf-8 -*-

import typing as T


def extract_page_id_and_space_key_from_url(
    url: str,
) -> tuple[int, str]:
    """
    Extract page id (123456) and space key (ABC) from the URL like this

    - https://mycompany.atlassian.net/wiki/spaces/ABC/pages/edit-v2/123456
    - https://mycompany.atlassian.net/wiki/spaces/ABC/pages/123456/This+Document+Is+Awesome
    """
    if url.startswith("https://") or url.startswith("http://"):
        url = "/".join(url.split("/")[2:])
    parts = url.split("/")
    if len(parts) >= 7:
        if parts[2] == "spaces" and parts[4] == "pages":
            if parts[5] == "edit-v2":
                return int(parts[6]), parts[3]
            else:
                return int(parts[5]), parts[3]
        else:
            raise NotImplementedError
    else:
        raise NotImplementedError
