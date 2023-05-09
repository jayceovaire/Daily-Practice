
#  you need to create a function that when provided with a triplet, returns the index of the
#  numerical element that lies between the other two elements.
# The input to the function will be an array of three distinct numbers (Haskell: a tuple).
# For example:
# gimme([2, 3, 1]) => 0


def gimme(input_array):
    ordered = sorted(input_array)
    target = ordered[1]
    position = 0
    for n in input_array:
        if n == target:
            return position
        else:
            position += 1
