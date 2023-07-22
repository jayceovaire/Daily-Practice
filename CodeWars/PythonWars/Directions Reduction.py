def dirReduc(arr):
    opposite_directions = {
        'NORTH': 'SOUTH',
        'SOUTH': 'NORTH',
        'EAST': 'WEST',
        'WEST': 'EAST',
    }

    reduced_directions = []

    for direction in arr:
        if reduced_directions and reduced_directions[-1] == opposite_directions[direction]:
            reduced_directions.pop()
        else:
            reduced_directions.append(direction)

    return reduced_directions


test = ['EAST', 'SOUTH', 'WEST', 'WEST', 'EAST', 'EAST', 'EAST']
print(dirReduc(test))