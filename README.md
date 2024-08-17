<div align="center">
  <h2>PyBridge</h2>
  <h3>A lightweight library that auto-generates API clients from OpenAPI schemas.</h3>
  <a href="https://github.com/sinantan/pybridge/stargazers"><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/sinantan/pybridge"></a>
  <a href="https://github.com/sinantan/pybridge/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/sinantan/pybridge"></a>
  <a href="https://github.com/sinantan/pybridge/blob/main/LICENSE"><img alt="GitHub" src="https://img.shields.io/github/license/sinantan/pybridge"></a>
</div>



# pybridge

## Installation

You can easily install it via pip:

```bash
pip install pybridge
```

## Usage

```python

from pybridgeclient import PyBridge
base_url = "https://example.api.com/"
headers = {
    "Authorization": "Bearer xxxxxxxx"}
py_bridge = PyBridge(base_url, headers)
# item_detail is endpoint that is generated from OpenAPI schema
item_detail = py_bridge.item_detail(item_id=1)

```

## Contribution and Feedback

For any contributions and feedback, please visit my GitHub page or reach me via email.