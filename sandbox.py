results = [60, 50, 60, 58, 54, 54,
          58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51,
          69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18,
          41, 51, 55, 61, 51, 44]

costs = [.25, .27, .25, .25, .25, .25,
         .33, .31, .24, .29, .22, .22,
         .25, .25, .28, .33, .21, .25,
         .25, .25, .25, .28, .24, .22,
         .20, .25, .30, .25, .24, .25,
         .25, .25, .27, .26, .26, .29]

najwyzszy_wynik = 0 
lenght = len(results)
for i in range(lenght):
    print('wynik ' + str(i), ' to', results[i])
    if results[i] > results[i]:
        najwyzszy_wynik = results[i]
    print('liczba testow', lenght)
    print('najwyzszy wynik', najwyzszy_wynik)

    najepsze_roztwory = []
    for i in range(lenght):
        if najwyzszy_wynik == results[i]:
           najepsze_roztwory.append(i)
    print('najlepsze wyniki:', najepsze_roztwory)

koszt = 100.0
najbardziej_oplacalny = 0 
for i in range(lenght):
    if results[i] == najwyzszy_wynik and costs[i] < koszt:
        najbardziej_oplacalny = i
        koszt = costs[i] 
print('roztwor o najwyzszym wyniku i najnizszych kosztach:', najbardziej_oplacalny,
       'kosztuje:', costs[najbardziej_oplacalny])
