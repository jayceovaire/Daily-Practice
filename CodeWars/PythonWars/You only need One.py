# You will be given an array a and a value x. All you need to do is check whether the
# provided array contains the value.
# Array can contain numbers or strings. X can be either.

def check(seq, elem):
    if elem in seq:
        return True
    else:
        return False

def check2(seq, elem):
    return elem in seq


