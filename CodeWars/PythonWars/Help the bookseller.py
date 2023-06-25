
b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B", "C", "D"]


def stock_list(list_of_art, list_of_cat):
    if list_of_art == '' or list_of_cat == '':
        return ''
    inventory = {}
    for char in list_of_cat:
        inventory[char] = 0

    for i in range(0, len(list_of_art)):
        split_item = list_of_art[i].split(' ')
        if split_item[0][0] not in inventory:
            inventory[split_item[0][0]] = int(split_item[1])
        else:
            inventory[split_item[0][0]] += int(split_item[1])

    returned_values = []

    for char in list_of_cat:
        if char in inventory:
            closure = f'({char} : {inventory[char]})'
            returned_values.append(closure)

    all_zero = True
    for char in inventory:
        if inventory[char] > 0:
            all_zero = False
        else:
            continue

    if all_zero == True:
        return ''
    else:
        return ' - '.join(returned_values)

