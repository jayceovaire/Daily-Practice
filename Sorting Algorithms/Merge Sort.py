import random

def merge(left, right):
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(left)
    merged.extend(right)
    return merged

def merge_sort(arr):
    stack = [[item] for item in arr]

    while len(stack) > 1:
        if len(stack) >= 2:
            merged = merge(stack.pop(-2), stack.pop(-1))
            stack.append(merged)
        else:
            break

    return stack[0]

# Generating two randomly unsorted lists of random numbers
random_list1 = [random.randint(1, 999) for _ in range(10)]
random_list2 = [random.randint(1, 999) for _ in range(10)]

print("First random list:", random_list1)
print("Second random list:", random_list2)

# Sorting the two lists using merge sort and then merging them
sorted_list1 = merge_sort(random_list1)
sorted_list2 = merge_sort(random_list2)

print("Sorted first list:", sorted_list1)
print("Sorted second list:", sorted_list2)

# Merging the two sorted lists
result = merge(sorted_list1, sorted_list2)
print("Merged and sorted result:", result)



