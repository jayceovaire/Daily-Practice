
# given 3 lengths of line return True if they can be used to form a triangle,
# return False otherwise.

def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
