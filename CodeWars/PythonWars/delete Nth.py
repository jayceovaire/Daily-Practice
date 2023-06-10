
check = []

def delete_nth(order: list, max_e: int) -> list:
    counter = {}
    newlist = []
    for num in order:
        if num not in counter:
            counter[num] = 1
        else:
            counter[num] += 1

        if counter[num] <= max_e:
            newlist.append(num)
        else:
            continue
    print(counter)

    return newlist

def delete_nthh(order: list, max_e: int) -> list:
    answer = []
    for num in order:
        if answer.count(num) < max_e:
            answer.append(num)
    return answer
