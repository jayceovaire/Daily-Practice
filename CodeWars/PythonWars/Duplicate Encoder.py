# The goal of this exercise is to convert a string to a new string where each character
# in the new string is "(" if that character appears only once in the original string, or ")" if that character
# appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

def duplicate_encode(word):
    encoder = {}
    for char in word:
        char = char.lower()
        if char not in encoder:
            encoder[char] = 1
        else:
            encoder[char] += 1

    returned_string = ''

    for char in word:
        char = char.lower()
        if encoder[char] > 1:
            returned_string += ')'
        else:
            returned_string += '('

    return returned_string
