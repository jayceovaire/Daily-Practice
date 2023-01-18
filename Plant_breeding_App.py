from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import random

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()

root.title("Cannabis Breeder App")
root.geometry(f"{1100}x{580}")

plant_label1 = customtkinter.CTkLabel(master=root, pady=5, padx=100, text="Plant 1")
plant_label1.grid(row=1, column=0)
plant_label2 = customtkinter.CTkLabel(master=root, pady=5, padx=100, text="Plant 2")
plant_label2.grid(row=2, column=0)

color_label = customtkinter.CTkLabel(master=root, text="Plant Color")
color_label.grid(row=0, column=4, pady=5, padx=10)
color_button1 = customtkinter.CTkSegmentedButton(master=root, values=["Green", "Purple"])
color_button1.grid(row=1, column=4, pady=5, padx=10)
color_button2 = customtkinter.CTkSegmentedButton(master=root, values=["Green","Purple"])
color_button2.grid(row=2, column=4, pady=5, padx=10)

height_label = customtkinter.CTkLabel(master=root, text="Plant Height")
height_label.grid(row=0, column=5, pady=5, padx=10)
height_button1 = customtkinter.CTkSegmentedButton(master=root, values=["Tall", "Short"])
height_button1.grid(row=1, column=5, pady=5, padx=10)
height_button2 = customtkinter.CTkSegmentedButton(master=root, values=["Tall","Short"])
height_button2.grid(row=2, column=5, pady=5, padx=10)

scent_label = customtkinter.CTkLabel(master=root, text="Plant Scent")
scent_label.grid(row=0, column=6, pady=5, padx=10)
scent_button1 = customtkinter.CTkSegmentedButton(master=root, values=["Scent1", "Scent2"])
scent_button1.grid(row=1, column=6, pady=5, padx=10)
scent_button2 = customtkinter.CTkSegmentedButton(master=root, values=["Scent1", "Scent2"])
scent_button2.grid(row=2, column=6, pady=5, padx=10)

flower_label = customtkinter.CTkLabel(master=root, text="Flower Density")
flower_label.grid(row=0, column=7, pady=5, padx=10)
flower_button1 = customtkinter.CTkSegmentedButton(master=root, values=["Light", "Medium", "Heavy"])
flower_button1.grid(row=1, column=7, pady=5, padx=10)
flower_button2 = customtkinter.CTkSegmentedButton(master=root, values=["Light", "Medium", "Heavy"])
flower_button2.grid(row=2, column=7, pady=5, padx=10)

strain_label = customtkinter.CTkLabel(master=root, text="Plant Strain-Type")
strain_label.grid(row=0, column=8, pady=5, padx=10)
strain_button1 = customtkinter.CTkSegmentedButton(master=root, values=["Indica", "Sativa", "Hybrid"])
strain_button1.grid(row=1, column=8, pady=5, padx=10)
strain_button2 = customtkinter.CTkSegmentedButton(master=root, values=["Indica", "Sativa", "Hybrid"])
strain_button2.grid(row=2, column=8, pady=5, padx=10)



class Plant:
    def __init__(self, color, height, smell, flower_size, strain):
        self.color = color
        self.height = height
        self.smell = smell
        self.flower_size = flower_size
        self.strain = strain

class App:
    def __init__(self):
        pass

def create_plant_1():
    color = color_button1.get()

    height = height_button1.get()
    scent = scent_button1.get()
    flower_size = flower_button1.get()
    strain = strain_button1.get()
    plant1 = Plant(color, height, scent, flower_size, strain)
    return plant1


def create_plant_2():
    color = color_button2.get()
    height = height_button2.get()
    scent = scent_button2.get()
    flower_size = flower_button2.get()
    strain = strain_button2.get()
    plant2 = Plant(color, height, scent, flower_size, strain)
    return plant2





