tester = ['1', '2', '4', '97', '34', '13', '1', '3', '2', '44']


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if int(arr[j]) > int(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


print(bubble_sort(tester))
