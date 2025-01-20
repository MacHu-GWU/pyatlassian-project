# -*- coding: utf-8 -*-

"""

"""

import typing as T


def _paginate(
    method: T.Callable,
    list_key: str,
    get_next_token: T.Callable,
    set_next_token: T.Callable,
    kwargs: T.Optional[dict[str, T.Any]] = None,
    max_results: T.Optional[int] = None,
) -> dict[str, T.Any]:
    """
    Convert a single API call into a generator that handles pagination.

    :param method: the original method to call
    :param list_key: the key in the response that contains the list of items
    :param get_next_token: a function to get the next token from the response
    :param set_next_token: a function to set the next token in the kwargs
    :param kwargs: original kwargs to pass to the method
    :param max_results: total max results to return
    """
    n = 0
    if kwargs is None:
        kwargs = {}

    while 1:
        res = method(**kwargs)
        n += len(res.get(list_key, []))
        yield res

        if n >= max_results:
            break

        next_token = get_next_token(res)
        if next_token is None:
            break
        else:
            set_next_token(kwargs, next_token)
