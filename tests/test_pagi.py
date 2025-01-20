# -*- coding: utf-8 -*-

import typing as T
import itertools
from pyatlassian.pagi import _paginate


def take(n: int, iterable: T.Iterable):
    "Return first n items of the iterable as a list."
    return list(itertools.islice(iterable, n))


last_item = 10
all_items = list(range(1, 1 + last_item))
total_n_items = len(all_items)


def list_items(
    page_size: int = 3,
    next_token: T.Optional[str] = None,
    opt_kwargs: T.Optional[dict[str, T.Any]] = None,
) -> dict[str, T.Any]:
    if next_token is None:
        items = take(page_size, all_items)
        if items[-1] < last_item:
            next_token = items[-1]
            return {
                "items": items,
                "last_item": items[-1],
                "next_token": str(next_token),
            }
        else:
            return {"items": items, "last_item": items[-1]}
    else:
        next_token = int(next_token)
        items = take(page_size, all_items[next_token:])
        if items[-1] < last_item:
            next_token = items[-1]
            return {
                "items": items,
                "last_item": items[-1],
                "next_token": str(next_token),
            }
        else:
            return {"items": items, "last_item": items[-1]}


def pagi_list_items(
    page_size: int = 3,
    next_token: T.Optional[str] = None,
    opt_kwargs: T.Optional[dict[str, T.Any]] = None,
    max_results: int = 9999,
) -> T.Iterable[dict[str, T.Any]]:
    def get_next_token(res: dict[str, T.Any]) -> T.Optional[str]:
        return res.get("next_token")

    def set_next_token(kwargs: dict[str, T.Any], next_token: str):
        kwargs["next_token"] = next_token

    yield from _paginate(
        method=list_items,
        list_key="items",
        get_next_token=get_next_token,
        set_next_token=set_next_token,
        kwargs=dict(
            page_size=page_size,
            next_token=next_token,
            opt_kwargs=opt_kwargs,
        ),
        max_results=max_results,
    )


def test_list_items():
    items = list_items(page_size=3)
    print(items)
    assert items == {"items": [1, 2, 3], "last_item": 3, "next_token": "3"}

    items = list_items(page_size=3, next_token="3")
    print(items)
    assert items == {"items": [4, 5, 6], "last_item": 6, "next_token": "6"}

    items = list_items(page_size=9, next_token="9")
    print(items)
    assert items == {"items": [10], "last_item": 10}

    items = list_items(page_size=15)
    print(items)
    assert items == {"items": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "last_item": 10}

    items = list_items(page_size=1)
    print(items)
    assert items == {"items": [1], "last_item": 1, "next_token": "1"}


def test_pagi_list_items_1():
    for res in pagi_list_items(
        page_size=3,
    ):
        print(res)


def test_pagi_list_items_2():
    for res in pagi_list_items(
        page_size=3,
        max_results=5,
    ):
        print(res)


def test_pagi_list_items_3():
    for res in pagi_list_items(
        page_size=1000,
        max_results=3,
    ):
        print(res)


if __name__ == "__main__":
    from pyatlassian.tests import run_cov_test

    run_cov_test(__file__, "pyatlassian.pagi", preview=False)
