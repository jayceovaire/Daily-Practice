
test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
toost = []

def max_sequence(arr: list) -> int:
    if not arr:
        return 0
    all_positive = True
    all_negative = True
    for num in arr:
        if num < 0:
            all_positive = False
        elif num > 0:
            all_negative = False

    if all_positive == True:
        return sum(arr)
    elif all_negative == True:
        return 0
    else:
        max_sum = arr[0]
        current_sum = arr[0]
        for num in arr[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum



print(max_sequence(test))
