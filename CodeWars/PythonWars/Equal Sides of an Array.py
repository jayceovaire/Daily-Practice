
# Given an array of numbers, iterate through the array and check if the sum of numbers on one side of
# any index are equal to the sum of the numbers on the other side of the index.
# example : function([1, 2, 3, 4, 3, 2, 1]) -> array[4] -> 4

testo = [1, 2, 3, 4, 3, 2, 1]

def find_even_index(arr):

    for i in range(len(arr)):
        left = sum(arr[:i])
        right = sum(arr[i + 1:])
        if left == right:
            return i
    return -1
