# -*-coding:utf-8 -#
import math

# loops through array [1 .. j - 1] in reverse and when i+1 is bigger than i, swaps them, then increment j
def insertSort(array):
	j = 1
	while j<len(array):
		key = array[j]
		i = j-1
		while i>=0 and array[i]>key:
			# after the key is replaced at the beginning, all the other keys to its right are moved one index to the right
			array[i+1] = array[i]
			i = i - 1
		array[i+1] = key
		j = j + 1 
	return array

# finds max in the array [1 .. n] (fillslot starts at n) and put it in An, then loops again through [1 .. n-1] and put it in An-1
def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)


array = [31, 41, 59, 26, 41, 58]

def linearSearch(array, v):
	i = 0
	while i<len(array):
		if array[i] == v:
			return i
		else:
			i = i + 1
	return -1

def mergeSort(numbers, *args):	
	pointer = []
	if len(numbers) == 1:
		return numbers 

	middle = len(numbers)//2
	first_array = numbers[:middle]
	second_array = numbers[middle:]

	mergeSort(first_array)
	mergeSort(second_array)

	i=0
	j=0
	k=0
	while i<len(first_array) and j<len(second_array):
		if first_array[i]<second_array[j]:
			numbers[k] = first_array[i]
			i= i+1
		else:
			numbers[k] = second_array[j]
			j= j+1
		k = k+1

	while i<len(first_array):
		numbers[k] = first_array[i]
		i = i+1
		k = k+1
	while j<len(second_array):
		numbers[k] = second_array[j]
		j = j+1
		k = k+1
	
	return numbers

# Taken from CLRS 4.1, the maximum subarray problem
stock_price = [100, 113, 110, 85, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]

def computeVariations(array):
	if len(array) == 1:
		return [0]*1
	variations = [0]*len(array)
	i = 1
	while i<len(array):
		variations[i] = array[i]-array[i-1]
		i = i + 1
		
	return variations

def findMaxCrossingSubarray(variations):
	middle = len(variations)//2
	
	# finds maximum subarray of left half
	low = 0
	totalSum = 0
	leftSum =  -float("inf")
	for i in range(middle, low, -1):
		totalSum = totalSum + variations[i]
		if totalSum > leftSum:
			leftSum = totalSum
			maxLeft = i

	# finds maximu subarray of right half
	rightSum = -float("inf")
	totalSum = 0
	for j in range(middle+1, len(variations)-1):
		totalSum = totalSum + variations[i]
		if totalSum>rightSum:
			rightSum = totalSum
			maxRight = j
	return(maxLeft, maxRight, leftSum + rightSum)

def findMaxSubarray(array, low, high):
	if high == low:
		return (low, high, variations[low])
	else:
		middle = (low+high)//2
print(findMaxSubarray(computeVariations(stock_price)))