
# write a function that tests if the factor is a factor of base.
# Return true if it is a factor or false if it is not.

def check_for_factor(base: int, factor: int) -> bool:
    return  base % factor == 0