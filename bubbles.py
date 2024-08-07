results = [60, 50, 60, 58, 54, 54,
          58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51,
          69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18,
          41, 51, 55, 61, 51, 44]

#Added new list with random costs 

costs = [.25, .27, .25, .25, .25, .25,
         .33, .31, .24, .29, .22, .22,
         .25, .25, .28, .33, .21, .25,
         .25, .25, .25, .28, .24, .22,
         .20, .25, .30, .25, .24, .25,
         .25, .25, .27, .26, .26, .29]

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

#created new variable to saving production costs.

cost = 100.0
most_cost_effective = 0
for i in range(length):
    if results[i] == top_result and costs[i] < cost:
        most_cost_effective = 1
        cost = costs [i]

print('Sample with the highest score and the highest production costs have number',
      most_cost_effective, 'and cost', costs[most_cost_effective]) 
