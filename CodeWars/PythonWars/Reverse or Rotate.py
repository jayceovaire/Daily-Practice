
test = 'first_half second_half'


def rev_rot(s, sz):
    if sz <= 0 or not s or sz > len(s):
        return ""

    chunks = []
    for i in range(0, len(s), sz):
        chunks.append(s[i:i + sz])

    if len(chunks[-1]) < sz:
        chunks = chunks[:-1]

    for i in range(len(chunks)):
        chunk = chunks[i]
        sum_cubes = 0
        for d in chunk:
            sum_cubes += int(d) ** 3
        if sum_cubes % 2 == 0:
            chunks[i] = chunk[::-1]
        else:
            chunks[i] = chunk[1:] + chunk[0]

    result = ""
    for chunk in chunks:
        result += chunk

    return result


print(rev_rot(test, 9))