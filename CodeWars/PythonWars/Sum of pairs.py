

# O(n^2)
def sum_pairs(ints: list, s: int):
    if not ints:
        return None

    smallest_pair = None
    for i in range(len(ints)):
        for j in range(i + 1, len(ints)):
            pair = [ints[i], ints[j]]
            summed_pair = sum(pair)
            if summed_pair == s:
                if not smallest_pair or pair[0] < smallest_pair[0]:
                    smallest_pair = pair
    return smallest_pair

# O(n)
def sum_pairs2(ints, s):
    if not ints:
        return None

    seen = set()
    for num in ints:
        complement = s - num
        if complement in seen:
            return [complement, num]
        seen.add(num)
    return None
