"""unittest.mock: replace collaborators so tests are fast and deterministic."""

import json
from unittest.mock import MagicMock, Mock, patch


def fetch_title(client: Mock, url: str) -> str:
    """Production code that uses a collaborator we do not want to call for real."""
    response = client.get(url)
    return str(json.loads(response)["title"])


client = Mock()
client.get.return_value = '{"title": "ARSNEL"}'
print(fetch_title(client, "http://x"))
client.get.assert_called_once_with("http://x")
print(client.get.call_count, client.get.call_args)

# side_effect can raise or return a sequence.
flaky = Mock(side_effect=[ConnectionError("down"), "ok"])
for _attempt in range(2):
    try:
        print(flaky())
    except ConnectionError as exc:
        print("error:", exc)

# patch swaps an attribute for the duration of a block.
with patch("os.getcwd", return_value="/pretend") as fake:
    import os

    print(os.getcwd(), fake.called)
print(os.getcwd() != "/pretend")

magic = MagicMock()
magic.__len__.return_value = 3
print(len(magic))
