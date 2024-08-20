def drink_me(param):
    info = 'This is ' + param + ' glass'
    print(info)
    param = 'empty'
    print('glass is', param)

glass = 'full'
drink_me(glass)