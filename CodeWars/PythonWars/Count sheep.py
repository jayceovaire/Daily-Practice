# Count sheep up to the given Integer Argument
import sys

def count_sheep(sheep):
    if sheep <= 0:
        return ''
    else:
        return count_sheep(sheep - 1) + f"{sheep} sheep..."

if len(sys.argv) < 2:
    print("Please provide the number of sheep to count")
else:
    num_sheep = int(sys.argv[1])
    result = count_sheep(num_sheep)
    print(result)
