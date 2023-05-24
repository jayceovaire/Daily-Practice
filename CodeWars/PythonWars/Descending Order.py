def descending_order(num: int) -> int:
    output = sorted(str(num), reverse=True)
    output = int(''.join(output))
    return output





descending_order(98765)