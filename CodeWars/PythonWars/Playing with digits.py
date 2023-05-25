


def dig_pow(n, p):
    n_str = str(n)
    total = 0

    for i, digit in enumerate(n_str):
        total += int(digit) ** (p + i)

    if total % n == 0:
        return total // n
    else:
        return -1


def dig_pow2(n, p):
    accumulator = 0
    n_str = str(n)

    for i in range(len(n_str)):
        accumulator += int(n_str[i]) ** (p + i)

    if accumulator % n == 0:
        return accumulator // n
    else:
        return -1

