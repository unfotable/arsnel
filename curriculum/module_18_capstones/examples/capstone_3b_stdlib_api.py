"""Capstone 3b: the same API using only the standard library (runs anywhere)."""

import json
import re
import threading
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

BOOKS: dict[int, dict[str, object]] = {}
BOOK_PATH = re.compile(r"^/books/(\d+)$")


class Handler(BaseHTTPRequestHandler):
    def _send(self, status: int, payload: object) -> None:
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path == "/books":
            self._send(200, list(BOOKS.values()))
        elif match := BOOK_PATH.match(self.path):
            book = BOOKS.get(int(match.group(1)))
            self._send(200, book) if book else self._send(404, {"detail": "not found"})
        else:
            self._send(404, {"detail": "no such route"})

    def do_POST(self) -> None:
        length = int(self.headers.get("Content-Length", 0))
        data = json.loads(self.rfile.read(length))
        if not data.get("title"):
            self._send(422, {"detail": "title required"})
            return
        book = {"id": len(BOOKS) + 1, "title": data["title"]}
        BOOKS[int(str(book["id"]))] = book
        self._send(201, book)

    def log_message(self, format: str, *args: object) -> None:
        """Keep the demo output clean."""


def call(
    base: str, path: str, payload: dict[str, object] | None = None
) -> tuple[int, object]:
    data = json.dumps(payload).encode() if payload is not None else None
    request = urllib.request.Request(
        base + path, data=data, method="POST" if data else "GET"
    )
    try:
        with urllib.request.urlopen(request) as response:
            return response.status, json.load(response)
    except urllib.error.HTTPError as error:
        return error.code, json.load(error)


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{server.server_address[1]}"
    print(call(base, "/books", {"title": "Fluent Python"}))
    print(call(base, "/books/1"))
    print(call(base, "/books/9"))
    print(call(base, "/books", {"title": ""}))
    print(call(base, "/books"))
    server.shutdown()
    server.server_close()
