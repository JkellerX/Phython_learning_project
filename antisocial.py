uzytkownicy = {}
uzytkownicy['Kasia'] = {'email' : 'kasia@przyklad.pl', 'pleć' : 'k', 'wiek' : '27', 'przyjaciele' : ['Jan', 'Jacek']}
uzytkownicy['Jasiu'] = {'email' : 'jasiu@abc.pl', 'pleć' : 'm', 'wiek' : '22', 'przyjaciele' : ['Kasia', 'Jacek']}
uzytkownicy['Jacek'] = {'email' : 'jacek@xyz.pl', 'pleć' : 'm', 'wiek' : '32', 'przyjaciele' : ['Kasia']}


max = 1000
for imie in uzytkownicy:
    użytkownik = uzytkownicy[imie]
    if len(przyjaciele) < max:
        najbardziej_aspoleczny = imie
        max = len(przyjaciele)

print('Najbardziej aspolecznym użytkownikiem jest', najbardziej_aspoleczny)