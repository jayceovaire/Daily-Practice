def stray(arr: list) -> int:
    filter = {}
    for i in arr:
        if i not in filter:
            filter[i] = 1
        else:
            filter[i] += 1
    for j in filter:
        if filter[j] < 2:
            return j


# dictionary and list comprehension
def stray(arr: list) -> int:
    filter = {i: arr.count(i) for i in arr}
    return [key for key, value in filter.items() if value < 2][0]



