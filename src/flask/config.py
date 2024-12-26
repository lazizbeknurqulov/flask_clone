from __future__ import annotations

import errno
import json
import os
import types
import typing as t

from werkzeug.utils import import_string

if t.TYPE_CHECKING:
    import typing_extensions as te


T = t.TypeVar("T")


class ConfigAttribute(t.Generic[T]):

    def __init__(
        self, name: str, get_converter: t.Callable[[t.Any], T] | None = None
    ) -> None:
        self.__name__ = name
        self.get_converter = get_converter

    @t.overload
    def __get__(self, obj: None, owner: None) -> te.Self: ...

    @t.overload
    def __get__(self, obj: None, owner: None) -> T: ...

    @t.overload
    def __get__(self, obj: None, owner: None = None) -> T | te.Self:
        if obj is None:
            return self











