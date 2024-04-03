def length_of_last_word(s):
    words = []
    word = ''
    is_word_started = False

    for char in s:
        if char != ' ':
            word += char
            is_word_started = True
        elif is_word_started:
            words.append(word)
            word = ''
            is_word_started = False

    if word:
        words.append(word)
    if words:
        return len(words[-1])

    return 0

print(length_of_last_word('a   b    dog     cat    monkey    ape    '))

# can also just do words = s.strip().split() return len(words[-1])
