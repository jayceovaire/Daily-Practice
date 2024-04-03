import random
from timeit import default_timer as timer


random_list = [random.randint(1, 999) for _ in range(5)]
print(random_list)




def insertion_sort(array: []):
    new_array = []

    def insertion(array: [], to_insert):
        insert_location = 0

        while insert_location < len(array) and to_insert > array[insert_location]:
            insert_location += 1

        array.insert(insert_location, to_insert)
        return array

    for item in array:
        new_array = insertion(new_array, item)

    return new_array

start = timer()
sortedTestList = insertion_sort(random_list)
end = timer()

print(sortedTestList)
print(end - start)





