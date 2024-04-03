# Binary Search
#len 10
#target 8
# 0,1,2,3,4,5,6,7,8,9
#0 left
# 9 right
# mid = 0 + (9 - 0) // 2 == 4

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        print(left, right)
        print(mid)

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
target = 15
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in array")

