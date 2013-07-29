import math;
# Quicksort...

def quicksort(list):
	if list == []:
		return []
	
	pivot = list[0]
	smaller = quicksort([x for x in list[1:] if x < pivot])
	greater = quicksort([x for x in list[1:] if x >= pivot])
	return smaller + [pivot] + greater

print (quicksort([1, 76, 4, 1,434, 5,2,4,9,102,1,43,4,2,7,48]))