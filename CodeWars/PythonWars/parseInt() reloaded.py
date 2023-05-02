

def parse_int(string):
    words = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
             'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
             'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
             'eighty': 80, 'ninety': 90, 'hundred': 100, 'thousand': 1000, 'million': 1000000}

    string = string.replace('-', ' ')
    string = string.split(' ')

    total = 0
    sub_total = 0
    for word in string:
        if word == 'and':
            continue
        value = words[word]
        if value == 100:
            sub_total *= value
        elif value >= 1000:
            total = (total + sub_total) * value
            sub_total = 0
        else:
            if sub_total >= 100 and value < 100:
                sub_total += value
                total += sub_total
                sub_total = 0
            else:
                sub_total += value
    return total + sub_total
