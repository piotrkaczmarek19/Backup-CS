# -*-coding:utf-8 -#


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

numbers = [5,1,4,6,9,45,13,26,45]

print(mergeSort(numbers))