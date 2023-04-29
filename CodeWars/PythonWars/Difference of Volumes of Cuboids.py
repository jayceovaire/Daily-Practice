
# given 2 lists of dimensions of cuboids return the difference in their volumes

def find_difference(a: list, b: list) -> int:
    vol_A = a[0] * a[1] * a[2]
    vol_B = b[0] * b[1] * b[2]

    return abs(vol_A - vol_B)
