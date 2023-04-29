# Given a list of Integers, return the sum of all positive integers
def positive_sum(arr):
    result = []
    for number in arr:
        if number > 0:
            result.append(number)
    result = sum(result)
    if result is None:
        return 0
    else:
        return result


