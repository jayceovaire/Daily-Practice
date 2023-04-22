# 6kyu problem - given n, return a string of 1 + 1 / n
# in increments of 1/3 n-times.


def series_sum(n):
    total = 0
    for i in range(n):
        total +=  1 / (1 + 3 * i)
    return "{:.2f}".format(total)

