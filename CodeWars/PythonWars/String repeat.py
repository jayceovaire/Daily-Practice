# Write a function that accepts an integer n and a string s as parameters,
# and returns a string of s repeated exactly n times.

def repeat_str(repeat, string):
    result = []
    for line in range(repeat):
        result.append(string)
    return "".join(result)

def repeat_str2(repeat, string):
    if repeat <= 0:
        return ''
    return string + repeat_str2(repeat - 1, string)