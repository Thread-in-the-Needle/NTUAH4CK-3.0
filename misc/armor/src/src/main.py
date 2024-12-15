import base64

def second(inp:str) -> str:
    part = '_7h15_4rm0r'
    return inp == part
    
    
    
def third(inp:str) -> str:
    return inp == '_3v3n_m4d3'
    
def fourth(inp:str) -> str:
    return [i for i in base64.b64encode(inp.encode())] == [88, 122, 66, 109, 88, 122, 56, 47, 80, 49, 57, 101, 88, 49, 57, 102, 88, 49, 57, 101, 102, 81, 61, 61]
    # [i for i in base64.b64encode('_0f_???_^_____^}'.encode())]
    

    
msg='Hello Admin, please verify your identity\nYou need to enter the password in 4 parts\n'
print(msg)

first = 'NH4CK{wh47_15'
def check():
    inp= input('Enter the first part: ')
    if inp == first:
        print('\tCorrect')
    else:
        print('\tBye')
        return
        
    if second(input('Enter the second part: ')):
        print('\tCorrect')
    else:
        print('\tHmm, not quite')
        return
        
    if third(input('Enter the third part: ')):
        print('\tCorrect')
    else:
        print('\tNo😠')
        return
        
    if fourth(input('Enter the fourth part: ')):
        print('\tCorrect')
    else:
        print('\tHey😲😲, you almost tricked me wth')
        return
    return True
if check():    
    print('\nWelcome Admin😍😍😍')
