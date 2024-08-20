#Using sorting for the 5 best samples (creating pseudo code)
def samples_sorting(items):
    change = True
    while change:
        change = False
        for i in range(0, len(items) - 1):
            if items[i] > items[i + 1]:
                temporary = items[i]
                items[i] = items[i + 1]
                items[i + 1] = temporary
                change = True

results = [60, 50, 60, 58, 54, 54,
           58, 50, 52, 54, 48, 69,
           34, 55, 51, 52, 44, 51,
           69, 64, 66, 55, 52, 61,
           46, 31, 57, 52, 44, 18,
           41, 51, 55, 61, 51, 44]

samples_sorting(results)
print(results)

coctails = ['coconut', 'strawberry', 'banana', 'pineapple']
samples_sorting(coctails)
print(coctails)
