def make_icecream_cup(icecream= 'wanilla', icing= 'chocolate', pinats=True,
                      banana=True, cookies=True, whipped_cream=True):
    receipe = 'icecream' + icecream + 'icing' + icing + ''
    if pinats:
        receipe = receipe + 'with pinats'
    if banana:
        receipe = receipe + 'banana'
    if cookies:
        receipe = receipe + 'cookies'
    if whipped_cream:
        receipe = receipe + 'whipped cream'
    else:
        receipe = receipe + 'without whipped cream'
    return receipe

cup = make_icecream_cup()
print('You ordered:', cup)

cup = make_icecream_cup('chocolate')
print('You ordered:', cup)

cup = make_icecream_cup(icing='carmel', whipped_cream= False, banana=False)
print('You ordered:', cup)

cup = make_icecream_cup(whipped_cream=False, banana=True, cookies=True, icecream='pinats')
print('You ordered:', cup)