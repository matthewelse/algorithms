import math

input_data = [5,7,2,3,8,1,4,6]

def mergesort(subset):
    if len(subset) == 1:
        return subset
    elif len(subset) > 1:
        # Perform merge sort.

        # Split into two.
        pivot = int(math.floor(len(subset)/2))

        left = subset[:pivot]
        right = subset[pivot:]

        left = mergesort(left)
        right = mergesort(right)

        output = []

        # Start with the first item of the left list...

        left_index = 0
        right_index = 0

        while (len(output) < len(subset)):
            if left_index >= len(left):
                output.extend(right[right_index:])
                continue
            elif right_index >= len(right):
                output.extend(left[left_index:])
                continue
            if (left[left_index] < right[right_index]):
                output.append(left[left_index])
                left_index += 1
            else:
                output.append(right[right_index])
                right_index += 1

        return output

print mergesort([5,7,2,3,8,1,4,1,6,5,8,3,8,23,7,34,7])