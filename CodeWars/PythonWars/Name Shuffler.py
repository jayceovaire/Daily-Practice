
# Write a function that returns a string in which firstname is swapped with last name.
def name_shuffler(str_):
    newstr = str_.split()
    newstr[0], newstr[1] = newstr[1], newstr[0]

    return ' '.join(newstr)

def name_shuffler2(str_):
    return ' '.join(reversed(str_.split()))
