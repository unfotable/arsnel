"""A complete HTTP round trip with only the standard library."""

import json
import threading
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        query = parse_qs(urlparse(self.path).query)
        name = query.get("name", ["world"])[0]
        self._send(200, {"message": f"hello {name}"})

    def do_POST(self) -> None:
        length = int(self.headers.get("Content-Length", 0))
        data = json.loads(self.rfile.read(length))
        self._send(201, {"received": data, "keys": sorted(data)})

    def _send(self, status: int, payload: dict[str, object]) -> None:
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: object) -> None:
        """Silence the default request logging."""


server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)  # port 0: any free port
port = server.server_address[1]
threading.Thread(target=server.serve_forever, daemon=True).start()

with urllib.request.urlopen(f"http://127.0.0.1:{port}/?name=ARSNEL") as response:
    print(response.status, json.load(response))

request = urllib.request.Request(
    f"http://127.0.0.1:{port}/",
    data=json.dumps({"b": 2, "a": 1}).encode(),
    headers={"Content-Type": "application/json"},
    method="POST",
)
with urllib.request.urlopen(request) as response:
    print(response.status, json.load(response))

server.shutdown()
server.server_close()
