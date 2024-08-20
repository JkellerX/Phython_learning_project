#There is something wrong... 

def drink_me(param):
    info = 'This is ' + param + ' glass'
    print(info)
    param = 'empty'

    glass = 'full'
    drink_me(glass)
    print('glass is', glass)

    