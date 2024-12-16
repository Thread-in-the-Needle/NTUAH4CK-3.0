# Overview

- The admin bot is using an http proxy as follows:
```python
def request(flow: http.HTTPFlow) -> None:
    if not flow.request.pretty_host.startswith("127.0.0.1"):
        flow.response = http.Response.make(
            403,  # (optional) status code
            b"Access Denied",  # (optional) content
            {"Content-Type": "text/html"}  # (optional) headers
        )
```

# Solution (was unintended 😛)
- Use `https://requestrepo.com/` and create a DNS record for `127.0.0.1.xxx.xxx`.
- The admin bot will make requests to that domain and you can intercept them, stealing the cookie just like `Lazy Admin` challenge.