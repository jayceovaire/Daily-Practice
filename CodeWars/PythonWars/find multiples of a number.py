
#  build a program that takes a value, integer , and returns a list of its multiples up to another value, limit .
#  If limit is a multiple of integer, it should be included as well. There will only ever be positive
#   integers passed into the function, not consisting of 0. The limit will always be higher than the base.

def find_multiples(integer: int, limit: int) -> list:
    result = []
    i = 1
    current_multiple = integer
    while current_multiple <= limit:
        result.append(current_multiple)
        i += 1
        current_multiple = integer * i
    return result


