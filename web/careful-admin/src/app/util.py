from json import loads,dump
items =loads(open('items.json').read())
from datetime import datetime
from random import choice
open('prev_searches.json','w').write('[]')



def search(queries:list[str]) -> list[str]:
    res=[]
    for q in queries:
        valid=[i for i in items if q in items[i]]
        if valid:
            res.append(choice(valid))
        else:
            res.append("nop.jpg")
    match=[i for i in items if all(q in items[i] for q in queries)]
    if match:
        res.append(choice(match))
    else:
        res.append("nop.jpg")
    return res
    
# prev_searches functions
    
def get_prev_searches() ->list:    
    def clear_old(prev_searches:list,dt=15):
        t=datetime.now().timestamp()
        return [i for i in prev_searches if t-i[1]<dt]
        
    try:
        with open('prev_searches.json','r') as f:
            prev_searches=loads(f.read())
    except:
        prev_searches=[]
    prev_searches=clear_old(prev_searches)
    save_prev_searches(prev_searches)
    return prev_searches

def save_prev_searches(prev_searches:list):
    with open('prev_searches.json','w') as f:
        dump(prev_searches,f)

def add(res:list[str]):
    prev_searches=get_prev_searches()
    t=datetime.now()
    prev_searches.append([res,int(t.timestamp()),t.strftime('%H:%M:%S')])
    save_prev_searches(prev_searches)
    

    