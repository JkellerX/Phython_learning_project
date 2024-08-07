results = [60, 50, 60, 58, 54, 54,
          58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51,
          69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18,
          41, 51, 55, 61, 51, 44]
top_result = 0 

length = len(results)
for i in range(length):
    print('sample_result #' + str(i), 'is', results[i])
    if results[i] > top_result:
        top_result = results[i] 

print('number of samples', length)
print('top_result:', top_result)

the_best_samples = []
for i in range(length):
    if top_result == results[i]:
        the_best_samples.append(i)

print('Samples with the highest score:', the_best_samples)