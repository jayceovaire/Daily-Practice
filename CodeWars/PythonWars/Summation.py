# Write a function that find the summation of every number from 1 to n.


def summation(num):
    if num == 0:
        return 0
    return num + summation(num - 1)

