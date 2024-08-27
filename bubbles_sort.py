#Using sorting for the 5 best samples (creating pseudo code)

#creating

def samples_sorting(results, items):
    change = True
    while change:
        change = False
        for i in range(0, len(items)-1):
            if results[i] < items[i + 1]:
                temporary = items[i]
                results[i] = results[i + 1]
                results[i + 1] = temporary
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

samples_sorting(results, items)
print(results, items)


#generating raport with the best 5 samples

number_of_results = len(results)
numbers_of_samples = list(range(number_of_results))

samples_sorting(results, numbers_of_samples)
