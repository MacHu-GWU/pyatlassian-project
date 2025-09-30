# -*- coding: utf-8 -*-

import dataclasses
from functools import cached_property
from home_secret.api import hs


@dataclasses.dataclass
class Config:
    site_url: str = dataclasses.field()
    email: str = dataclasses.field()
    api_token: str = dataclasses.field()

    @classmethod
    def new_sh(cls):
        prefix_sh = "providers.atlassian.accounts.sh"
        return cls(
            site_url=hs.v(f"{prefix_sh}.site_url"),
            email=hs.v(f"{prefix_sh}.users.sh.email"),
            api_token=hs.v(f"{prefix_sh}.users.sh.secrets.sync_page.value"),
        )

    @classmethod
    def new_sh_esc(cls):
        prefix_sh = "providers.atlassian.accounts.sh_esc"
        return cls(
            site_url=hs.v(f"{prefix_sh}.site_url"),
            email=hs.v(f"{prefix_sh}.users.sh_esc.email"),
            api_token=hs.v(f"{prefix_sh}.users.sh_esc.secrets.sync_page.value"),
        )

    @classmethod
    def new(cls):
        return cls.new_sh()

    @cached_property
    def client(self):
        pass
