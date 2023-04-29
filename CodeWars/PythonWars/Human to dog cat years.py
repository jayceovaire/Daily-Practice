# Given a number of Human years return a list showing [human, cat, dog] years

def human_years_cat_years_dog_years(human_years):
    years_list = []
    years_list.append(human_years)
    cat_years = 0
    dog_years = 0
    for i in range(human_years):
        if cat_years >= 24:
            cat_years += 4
        elif cat_years == 15:
            cat_years += 9
        elif cat_years == 0:
            cat_years += 15
    years_list.append(cat_years)
    for i in range(human_years):
        if dog_years >= 24:
            dog_years += 5
        elif dog_years == 15:
            dog_years += 9
        elif dog_years == 0:
            dog_years += 15
    years_list.append(dog_years)

    return years_list