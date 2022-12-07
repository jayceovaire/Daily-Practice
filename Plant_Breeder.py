import random

# Define plant class


class Plant:

    def __init__(self, color, height, smell, flower_size, strain):
        self.color = color
        self.height = height
        self.smell = smell
        self.flower_size = flower_size
        self.strain = strain


# Define plant breeding function
def breed_plants(plant1, plant2, plants, trait_counts):
    # Randomly determine plant traits
    color = random.choice([plant1.color, plant2.color])
    height = random.choice([plant1.height, plant2.height])

    # If the parent plants have different smells,
    # there is a 50% chance of creating a plant with "new smell"
    if plant1.smell != plant2.smell:
        smell = random.choice([plant1.smell, plant2.smell, "new smell"])
    else:
        smell = random.choice([plant1.smell, plant2.smell])

    # If the parent plants have different strains,
    # there is a 1/3 chance of creating a plant with "hybrid" strain
    if plant1.strain.lower() == "indica" and plant2.strain.lower() == "sativa":
        strain = random.choice(["indica", "sativa", "hybrid", "hybrid"])

    elif plant1.strain.lower() == "sativa" and plant2.strai.lower() == "indica":
        strain = random.choice(["indica", "sativa", "hybrid", "hybrid"])
    else:
        # If the parent plants are both hybrid,
        # there is a 1/4 chance of creating a plant with "indica" strain,
        # a 1/4 chance of creating a plant with "sativa" strain,
        # and a 1/2 chance of creating a plant with "hybrid" strain
        if plant1.strain.lower() == "hybrid" and plant2.strain.lower() == "hybrid":
            strain = random.choice(["indica", "sativa", "hybrid", "hybrid"])

        elif plant1.strain.lower() == "hybrid" and plant2.strain.lower() == "indica":
            strain = random.choice(["hybrid", "indica", "sativa", "indica"])

        elif plant1.strain.lower() == "hybrid" and plant2.strain.lower() == "sativa":
            strain = random.choice(["hybrid", "indica", "sativa", "sativa"])

        elif plant2.strain.lower() == "hybrid" and plant1.strain.lower() == "indica":
            strain = random.choice(["hybrid", "indica", "sativa", "indica"])

        elif plant2.strain.lower() == "hybrid" and plant1.strain.lower() == "sativa":
            strain = random.choice(["hybrid", "indica", "sativa", "sativa"])

        else:
            strain = random.choice([plant1.strain, plant2.strain])

    # If the parent plants have different flower sizes,
    # there is a 1/3 chance of creating a plant with medium flower size
    if plant1.flower_size == "light" and plant2.flower_size == "heavy":
        flower_size = random.choice(["light", "heavy", "medium"])
    else:
        flower_size = random.choice([plant1.flower_size, plant2.flower_size])

    # Create new plant with random traits
    new_plant = Plant(color, height, smell, flower_size, strain)
    # Add the new plant to the list of plants
    plants.append(new_plant)

    # Create a string representing the plant's traits
    trait_string = f"{color}, {height}, {smell}, {flower_size} flowers, {strain} strain"

    # Increment the count for this trait combination
    if trait_string in trait_counts:
        trait_counts[trait_string] += 1
    else:
        trait_counts[trait_string] = 1

# Create initial plants
# Prompt the user to input values for each trait of plant 1


color1 = input("Enter color of plant 1: ")

height1 = ""
while height1 not in ["tall", "short"]:
    height1 = input("Enter height of plant 1 (tall or short): ")

smell1 = input("Enter smell of plant 1: ")

flower_size1 = ""
while flower_size1 not in ["light", "medium", "heavy"]:
    flower_size1 = input("Enter flower size of plant 1 (light, medium, heavy): ")

strain1 = ""
while strain1 not in ["indica", "sativa", "hybrid"]:
    strain1 = input("Enter strain of plant 1 (indica, sativa, hybrid): ")

# Create plant 1
plant1 = Plant(color1, height1, smell1, flower_size1, strain1)

# Prompt the user to input values for each trait of plant 1
color2 = input("Enter color of plant 2: ")

height2 = ""
while height2 not in ["tall", "short"]:
    height2 = input("Enter height of plant 2 (tall or short): ")

smell2 = input("Enter smell of plant 2: ")

flower_size2 = ""
while flower_size2 not in ["light", "medium", "heavy"]:
    flower_size2 = input("Enter flower size of plant 2 (light, medium, heavy): ")

strain2 = ""
while strain2 not in ["indica", "sativa", "hybrid"]:
    strain2 = input("Enter strain of plant 2 (indica, sativa, hybrid): ")

# Create plant 2
plant2 = Plant(color2, height2, smell2, flower_size2, strain2)

# Initialize empty list of plants
plants = []

# Initialize empty dictionary for trait counts
trait_counts = {}

# Input number of plants to breed
num_plants = int(input("Enter number of seeds expected: "))

# Breed plants and print result
for i in range(num_plants):
    breed_plants(plant1, plant2, plants, trait_counts)

# Calculate total number of plants
total_plants = sum(trait_counts.values())

# Print trait counts as percentages
for trait_string, count in trait_counts.items():
    percentage = 100 * count / total_plants
    print(f"{percentage:.2f}% of plants have traits: {trait_string}")
