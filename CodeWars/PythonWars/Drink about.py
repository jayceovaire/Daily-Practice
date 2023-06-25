# create a function that takes in an age and returns what the person of that age should drink

def people_with_age_drink(age: int) -> str:
    if age <= 13:
        return 'drink toddy'
    elif age <= 17:
        return 'drink coke'
    elif age <= 20:
        return 'drink beer'
    else:
        return 'drink whisky'