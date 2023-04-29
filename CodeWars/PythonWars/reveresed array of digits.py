# write a function that takes in a number then returns
# an array of all characters
# of that number in reversed order.
# example (123) -> [3, 2, 1]

def digitize(n: int) -> list:

    num_list = []
    for char in str(n):
        num_list.append(int(char))
    num_list = num_list[::-1]
    return num_list







