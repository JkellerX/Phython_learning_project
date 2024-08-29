import ch1text

def policz_zdania(tekst):
    liczba = 0
    for znak in tekst:
        if znak in '.?!':
            liczba = liczba + 1
    return liczba

def oblicz_czytelnosc(tekst):
    liczba_slow = 0
    liczba_zdan = 0
    liczba_sylab = 0
    wynik = 0 

    slowa = tekst.split()
    liczba_slow = len(slowa)
    liczba_zdan = policz_zdania(tekst)
    
    print(liczba_slow, 'słow')
    print(liczba_zdan, 'zdan')

oblicz_czytelnosc(ch1text.tekst)