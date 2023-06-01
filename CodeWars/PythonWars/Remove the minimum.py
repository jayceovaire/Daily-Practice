def remove_smallest(numbers: list) -> list:
    if numbers == []:
        return []
    copy = numbers.copy()
    copy.remove(min(copy))
    return copy
