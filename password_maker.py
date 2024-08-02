import random as rd
import os

def mkfile(name):
    dir = os.path.dirname(__file__)
    txt = os.path.join(dir, name)
    _, ext = os.path.splitext(txt)
    if ext == '':
        txt = os.path.join(txt + '.txt')
    return txt

def savepass(name, password):
    txt = mkfile(name)
    if type(password) == list:
        for passw in password:    
            with open(txt, 'a+') as fil:
                fil.write(passw + '\n')
    else:
        with open(txt, 'a+') as fil:
                fil.write(password + '\n')
    return txt

def loop(func, n, *arg):
    ini = 0
    n = int(n)
    if n == 1:
        password = func(*arg)
        return password
    
    password = []
    while ini < n:
        passw = func(*arg)
        password.append(passw)
        ini += 1
    return password
        
def peak(x, y):
    return chr(rd.randint(x, y))

def intertwine(resul, R2, n):
    if type(resul) == list:
        x = ''.join(resul)
    else:
        x = resul
    
    x = list(x)
    rd.shuffle(x)

    if type(resul) != list:
        while len(x) > R2:
            y = x.pop()
        password = ''.join(x)  
        return password

    password = []
    while len(password) < int(n):
        password.append('')
        for i in range(len(password)):
            while len(password[i]) < R2:
                password[i] += x[0]
                del x[0]

    return password
        
def uppercase(R2):
    password = ''
    while len(password) < R2:
        char = peak(65, 90)
        password += char
    return password

def lowercase(R2):
    password = ''
    while len(password) < R2:
        char = peak(97, 122)
        password += char
    return password

def pin(R2):
    password = ''
    while len(password) < R2:
        char = peak(48, 57)
        password += char
    return password

def symbols(R2):
    password = ''
    while len(password) < R2:
        char = peak(33, 47)
        password += char
    return password    
    
    
print('0 - Exit',
      '1 - Uppercase only',
      '2 - Lowercase only',
      '3 - Pin',
      '4 - Symbols',
      
      '5 - Uppercase & Lowercase',
      '6 - Uppercase & Numbers',
      '7 - Uppercase & Symbols',

      '8 - Lowercase & Numbers',
      '9 - Lowercase & Symbols',

      '10 - Numbers & Symbols',

      '11 - Uppercase & Lowercase & Numbers',
      '12 - Uppercase & Lowercase & Symbols',
      '13 - Uppercase & Numbers & Symbols',

      '14 - Lowercase & Numbers & Symbols',
      
      '15 - Random',

      '16 - Customized password \n'
      
      ,sep='\n')

