import random

# Define plant class
class Plant:
    def __init__(self, color, height, smell, flower_size):
        self.color = color
        self.height = height
        self.smell = smell
        self.flower_size = flower_size
    def describe_plant(self):
        print(f"This plant is {self.color}, is {self.height}cm tall, and has a {self.smell} smell.")

# Define plant breeding function
def breed_plants(plant1, plant2, plants, trait_counts):
    # Randomly determine plant traits
    color = random.choice([plant1.color, plant2.color])
    height = random.choice([plant1.height, plant2.height])
    smell = random.choice([plant1.smell, plant2.smell])
    flower_size = random.choice([plant1.flower_size, plant2.flower_size])

    # Create new plant with random traits
    new_plant = Plant(color, height, smell, flower_size)
    # Add the new plant to the list of plants
    plants.append(new_plant)

    # Create a string representing the plant's traits
    trait_string = f"{color}, {height}, {smell}, {flower_size} flowers"

    # Increment the count for this trait combination
    if trait_string in trait_counts:
        trait_counts[trait_string] += 1
    else:
        trait_counts[trait_string] = 1

# Create initial plants
plant1 = Plant("purple", "tall", "sweet", "light")
plant2 = Plant("green", "short", "sour", "heavy")

# Initialize empty list of plants
plants = []

# Initialize empty dictionary for trait counts
trait_counts = {}

# Input number of plants to breed
num_plants = int(input("Enter number of plants to breed: "))

# Breed plants and print result
for i in range(num_plants):
    breed_plants(plant1, plant2, plants, trait_counts)

# Calculate total number of plants
total_plants = sum(trait_counts.values())

# Print trait counts as percentages
for trait_string, count in trait_counts.items():
    percentage = 100 * count / total_plants
    print(f"{percentage:.2f}% of plants have traits: {trait_string}")


