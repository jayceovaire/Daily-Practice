# given a string return the string with the first letter of each word capitalized.

test = "how can mirros be real if our eyes aren't real?"

def to_jaden_case(string):
    words = string.split()
    jaden_case_words = []
    for word in words:
        jaden_case_words.append(word.capitalize())
    return " ".join(jaden_case_words)
