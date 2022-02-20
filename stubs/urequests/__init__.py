from typing import Any


class Request:
    ...


class Response:
    status_code: int
    reason: str
    headers: dict[str, str]

    def __init__(self, f) -> None:
        ...

    def close(self) -> None:
        ...

    @property
    def content(self) -> bytes:
        ...

    @property
    def text(self) -> str:
        ...

    def json(self) -> Any:
        ...


def request(
    method: str,
    url: str,
    data=None,
    json=None,
    headers={},
    auth=None,
    stream=None,
    parse_headers=True,
) -> Response:
    ...


def head(url: str, **kw) -> Response:
    ...


def get(url: str, **kw) -> Response:
    ...


def post(url: str, **kw) -> Response:
    ...


def put(url: str, **kw) -> Response:
    ...


def patch(url: str, **kw) -> Response:
    ...


def delete(url: str, **kw) -> Response:
    ...
