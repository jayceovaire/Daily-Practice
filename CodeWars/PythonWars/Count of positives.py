
# Given an array of numbers, return the total count of positive numbers and
# the sum of any and all negative numbers

def count_positives_sum_negatives(arr):
    if not arr:
        return []
    count = 0
    negatives = 0
    for number in arr:
        if number > 0:
            count += 1
        elif number < 0:
            negatives += number
    return [count, negatives]

