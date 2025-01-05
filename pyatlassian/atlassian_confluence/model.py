# -*- coding: utf-8 -*-

"""
"""

import dataclasses
from functools import cached_property

from ..atlassian.api import (
    Atlassian,
    NA,
    rm_na,
    T_RESPONSE,
)

from .children import ChildrenMixin
from .label import LabelMixin
from .page import PageMixin
from .space import SpaceMixin


@dataclasses.dataclass
class Confluence(
    Atlassian,
    ChildrenMixin,
    LabelMixin,
    PageMixin,
    SpaceMixin,
):
    """
    - https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#about
    """

    @cached_property
    def _root_url(self) -> str:
        return f"{self.url}/wiki/api/v2"

    def _paginate(
        self,
        base_url: str,
        params: dict,
        paginate: bool = False,
        max_results: int = 9999,
        _url: str = None,
        _results: list[T_RESPONSE] = None,
    ) -> T_RESPONSE:
        """
        Universal pagination handler for Atlassian API endpoints.


        :param base_url: The base URL for the API endpoint
        :param params: Dictionary of query parameters
        :param paginate: If True, will auto paginate until all results are fetched
        :param max_results: Maximum number of results to return
        :param _url: Internal parameter for continuation URLs
        :param _results: Internal parameter for result accumulation
        :param kwargs: Additional parameters to pass through to recursive calls
        """
        if _url is None:
            _url = base_url
        if _results is None:
            _results = []
        if len(_results) >= max_results:
            return {"results": _results}

        # Remove None/NA values and make request
        cleaned_params = rm_na(**params)
        cleaned_params = cleaned_params if cleaned_params else None
        res = self.make_request(
            method="GET",
            url=_url,
            params=cleaned_params,
        )

        # Accumulate results
        _results.extend(res.get("results", []))

        # Handle pagination
        if "next" in res.get("_links", {}) and paginate:
            next_url = f"{self.url}{res['_links']['next']}"
            _res = self._paginate(
                base_url=base_url,
                params=params,
                paginate=True,
                max_results=max_results,
                _url=next_url,
                _results=_results,
            )
        else:
            _res = None

        # Return results
        if _res is None:
            res["results"] = _results
        else:
            res = {"results": _results}
        return res
