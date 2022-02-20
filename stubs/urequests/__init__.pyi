"""
URequests HTTP Library
~~~~~~~~~~~~~~~~~~~~~
`urequests` implements a subset of API of the popular 3rd-party package `requests`

Basic GET usage:
   >>> import urequests
   >>> r = urequests.get('https://www.python.org')
   >>> r.status_code
   200
   >>> b'Python is a programming language' in r.content
   True
... or POST:
   >>> payload = dict(key1='value1', key2='value2')
   >>> r = urequests.post('https://httpbin.org/post', data=payload)
   >>> print(r.text)
   {
     ...
     "form": {
       "key1": "value1",
       "key2": "value2"
     },
     ...
   }
"""

from typing import Any, Text, Optional

class Request: ...

class Response:
    """The :class:`Response <Response>` object, which contains a
    server's response to an HTTP request.
    """

    status_code: int

    #: Textual reason of responded HTTP Status, e.g. "Not Found" or "OK".
    reason: Optional[str] = None

    #: Case-insensitive Dictionary of Response Headers.
    #: For example, ``headers['content-encoding']`` will return the
    #: value of a ``'Content-Encoding'`` response header.
    headers: dict[str, str]
    def __init__(self, f) -> None: ...
    def close(self):
        """Releases the connection. Once this method has been
        called the underlying ``raw`` object must not be accessed again.

        *Note: Should not normally need to be called explicitly.*
        """
    @property
    def content(self) -> bytes:
        """Content of the response, in bytes."""
    @property
    def text(self) -> str:
        """Content of the response, in unicode."""
    def json(self):
        """Returns the json-encoded content of a response, if any."""

def request(
    method: Text,
    url: Text,
    data: Any | None = ...,
    json: Any | None = ...,
    headers: dict[str, str] = ...,
    auth: Any | None = ...,
    stream: Any | None = ...,
    parse_headers: bool = True,
) -> Response:
    """Constructs and sends a :class:`Request <Request>`.

    Usage::
       >>> import urequests
       >>> req = urequests.request('GET', 'https://httpbin.org/get')
    """

def head(
    url: Text,
    data: Any | None = ...,
    json: Any | None = ...,
    headers: Any | None = ...,
    auth: Any | None = ...,
    stream: Any | None = ...,
    parse_headers: bool = True,
) -> Response:
    """Sends a HEAD request."""

def get(
    url: Text,
    data: Any | None = ...,
    json: Any | None = ...,
    headers: Any | None = ...,
    auth: Any | None = ...,
    stream: Any | None = ...,
    parse_headers: bool = True,
) -> Response:
    """Sends a GET request."""

def post(
    url: Text,
    data: Any | None = ...,
    json: Any | None = ...,
    headers: Any | None = ...,
    auth: Any | None = ...,
    stream: Any | None = ...,
    parse_headers: bool = True,
) -> Response:
    """Sends a POST request."""

def put(
    url: Text,
    data: Any | None = ...,
    json: Any | None = ...,
    headers: Any | None = ...,
    auth: Any | None = ...,
    stream: Any | None = ...,
    parse_headers: bool = True,
) -> Response:
    """Sends a PUT request."""

def patch(
    url: Text,
    data: Any | None = ...,
    json: Any | None = ...,
    headers: Any | None = ...,
    auth: Any | None = ...,
    stream: Any | None = ...,
    parse_headers: bool = True,
) -> Response:
    """Sends a PUT request."""

def delete(
    url: Text,
    data: Any | None = ...,
    json: Any | None = ...,
    headers: Any | None = ...,
    auth: Any | None = ...,
    stream: Any | None = ...,
    parse_headers: bool = True,
) -> Response:
    """Sends a DELETE request."""
