

def capitals(word):
    output = []
    for i in range(0, len(word)):
        if word[i] == word[i].upper():
            output.append(i)
    return output

def capitals2(word):
    return [i for i, letter in enumerate(word) if letter.isupper()]

