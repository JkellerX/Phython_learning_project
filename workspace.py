#KAMIEŃ, PAPIER, NOŻYCE
# Ten kod jest implementacją wersji gry, w której przeciwnikiem jest komputer

#Tutaj przygotowujemy fundamenty pod resztę kodu,
#imporując moduł random i deklarując zmienną zwycięzca

import random

zwyciezca = ''

#Komputer losowo wybiera kamień, papier lub nożyce:
#generuje liczbę losową od 0 do 2, a nastepnie 
#przypisuje ją do odpowiedającego jej łańcucha.

liczba_losowa = random.randint(0, 2)

if liczba_losowa == 0:
    wybór_komputera = 'kamień'
elif liczba_losowa == 1:
    wybór_komputera = 'papier'
else:
    wybór_komputera = 'nożyce'

#Pobież wybór użytkownika przy użyciu prostej instrukcji. 
wybór_użytkownika = ''
while (wybór_użytkownika != 'kamień' and
       wybór_użytkownika != 'papier' and
       wybór_użytkownika != 'nożyce'):
    wybór_użytkownika = input('kamień, papier czy nożyce? ')
if wybór_komputera == wybór_użytkownika:
    zwycięzca = 'remis'
elif wybór_komputera == 'papier' and wybór_użytkownika == 'kamień':
    zwycięzca = 'komputer'
elif wybór_komputera == 'kamień' and wybór_użytkownika == 'nożyce':
    zwycięzca = 'komputer'
elif wybór_komputera == 'nożyce' and wybór_użytkownika == 'papier':
    zwycięzca = 'użytkownik'
if zwycięzca == 'remis':
    print('Obaj wybraliśmy', wybór_komputera + ' , zagraj ponownie.')
else:
    print('Wygrał', zwycięzca + '.', 'Komputer wybrał', wybór_komputera + '.')