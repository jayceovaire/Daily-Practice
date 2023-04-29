# Create a function that accepts a list and returns the sum of the two smallest
# numbers in that list


def sum_two_smallest_numbers(numbers):
    x = min(numbers)
    numbers.remove(x)
    y = min(numbers)
    return x + y



def sum_two_smallest_numbers2(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]