def breed_plants():
    plant1 = create_plant_1()
    plant2 = create_plant_2()
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
    if plant1.strain == "Indica" and plant2.strain == "Sativa":
        strain = random.choice(["Indica", "Sativa", "Hybrid", "Hybrid"])

    elif plant1.strain == "Sativa" and plant2.strain == "Indica":
        strain = random.choice(["Indica", "Sativa", "Hybrid", "Hybrid"])
    else:
        # If the parent plants are both hybrid,
        # there is a 1/4 chance of creating a plant with "indica" strain,
        # a 1/4 chance of creating a plant with "sativa" strain,
        # and a 1/2 chance of creating a plant with "hybrid" strain
        if plant1.strain == "Hybrid" and plant2.strain == "Hybrid":
            strain = random.choice(["Indica", "Sativa", "Hybrid", "Hybrid"])

        elif plant1.strain == "Hybrid" and plant2.strain == "Indica":
            strain = random.choice(["Hybrid", "Indica", "Sativa", "Indica"])

        elif plant1.strain == "Hybrid" and plant2.strain == "Sativa":
            strain = random.choice(["Hybrid", "Indica", "Sativa", "Sativa"])

        elif plant2.strain == "Hybrid" and plant1.strain == "Indica":
            strain = random.choice(["Hybrid", "Indica", "Sativa", "Indica"])

        elif plant2.strain == "Hybrid" and plant1.strain == "Sativa":
            strain = random.choice(["Hybrid", "Indica", "Sativa", "Sativa"])

        else:
            strain = random.choice([plant1.strain, plant2.strain])

    # If the parent plants have different flower sizes,
    # there is a 1/3 chance of creating a plant with medium flower size
    if plant1.flower_size == "Light" and plant2.flower_size == "Heavy":
        flower_size = random.choice(["Light", "Heavy", "Medium"])
    else:
        flower_size = random.choice(
            [plant1.flower_size, plant2.flower_size])

    # Create new plant with random traits
    new_plant = Plant(color, height, smell, flower_size, strain)

    plants.append(new_plant)

    # Create a string representing the plant's traits
    trait_string = f"{color}, {height}, {smell}, {flower_size} flowers, {strain} strain"

    # Increment the count for this trait combination
    if trait_string in trait_counts:
        trait_counts[trait_string] += 1
    else:
        trait_counts[trait_string] = 1


plants = []
trait_counts = {}
strain_counts = {"Indica": 0, "Sativa": 0, "Hybrid": 0}
smell_counts = {"Scent1": 0, "Scent2": 0, "new smell": 0}
color_counts = {"Green": 0, "Purple": 0}
flower_counts = {"Heavy": 0, "Medium": 0, "Light": 0}
height_counts = {"Tall": 0, "Short": 0}




def breed_hundred_plants():
    for i in range(100):
        breed_plants()
def display_outcomes():
    # Calculate total number of plants
    total_plants = sum(trait_counts.values())
    for trait_string, count in trait_counts.items():
        percentage = 100 * count / total_plants
        print(f"{percentage:.2f}% of plants have traits: {trait_string}")

    # iterate through plants and update count of expected strain types
    for plant in plants:
        color_counts[plant.color] += 1
        height_counts[plant.height] += 1
        smell_counts[plant.smell] += 1
        flower_counts[plant.flower_size] += 1
        strain_counts[plant.strain] += 1

    # Print Individual Traits as percentages
    for color, count in color_counts.items():
        percentage = 100 * count / total_plants
        if percentage != 0.00:
            print(f"{percentage:.2f}% of plants are {color}")

    for height, count in height_counts.items():
        percentage = 100 * count / total_plants
        if percentage != 0.00:
            print(f"{percentage:.2f}% of plants are {height}")

    for smell, count in smell_counts.items():
        percentage = 100 * count / total_plants
        if percentage != 0.00:
            print(f"{percentage:.2f}% of plants smell {smell}")

    for flower, count in flower_counts.items():
        percentage = 100 * count / total_plants
        if percentage != 0.00:
            print(f"{percentage:.2f}% of plant flowers are {flower}")

    for strain, count in strain_counts.items():
        percentage = 100 * count / total_plants
        if percentage != 0.00:
            print(f"{percentage:.2f}% of plants are {strain}")

def Pprint():
    display_outcomes()

breed_button = customtkinter.CTkButton(master=root, text="Breed Plants", command=breed_hundred_plants)
breed_button.grid(row=4, column=6, pady=(50, 0), padx=10)

printbutton = customtkinter.CTkButton(master=root, text="Print", command=Pprint)
printbutton.grid(row=5, column=6, pady=5, padx=10)

if __name__ == "__main__":
    root.mainloop()