while True:
    R1 = input('Choose an option > ')
    R1 = R1.strip()
    if not R1.isdigit() or int(R1) > 17:
        print('Error \n')
        break


    n = input('How many passwords do you want to generate > ')
    if not n.isdigit() or n == '0':
        print('Error \n') 
        break
    
    
    R2 = input('Password length (min. 6) > ')
    R2 = R2.strip()
    if R2 == '':
        R2 = 0
        
    elif not R2.isdigit():
        print('Error \n')
        break
    
    R2 = int(R2)
    while R2 < 6:
        R2 += 1


    match R1:
        case '1':
            password = loop(uppercase, n, R2)
            if type(password) == list:
                print('\nYour passwords: ')
                for psw in password:
                    print(psw)
                print(end='\n')
            else:
                print(f'\nYour password: {password} \n')

        case '2':
            password = loop(lowercase, n, R2)
            if type(password) == list:
                print('\nYour passwords: ')
                for psw in password:
                    print(psw)
                print(end='\n')
            else:
                print(f'\nYour password: {password} \n')

        case '3':
            password = loop(pin, n, R2)
            if type(password) == list:
                print('\nYour passwords: ')
                for psw in password:
                    print(psw)
                print(end='\n')
            else:
                print(f'\nYour password: {password} \n')

        case '4':
            password = loop(symbols, n, R2)
            if type(password) == list:
                print('\nYour passwords: ')
                for psw in password:
                    print(psw)
                print(end='\n')
            else:
                print(f'\nYour password: {password} \n')

        case '5':
            password = intertwine(loop(uppercase, n, R2) + loop(lowercase, n, R2), R2, n)
            if type(password) == list:
                print('\nYour passwords: ')
                for psw in password:
                    print(psw)
                print(end='\n')
            else:
                print(f'\nYour password: {password} \n')

        case '6':
            password = intertwine(loop(uppercase, n, R2) + loop(pin, n, R2), R2, n)
            if type(password) == list:
                print('\nYour passwords: ')
                for psw in password:
                    print(psw)
                print(end='\n')
            else:
                print(f'\nYour password: {password} \n')

        case '7':
            password = intertwine(loop(uppercase, n, R2) + loop(symbols, n, R2), R2, n)
            if type(password) == list:
                print('\nYour passwords: ')
                for psw in password:
                    print(psw)
                print(end='\n')
            else:
                print(f'\nYour password: {password} \n')

        case '8':
            password = intertwine(loop(lowercase, n, R2) + loop(pin, n, R2), R2, n)
            if type(password) == list:
                print('\nYour passwords: ')
                for psw in password:
                    print(psw)
                print(end='\n')
            else:
                print(f'\nYour password: {password} \n')

        case '9':
            password = intertwine(loop(lowercase, n, R2) + loop(symbols, n, R2), R2, n)
            if type(password) == list:
                print('\nYour passwords: ')
                for psw in password:
                    print(psw)
                print(end='\n')
            else:
                print(f'\nYour password: {password} \n')

        case '10':
            password = intertwine(loop(pin, n, R2) + loop(symbols, n, R2), R2, n)
            if type(password) == list:
                print('\nYour passwords: ')
                for psw in password:
                    print(psw)
                print(end='\n')
            else:
                print(f'\nYour password: {password} \n')

        case '11':
            password = intertwine(loop(uppercase, n, R2) + loop(lowercase, n, R2) + loop(pin, n, R2), R2, n)
            if type(password) == list:
                print('\nYour passwords: ')
                for psw in password:
                    print(psw)
                print(end='\n')
            else:
                print(f'\nYour password: {password} \n')

        case '12':
            password = intertwine(loop(uppercase, n, R2) + loop(lowercase, n, R2) + loop(symbols, n, R2), R2, n)
            if type(password) == list:
                print('\nYour passwords: ')
                for psw in password:
                    print(psw)
                print(end='\n')
            else:
                print(f'\nYour password: {password} \n')

        case '13':
            password = intertwine(loop(uppercase, n, R2) + loop(pin, n, R2) + loop(symbols, n, R2), R2, n)
            if type(password) == list:
                print('\nYour passwords: ')
                for psw in password:
                    print(psw)
                print(end='\n')
            else:
                print(f'\nYour password: {password} \n')

        case '14':
            password = intertwine(loop(lowercase, n, R2) + loop(pin, n, R2) + loop(symbols, n, R2), R2, n)
            if type(password) == list:
                print('\nYour passwords: ')
                for psw in password:
                    print(psw)
                print(end='\n')
            else:
                print(f'\nYour password: {password} \n')

        case '15':
            password = intertwine(loop(uppercase, n, R2) + loop(lowercase, n, R2) + loop(pin, n, R2) + loop(symbols, n, R2), R2, n)
            if type(password) == list:
                print('\nYour passwords: ')
                for psw in password:
                    print(psw)
                print(end='\n')
            else:
                print(f'\nYour password: {password} \n')

        case '16':
            prefix = input('Add a password prefix > ')
            password = intertwine(loop(pin, n, R2) + loop(symbols, n, R2), R2, n)
            if type(password) == list:
                for i in range(len(password)):
                    cusmtom = prefix + password[i]  
                    while len(cusmtom) > R2:
                        password[i] = cusmtom[:R2]
                        cusmtom = cusmtom[:R2]
                    cusmtom = ''
                print('\nYour passwords: ')
                for psw in password:
                    print(psw)
                print(end='\n')
            else:
                prefix += password  
                password = prefix[:R2]
                print(f'\nYour password: {password} \n')
        
        case _:
            break
        
    print('Do you want to save the password in a file?(y/N)')
    R3 = input('> ')
    R3 = R3.lower().strip()
    if R3 == 'yes' or R3 == "y":
        R4 = input('File\'s name > ')
        print(f'Password saved in {savepass(R4, password)}\n')
    else:
        print(end='\n')