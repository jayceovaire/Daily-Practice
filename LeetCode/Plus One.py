
def plusOne(digits: [int]) -> [int]:

    numString = ''
    result = []

    for i in digits:
        numString += str(i)

    numString = int(numString) + 1

    for i in str(numString):
        result.append(int(i))

    return result


def PlusOne(digits: [int]) -> [int]:

    carry = 1

    for i in range(len(digits) - 1, -1, -1):
        digits[i] += carry
        carry = digits[i] // 10
        digits[i] %= 10

    if carry:
        digits.insert(0, carry)

    return digits