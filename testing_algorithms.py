# Cian Hogan GMIT Data Analytics
# COMPUTATIONAL THINKING WITH ALGORITHMS Module Project
# Testing file imported to main file
# Contains implementations of the 5 algorithms and testing functions

import time # import to measue time
import random # import to generate random lists and pivot

# testing algorithm
def algoTest(algo):
    # Seeding random module for consistent results on multiple runs of tests
	random.seed(1234)

	output = [] # initialize output variable

	sizes = [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600] # array sizes n

    #test is run once for each size of n
	for size in sizes:
		tempOut = [] # temp variable to store results

		for i in range(10): # run test 10 times

			# https://www.techbeamers.com/python-generate-random-numbers-list/
            # generating list of random ints using list comprehension
            # list is size in length
			arr = [random.randint(0, 1000) for j in range(size)]

			start_time = time.time() # used to track time algorithm starts

			algo(arr) # performs the algorithm on the random array

			end_time = time.time() # used to track time algorithm finishes

			total_time = (end_time - start_time) # caculate run time

			tempOut.append(total_time) # add run time to temp list

		avgRes = sum(tempOut)/len(tempOut) # calculate avg run time

		# add avg run time in miliseconds to output file, 
        # rounded to 4 decimals	
		output.append(round((avgRes*1000),4)) 

	return output

# Same as test above but uses built-in list.sort() method
def pythonSortTest():

    random.seed(1234)

    output = []

    sizes = [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600]

    for size in sizes:
        tempOut = []

        for i in range(10):

            
            arr = [random.randint(0, 1000) for j in range(size)]

            start_time = time.time() 

            arr.sort() # python sort on array

            end_time = time.time()

            total_time = (end_time - start_time)

            tempOut.append(total_time)

        avgRes = sum(tempOut)/len(tempOut)
            
        output.append(round(avgRes*1000,4))

    return output

# bubbleSort
# https://www.geeksforgeeks.org/python-program-for-bubble-sort/
# https://realpython.com/sorting-algorithms-python/#the-bubble-sort-algorithm-in-python
def bubbleSort(arr):
    n = len(arr) # n equal to number of elements in array

    # Outer loop which moves performs n-1 passes through array  
    for i in range(n-1):
        array_sorted = True # flag to end if array is already sorted
        
        # inner loop passes through each element comparing
        # and swapping out of place elements
        for j in range(0, n-i-1):

            # swapping elements if out of place
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

                # if any swaps happen on first run the array is not sorted
                array_sorted = False 

        if array_sorted: # break is array is already sorted on first loop big O(n)
            break

    return arr # return the sorted array


# mergeSort
# 2 parts, merge and mergesort
# https://realpython.com/sorting-algorithms-python/#the-merge-sort-algorithm-in-python

def merge(left, right):
	# if left half is empty return the right half    
    if len(left) == 0:
		return right
    # if right half is empty return the left half  
	if len(right) == 0:
		return left

    # temp array to store output
	res = []

    # initialize 2 counters i&j as 0
	i = j = 0

    # loop until res array is same size as left & right combined
	while len(res) < (len(left) + len(right)):
        # compare elements
		if left[i] <= right[j]:
            # add lower element to output array
			res.append(left[i])
			i += 1 # increment left counter by 1
		else: # add lower element to output array
			res.append(right[j])
			j += 1 # increment right counter by 1

        # if we get to the end of the right array
		if j == len(right):
			res += left[i:] # add rest of the left array
			break # end loop
        
        # if we get to the end of the left array
		if i == len(left):
			res += right[j:] # add rest of the right array
			break # end loop

	return res # return output array


def mergeSort(arr):
    # if array has 1 item or less return the array
	if len(arr) <= 1:
		return arr
    # key to split array in half
	mid = len(arr)//2

    # create left half and right half
	left = arr[0:mid]
	right = arr[mid:]

    # recursivley call mergesort on left and right halves
    # use merge function to merge those recursions
	return merge(mergeSort(left), mergeSort(right))


# https://realpython.com/sorting-algorithms-python/#the-insertion-sort-algorithm-in-python
def insertionSort(arr):

    # start with 2nd item and loop through array    
    for i in range(1, len(arr)):
        
        # key element to position
        key = arr[i]

        # variable to compare key from right to left
        j = i - 1

        # while key value less than element to left and not at start of array
        while j >= 0 and arr[j] > key:
    
            arr[j + 1] = arr[j] # rearrange positions
            j -= 1 # decrement to look at next item to left in array on next loop
       
        arr[j + 1] = key # position key item

    return arr # return array

# https://realpython.com/sorting-algorithms-python/#the-timsort-algorithm-in-python
def quickSortRandom(array):
    # return if array is 0 or 1 item in length
    if len(array) < 2:
        return array

    # initialize 3 list to store partitions
    low, same, high = [], [], []

    # Choose random item as pivot
    pivot = array[random.randint(0, len(array) - 1)]

    for item in array:
        
        if item < pivot: # assign to lower partition
            low.append(item)
        elif item == pivot: # assign values equal to pivot
            same.append(item)
        elif item > pivot: # assign to higher partition
            high.append(item)

    # return a recursive operation on the low and high partitions
    # combine the result with the same array 
    return quickSortRandom(low) + same + quickSortRandom(high)


# https://realpython.com/sorting-algorithms-python/#the-timsort-algorithm-in-python
def quickSortMiddle(array):
    # return if array is 0 or 1 item in length
    if len(array) < 2:
        return array
    # initialize 3 list to store partitions
    low, same, high = [], [], []

    # Choose middle item as pivot using int divison
    pivot = array[len(array)//2]

    for item in array:
        
        if item < pivot: # assign to lower partition
            low.append(item)
        elif item == pivot:# assign values equal to pivot
            same.append(item)
        elif item > pivot: # assign to higher partition
            high.append(item)

    # return a recursive operation on the low and high partitions
    # combine the result with the same array            
    return quickSortMiddle(low) + same + quickSortMiddle(high)


# https://www.programiz.com/dsa/counting-sort
def countingSort(arr):
    # starting max value
    max_val = 0
    # initiate empty output array
    output = [0] * len(arr) 
    
    # Find max element in array and assign to max_val
    for i in arr:
        if i > max_val:
            max_val = i

    # Create empty count array from 0-max value
    count = [0] * (max_val+1)
    
    # increment count array for each occurance
    for item in arr:
        count[item] +=1
    
    # modify count to cumulative sum array
    for c in range(len(count)-1):
        count[c+1] += count[c]
   
    # Start at the end of the array and work back    
    start = len(arr) - 1
    
    # map the input array vals to the correct output array position
    # decrement the cum sum count arry value by 1 each time
    while start >= 0:
        output[count[arr[start]]-1] = arr[start]
        count[arr[start]] -= 1
    
        start -= 1 # move from right to left in array
        
    return output # return sorted output array



