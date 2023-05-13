
# Complete the solution so that the function will break up camel casing, using a space between words.
def solution(string):
    result = ""
    for char in string:
        if char.isupper():
            result += " " + char
        else:
            result += char

    return result