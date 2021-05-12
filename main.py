# Cian Hogan GMIT Data Analytics
# COMPUTATIONAL THINKING WITH ALGORITHMS Module Project
# Main test file to be run

import pandas as pd # store results write to CSV
import time # measure performance of test
import testing_algorithms as alg # import tests and algorithms from test file


# output and CSV headings
headings = [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600]

# dict of results
results = {}

# time total test
start = time.time()

# add headings to output
results["Array Size"] = headings

# test each algorithm and add results to output
results["Bubble Sort"] = alg.algoTest(alg.bubbleSort)

results["Insertion Sort"] = alg.algoTest(alg.insertionSort)

results["Merge Sort"] = alg.algoTest(alg.mergeSort)

results["Counting Sort"] = alg.algoTest(alg.countingSort)

results["Quick Sort Random Pivot"] = alg.algoTest(alg.quickSortRandom)

results["Quick Sort Middle Pivot"] = alg.algoTest(alg.quickSortMiddle)

results["Python built in sort()"] =  alg.pythonSortTest() # built-in test


end = time.time() # finsih timing test

totalTime = end-start

# add results to dataframe
output = pd.DataFrame.from_dict(results, orient="index")

# output to CSV file
output.to_csv("results.csv")

# output to console
print(output)

# output total time taken
print("Total time take: " + str(totalTime))


	




