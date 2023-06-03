
# Create a function that removes any  trailing zeros

def no_boring_zeros(n: int) -> int:
    n_copy = str(n)
    while n_copy[-1] == '0' and len(n_copy) > 1:
        n_copy = n_copy[:-1]
    return int(n_copy)

