for i in range(0,4):
    for j in range(0,4):
        print (i * j)

for wyraz in ['aa', 'bbb', 'cccc', 'dddd', 'eeeee']:
    for i in range(2,7):
        litery = len(wyraz)
        if (litery % i) == 0:
            print(i, wyraz)

pelny = False

datki =[]
limit = 45

zabawki = ['robor', 'lalka', 'piłka', 'puzzle']

while not pelny:
    for zabawka in zabawki:
        datki.append(zabawka)
        ilosc = len(datki)
        if (ilosc >= limit):
            pelny = True
print('w koszyku znajduje się', len(datki), 'zabawek')
print(datki)