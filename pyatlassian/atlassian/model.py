# -*- coding: utf-8 -*-

import typing as T
import json
import dataclasses
from functools import cached_property

import requests
from requests.auth import HTTPBasicAuth

from .exc import ParamError
from .arg import REQ, _REQUIRED, NA, rm_na, T_KWARGS

T_RESPONSE = T.Dict[str, T.Any]


@dataclasses.dataclass
class BaseModel:
    def _validate(self):
        for field in dataclasses.fields(self.__class__):
            if field.init:
                k = field.name
                if getattr(self, k) is REQ:  # pragma: no cover
                    raise ParamError(f"Field {k!r} is required for {self.__class__}.")

    def __post_init__(self):
        self._validate()

    @classmethod
    def _split_req_opt(cls, kwargs: T_KWARGS) -> T.Tuple[T_KWARGS, T_KWARGS]:
        req_kwargs, opt_kwargs = dict(), dict()
        for field in dataclasses.fields(cls):
            if isinstance(field.default, _REQUIRED):
                try:
                    req_kwargs[field.name] = kwargs[field.name]
                except KeyError:
                    raise ParamError(
                        f"{field.name!r} is a required parameter for {cls}!"
                    )
            else:
                try:
                    opt_kwargs[field.name] = kwargs[field.name]
                except KeyError:
                    pass
        opt_kwargs = rm_na(**opt_kwargs)
        return req_kwargs, opt_kwargs


def _get_site_url(url: str) -> str:
    """
    Convert any of these url to https://mycompany.atlassian.net

    - https://mycompany.atlassian.net/wiki/spaces/SPACEKEY/...
    - https://mycompany.atlassian.net/jira/core/projects/PROJECTKEY/board/...
    """
    parts = url.split("/")
    return "/".join(parts[:3])


@dataclasses.dataclass
class Atlassian(BaseModel):
    url: str = dataclasses.field(default=REQ)
    username: str = dataclasses.field(default=REQ)
    password: str = dataclasses.field(default=NA)

    def __post_init__(self):
        self.url = _get_site_url(self.url)

    @property
    def headers(self) -> T.Dict[str, T.Any]:
        return {"Content-Type": "application/json"}

    @cached_property
    def http_basic_auth(self) -> "HTTPBasicAuth":
        return HTTPBasicAuth(username=self.username, password=self.password)

    def request(
        self,
        method: str,  # GET, POST, PUT, DELETE
        url: str,
        params: T.Optional[T.Dict[str, T.Any]] = None,
    ) -> "requests.Response":
        """
        Make HTTP request and get response.
        """
        return requests.request(
            method=method,
            url=url,
            headers=self.headers,
            params=params,
            auth=self.http_basic_auth,
        )

    def make_request(
        self,
        method: str,
        url: str,
        params: T.Optional[T.Dict[str, T.Any]] = None,
    ) -> T_RESPONSE:
        """
        Wrap the response object with better error handling.
        """
        # print(f"{method = }") # for debug only
        # print(f"{url = }") # for debug only
        # print(f"{params = }") # for debug only
        res = self.request(
            method=method,
            url=url,
            params=params,
        )
        res.raise_for_status()
        return json.loads(res.text)
