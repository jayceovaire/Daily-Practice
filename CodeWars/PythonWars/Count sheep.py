# Count sheep up to the given Integer Argument

def count_sheep(sheep):
    if sheep <= 0:
        return ''
    else:
        return count_sheep(sheep - 1) + f"{sheep} sheep..."





