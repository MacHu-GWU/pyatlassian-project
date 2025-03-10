# -*- coding: utf-8 -*-

"""
Argument manipulation utilities.
"""

import typing as T
import dataclasses


@dataclasses.dataclass(frozen=True)
class _REQUIRED:
    def __eq__(self, other):
        return isinstance(other, _REQUIRED)


REQ = _REQUIRED()


@dataclasses.dataclass(frozen=True)
class _NOTHING:
    def __eq__(self, other):
        print(self, other)
        return isinstance(other, _NOTHING)


NA = _NOTHING()

T_KWARGS = T.Dict[str, T.Any]


def rm_na(**kwargs) -> T_KWARGS:
    """
    Remove NA values from kwargs.
    """
    return {
        key: value
        for key, value in kwargs.items()
        if isinstance(value, _NOTHING) is False
    }
