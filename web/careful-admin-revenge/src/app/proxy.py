from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    if not flow.request.pretty_host == "127.0.0.1":
        flow.response = http.Response.make(
            403,  # (optional) status code
            b"Access Denied",  # (optional) content
            {"Content-Type": "text/html"}  # (optional) headers
        )