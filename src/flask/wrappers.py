from __future__ import annotations
import typing as t
from werkzeug.exceptions import BadRequest
from werkzeug.exceptions import HTTPException
from werkzeug.wrappers import Request as RequestBase
from werkzeug.wrappers import Response as ResponseBase

from . import json

# You can use Rule only for type checking
if t.TYPE_CHECKING:
    from werkzeug.routing import Rule


class Request(RequestBase):

    json_module = t.Any = json
    url_rule: Rule | None = None
    view_args: dict[str, t.Any] | None = None
    routing_exception: HTTPException | None = None
    _max_content_length: int | None = None
    _max_form_memory_size: int | None = None
    _max_form_parts: int | None = None

    def max_content_length(self) -> int | None:
        if self._max_content_length is not None:
            return self._max_content_length













