
# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without
# any elements with the same value next to each other and preserving the original order of elements.

def unique_in_order(sequence: list)-> list:
    result = []
    prevchar = ''
    for char in sequence:
        if char != prevchar:
            result.append(char)
            prevchar = char
        else:
            continue
    return result
