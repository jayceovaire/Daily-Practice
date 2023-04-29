from tkinter import *
import customtkinter
import random

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()

root.title("Cannabis Breeder App")
root.geometry(f"{1100}x{580}")

plant_label1 = customtkinter.CTkLabel(master=root, pady=5, padx=85,
                                      text="Plant 1")
plant_label1.grid(row=1, column=0)
plant_label2 = customtkinter.CTkLabel(master=root, pady=5, padx=85,
                                      text="Plant 2")
plant_label2.grid(row=3, column=0)

color_label = customtkinter.CTkLabel(master=root, text="Plant Color")
color_label.grid(row=0, column=1, pady=5, padx=10)
color_button1 = customtkinter.CTkSegmentedButton(master=root,
                                                 values=["Green", "Purple"])
color_button1.grid(row=1, column=1, pady=5, padx=10)
color_button2 = customtkinter.CTkSegmentedButton(master=root,
                                                 values=["Green", "Purple"])
color_button2.grid(row=3, column=1, pady=5, padx=10)

height_label = customtkinter.CTkLabel(master=root, text="Plant Height")
height_label.grid(row=0, column=2, pady=5, padx=10)
height_button1 = customtkinter.CTkSegmentedButton(master=root,
                                                  values=["Tall", "Short"])
height_button1.grid(row=1, column=2, pady=5, padx=10)
height_button2 = customtkinter.CTkSegmentedButton(master=root,
                                                  values=["Tall", "Short"])
height_button2.grid(row=3, column=2, pady=5, padx=10)

scent_label = customtkinter.CTkLabel(master=root, text="Plant Scent")
scent_label.grid(row=0, column=3, pady=5, padx=10)
scent_button1 = customtkinter.CTkSegmentedButton(master=root,
                                                 values=["Scent1", "Scent2"])
scent_button1.grid(row=1, column=3, pady=5, padx=10)
scent_button2 = customtkinter.CTkSegmentedButton(master=root,
                                                 values=["Scent1", "Scent2"])
scent_button2.grid(row=3, column=3, pady=5, padx=10)

flower_label = customtkinter.CTkLabel(master=root, text="Flower Density")
flower_label.grid(row=0, column=4, pady=5, padx=10)
flower_button1 = customtkinter.CTkSegmentedButton(master=root,
                                                  values=["Small", "Big"])
flower_button1.grid(row=1, column=4, pady=5, padx=10)
flower_button2 = customtkinter.CTkSegmentedButton(master=root,
                                                  values=["Small", "Big"])
flower_button2.grid(row=3, column=4, pady=5, padx=10)

strain_label = customtkinter.CTkLabel(master=root, text="Plant Strain-Type")
strain_label.grid(row=0, column=5, pady=5, padx=10)
strain_button1 = customtkinter.CTkSegmentedButton(
    master=root, values=["Indica", "Sativa", "Hybrid"])
strain_button1.grid(row=1, column=5, pady=5, padx=10)
strain_button2 = customtkinter.CTkSegmentedButton(
    master=root, values=["Indica", "Sativa", "Hybrid"])
strain_button2.grid(row=3, column=5, pady=5, padx=10)

color_dom_rec_button1 = customtkinter.CTkSegmentedButton(
    master=root, values=["DD", "Dr", "rr"])
color_dom_rec_button1.grid(row=2, column=1, pady=5, padx=10)
color_dom_rec_button2 = customtkinter.CTkSegmentedButton(
    master=root, values=["DD", "Dr", "rr"])
color_dom_rec_button2.grid(row=4, column=1, pady=5, padx=10)

height_dom_rec_button1 = customtkinter.CTkSegmentedButton(
    master=root, values=["DD", "Dr", "rr"])
height_dom_rec_button1.grid(row=2, column=2, pady=5, padx=10)
height_dom_rec_button2 = customtkinter.CTkSegmentedButton(
    master=root, values=["DD", "Dr", "rr"])
height_dom_rec_button2.grid(row=4, column=2, pady=5, padx=10)


scent_dom_rec_button1 = customtkinter.CTkSegmentedButton(
    master=root, values=["DD", "Dr", "rr"])
scent_dom_rec_button1.grid(row=2, column=3, pady=5, padx=10)
scent_dom_rec_button2 = customtkinter.CTkSegmentedButton(
    master=root, values=["DD", "Dr", "rr"])
scent_dom_rec_button2.grid(row=4, column=3, pady=5, padx=10)

flower_dom_rec_button1 = customtkinter.CTkSegmentedButton(
    master=root, values=["DD", "Dr", "rr"])
flower_dom_rec_button1.grid(row=2, column=4, pady=5, padx=10)
flower_dom_rec_button2 = customtkinter.CTkSegmentedButton(
    master=root, values=["DD", "Dr", "rr"])
flower_dom_rec_button2.grid(row=4, column=4, pady=5, padx=10)

strain_dom_rec_button1 = customtkinter.CTkSegmentedButton(
    master=root, values=["DD", "Dr", "rr"])
strain_dom_rec_button1.grid(row=2, column=5, pady=5, padx=10)
strain_dom_rec_button2 = customtkinter.CTkSegmentedButton(
    master=root, values=["DD", "Dr", "rr"])
strain_dom_rec_button2.grid(row=4, column=5, pady=5, padx=10)


class BabyPlant:
    def __init__(self, color, height, scent, flower_size, strain):
        self.color = color
        self.height = height
        self.smell = scent
        self.flower_size = flower_size
        self.strain = strain


class Plant:
    def __init__(self, color, C_gene, height, H_gene, scent, S_gene,
                 flower_size, F_gene, strain, ST_gene):
        self.color = color
        self.height = height
        self.smell = scent
        self.flower_size = flower_size
        self.strain = strain
        self.C_gene = C_gene
        self.H_gene = H_gene
        self.S_gene = S_gene
        self.F_gene = F_gene
        self.ST_gene = ST_gene


def create_plant_1():
    color = color_button1.get()
    C_gene = color_dom_rec_button1.get()
    height = height_button1.get()
    H_gene = height_dom_rec_button1.get()
    scent = scent_button1.get()
    S_gene = scent_dom_rec_button1.get()
    flower_size = flower_button1.get()
    F_gene = flower_dom_rec_button1.get()
    strain = strain_button1.get()
    ST_gene = strain_dom_rec_button1.get()
    plant1 = Plant(color, C_gene, height, H_gene, scent,
                   S_gene, flower_size, F_gene, strain, ST_gene)
    return plant1


def create_plant_2():
    color = color_button2.get()
    C_gene = color_dom_rec_button2.get()
    height = height_button2.get()
    H_gene = height_dom_rec_button2.get()
    scent = scent_button2.get()
    S_gene = scent_dom_rec_button2.get()
    flower_size = flower_button2.get()
    F_gene = flower_dom_rec_button2.get()
    strain = strain_button2.get()
    ST_gene = strain_dom_rec_button2.get()
    plant2 = Plant(color, C_gene, height, H_gene, scent,
                   S_gene, flower_size, F_gene, strain, ST_gene)
    return plant2


def breed_plants():
    plant1 = create_plant_1()
    plant2 = create_plant_2()

    p_1_color = color_button1.get()
    p_1_height = height_button1.get()
    p_1_scent = scent_button1.get()
    p_1_flower = flower_button1.get()
    p_1_strain = strain_button1.get()
    p_2_color = color_button2.get()
    p_2_height = height_button2.get()
    p_2_scent = scent_button2.get()
    p_2_flower = flower_button2.get()
    p_2_strain = strain_button2.get()

    def get_color():
        if p_1_color == "Green" and p_2_color == "Green":
            if plant1.C_gene == "DD" and plant2.C_gene == "DD":
                color = "Green"
                return color
            elif plant1.C_gene == "DD" and plant2.C_gene == "Dr":
                color = "Green"
                return color
            elif plant1.C_gene == "DD" and plant2.C_gene == "rr":
                color = "Green"
                return color
            elif plant1.C_gene == "Dr" and plant2.C_gene == "DD":
                color = "Green"
                return color
            elif plant1.C_gene == "Dr" and plant2.C_gene == "Dr":
                color = random.choice(["Green", "Green", "Green", "X-Color"])
                return color
            elif plant1.C_gene == "Dr" and plant2.C_gene == "rr":
                color = random.choice(["Green", "Green", "X-Color", "X-Color"])
                return color
            elif plant1.C_gene == "rr" and plant2.C_gene == "DD":
                color = "Green"
                return color
            elif plant1.C_gene == "rr" and plant2.C_gene == "Dr":
                color = random.choice(["Green", "Green", "X-Color", "X-Color"])
                return color
            elif plant1.C_gene == "rr" and plant2.C_gene == "rr":
                color = "Green"
                return color


        elif p_1_color == "Green" and p_2_color == "Purple":
            if plant1.C_gene == "DD" and plant2.C_gene == "DD":
                color = "X-Color"
                return color
            elif plant1.C_gene == "DD" and plant2.C_gene == "Dr":
                color = random.choice(["Green", "X-Color"])
                return color
            elif plant1.C_gene == "DD" and plant2.C_gene == "rr":
                color = "Green"
                return color
            elif plant1.C_gene == "Dr" and plant2.C_gene == "DD":
                color = random.choice(["X-Color", "Purple"])
                return color
            elif plant1.C_gene == "Dr" and plant2.C_gene == "Dr":
                color = random.choice(["X-Color", "X-Color", "Green", "Purple"])
                return color
            elif plant1.C_gene == "Dr" and plant2.C_gene == "rr":
                color = random.choice(["Green", "Purple"])
                return color
            elif plant1.C_gene == "rr" and plant2.C_gene == "DD":
                color = "Purple"
                return color
            elif plant1.C_gene == "rr" and plant2.C_gene == "Dr":
                color = random.choice(["Purple", "Green"])
                return color
            elif plant1.C_gene == "rr" and plant2.C_gene == "rr":
                color = "X-Color"
                return color

        elif p_1_color == "Purple" and p_2_color == "Green":
            if plant1.C_gene == "DD" and plant2.C_gene == "DD":
                color = "X-Color"
                return color
            elif plant1.C_gene == "DD" and plant2.C_gene == "Dr":
                color = random.choice(["Green", "X-Color"])
                return color
            elif plant1.C_gene == "DD" and plant2.C_gene == "rr":
                color = "Green"
                return color
            elif plant1.C_gene == "Dr" and plant2.C_gene == "DD":
                color = random.choice(["X-Color", "Purple"])
                return color
            elif plant1.C_gene == "Dr" and plant2.C_gene == "Dr":
                color = random.choice(["X-Color", "X-Color", "Green", "Purple"])
                return color
            elif plant1.C_gene == "Dr" and plant2.C_gene == "rr":
                color = random.choice(["Green", "Purple"])
                return color
            elif plant1.C_gene == "rr" and plant2.C_gene == "DD":
                color = "Purple"
                return color
            elif plant1.C_gene == "rr" and plant2.C_gene == "Dr":
                color = random.choice(["Purple", "Green"])
                return color
            elif plant1.C_gene == "rr" and plant2.C_gene == "rr":
                color = "X-Color"
                return color

        elif p_1_color == "Purple" and p_2_color == "Purple":
            if plant1.C_gene == "DD" and plant2.C_gene == "DD":
                color = "Purple"
                return color
            elif plant1.C_gene == "DD" and plant2.C_gene == "Dr":
                color = "Purple"
                return color
            elif plant1.C_gene == "DD" and plant2.C_gene == "rr":
                color = "Purple"
                return color
            elif plant1.C_gene == "Dr" and plant2.C_gene == "DD":
                color = "Purple"
                return color
            elif plant1.C_gene == "Dr" and plant2.C_gene == "Dr":
                color = random.choice(["Purple", "Purple", "Purple", "X-Color"])
                return color
            elif plant1.C_gene == "Dr" and plant2.C_gene == "rr":
                color = random.choice(
                    ["Purple", "Purple", "X-Color", "X-Color"])
                return color
            elif plant1.C_gene == "rr" and plant2.C_gene == "DD":
                color = "Purple"
                return color
            elif plant1.C_gene == "rr" and plant2.C_gene == "Dr":
                color = random.choice(["Purple", "Purple",
                                       "X-Color", "X-Color"])
                return color
            elif plant1.C_gene == "rr" and plant2.C_gene == "rr":
                color = "Purple"
                return color

    def get_height():
        if p_1_height == "Tall" and p_2_height == "Tall":
            if plant1.H_gene == "DD" and plant2.H_gene == "DD":
                height = "Tall"
                return height
            if plant1.H_gene == "DD" and plant2.H_gene == "Dr":
                height = "Tall"
                return height
            if plant1.H_gene == "DD" and plant2.H_gene == "rr":
                height = "Tall"
                return height

            if plant1.H_gene == "Dr" and plant2.H_gene == "DD":
                height = "Tall"
                return height
            if plant1.H_gene == "Dr" and plant2.H_gene == "Dr":
                height = random.choice(["Tall", "Tall", "Tall", "X-Height"])
                return height
            if plant1.H_gene == "Dr" and plant2.H_gene == "rr":
                height = random.choice(["Tall", "X-Height"])
                return height

            if plant1.H_gene == "rr" and plant2.H_gene == "DD":
                height = "Tall"
                return height
            if plant1.H_gene == "rr" and plant2.H_gene == "Dr":
                height = random.choice(["Tall", "X-Height"])
                return height
            if plant1.H_gene == "rr" and plant2.H_gene == "rr":
                height = "Tall"
                return height

        if p_1_height == "Tall" and p_2_height == "Short":
            if plant1.H_gene == "DD" and plant2.H_gene == "DD":
                height = "X-Height"
                return height
            if plant1.H_gene == "DD" and plant2.H_gene == "Dr":
                height = random.choice(["Tall", "X-Height"])
                return height
            if plant1.H_gene == "DD" and plant2.H_gene == "rr":
                height = "Tall"
                return height

            if plant1.H_gene == "Dr" and plant2.H_gene == "DD":
                height = random.choice(["Short", "X-Height"])
                return height
            if plant1.H_gene == "Dr" and plant2.H_gene == "Dr":
                height = random.choice(["Short", "X-Height",
                                        "Tall", "X-Height"])
                return height
            if plant1.H_gene == "Dr" and plant2.H_gene == "rr":
                height = random.choice(["X-Height", "Tall"])
                return height

            if plant1.H_gene == "rr" and plant2.H_gene == "DD":
                height = "Short"
                return height
            if plant1.H_gene == "rr" and plant2.H_gene == "Dr":
                height = random.choice(["Short", "X-Height"])
                return height
            if plant1.H_gene == "rr" and plant2.H_gene == "rr":
                height = "X-Height"
                return height

        if p_1_height == "Short" and p_2_height == "Short":
            if plant1.H_gene == "DD" and plant2.H_gene == "DD":
                height = "Short"
                return height
            if plant1.H_gene == "DD" and plant2.H_gene == "Dr":
                height = "Short"
                return height
            if plant1.H_gene == "DD" and plant2.H_gene == "rr":
                height = "Short"
                return height

            if plant1.H_gene == "Dr" and plant2.H_gene == "DD":
                height = "Short"
                return height
            if plant1.H_gene == "Dr" and plant2.H_gene == "Dr":
                height = random.choice(["Short", "Short", "Short", "X-Height"])
                return height
            if plant1.H_gene == "Dr" and plant2.H_gene == "rr":
                height = random.choice(["Short", "X-Height"])
                return height

            if plant1.H_gene == "rr" and plant2.H_gene == "DD":
                height = "Short"
                return height
            if plant1.H_gene == "rr" and plant2.H_gene == "Dr":
                height = random.choice(["Short", "X-Height"])
                return height
            if plant1.H_gene == "rr" and plant2.H_gene == "rr":
                height = "Short"
                return height

        if p_1_height == "Short" and p_2_height == "Tall":
            if plant1.H_gene == "DD" and plant2.H_gene == "DD":
                height = "X-Height"
                return height
            if plant1.H_gene == "DD" and plant2.H_gene == "Dr":
                height = random.choice(["Short", "X-Height"])
                return height
            if plant1.H_gene == "DD" and plant2.H_gene == "rr":
                height = "Short"
                return height

            if plant1.H_gene == "Dr" and plant2.H_gene == "DD":
                height = random.choice(["Tall", "X-Height"])
                return height
            if plant1.H_gene == "Dr" and plant2.H_gene == "Dr":
                height = random.choice(["Short", "X-Height",
                                        "Tall", "X-Height"])
                return height
            if plant1.H_gene == "Dr" and plant2.H_gene == "rr":
                height = random.choice(["X-Height", "Short"])
                return height

            if plant1.H_gene == "rr" and plant2.H_gene == "DD":
                height = "Tall"
                return height
            if plant1.H_gene == "rr" and plant2.H_gene == "Dr":
                height = random.choice(["Tall", "X-Height"])
                return height
            if plant1.H_gene == "rr" and plant2.H_gene == "rr":
                height = "X-Height"
                return height

    def get_scent():
        if p_1_scent == "Scent1" and p_2_scent == "Scent1":
            if plant1.S_gene == "DD" and plant2.S_gene == "DD":
                scent = "Scent1"
                return scent
            if plant1.S_gene == "DD" and plant2.S_gene == "Dr":
                scent = "Scent1"
                return scent
            if plant1.S_gene == "DD" and plant2.S_gene == "rr":
                scent = "Scent1"
                return scent
            if plant1.S_gene == "Dr" and plant2.S_gene == "DD":
                scent = "Scent1"
            if plant1.S_gene == "Dr" and plant2.S_gene == "Dr":
                scent = random.choice(["Scent1", "Scent1", "Scent1", "X-Scent"])
                return scent
            if plant1.S_gene == "Dr" and plant2.S_gene == "rr":
                scent = random.choice(["Scent1", "X-Scent"])
                return scent
            if plant1.S_gene == "rr" and plant2.S_gene == "DD":
                scent = "Scent1"
                return scent
            if plant1.S_gene == "rr" and plant2.S_gene == "Dr":
                scent = random.choice(["Scent1", "X-Scent"])
                return scent
            if plant1.S_gene == "rr" and plant2.S_gene == "rr":
                scent = "X-Scent"
                return scent

        if p_1_scent == "Scent1" and p_2_scent == "Scent2":
            if plant1.S_gene == "DD" and plant2.S_gene == "DD":
                scent = random.choice(["X-Scent"])
                return scent
            if plant1.S_gene == "DD" and plant2.S_gene == "Dr":
                scent = random.choice(["X-Scent", "Scent1",
                                       "X-Scent", "Scent1"])
                return scent
            if plant1.S_gene == "DD" and plant2.S_gene == "rr":
                scent = "Scent1"
                return scent
            if plant1.S_gene == "Dr" and plant2.S_gene == "DD":
                scent = random.choice(["X-Scent", "Scent2"])
                return scent
            if plant1.S_gene == "Dr" and plant2.S_gene == "Dr":
                scent = random.choice(["X-Scent", "X-Scent",
                                       "Scent1", "Scent2"])
                return scent
            if plant1.S_gene == "Dr" and plant2.S_gene == "rr":
                scent = random.choice(["Scent1", "X-Scent"])
                return scent
            if plant1.S_gene == "rr" and plant2.S_gene == "DD":
                scent = "Scent2"
                return scent
            if plant1.S_gene == "rr" and plant2.S_gene == "Dr":
                scent = random.choice(["X-Scent", "Scent2"])
                return scent
            if plant1.S_gene == "rr" and plant2.S_gene == "rr":
                scent = random.choice(["X-Scent"])
                return scent

        if p_1_scent == "Scent2" and p_2_scent == "Scent1":
            if plant1.S_gene == "DD" and plant2.S_gene == "DD":
                scent = ""
                return scent
            if plant1.S_gene == "DD" and plant2.S_gene == "Dr":
                scent = ""
                return scent
            if plant1.S_gene == "DD" and plant2.S_gene == "rr":
                scent = " "
                return scent
            if plant1.S_gene == "Dr" and plant2.S_gene == "DD":
                scent = " "
                return scent
            if plant1.S_gene == "Dr" and plant2.S_gene == "Dr":
                scent = ""
                return scent
            if plant1.S_gene == "Dr" and plant2.S_gene == "rr":
                scent = " "
                return scent
            if plant1.S_gene == "rr" and plant2.S_gene == "DD":
                scent = " "
                return scent
            if plant1.S_gene == "rr" and plant2.S_gene == "Dr":
                scent = " "
                return scent
            if plant1.S_gene == "rr" and plant2.S_gene == "rr":
                scent = ""
                return scent


        if p_1_scent == "Scent2" and p_2_scent == "Scent2":
            if plant1.S_gene == "DD" and plant2.S_gene == "DD":
                scent = "Scent2"
                return scent
            if plant1.S_gene == "DD" and plant2.S_gene == "Dr":
                scent = "Scent2"
                return scent
            if plant1.S_gene == "DD" and plant2.S_gene == "rr":
                scent = "Scent2"
                return scent
            if plant1.S_gene == "Dr" and plant2.S_gene == "DD":
                scent = "Scent2"
                return scent
            if plant1.S_gene == "Dr" and plant2.S_gene == "Dr":
                scent = random.choice(["Scent2", "Scent2",
                                       "Scent2", "X-Scent"])
                return scent
            if plant1.S_gene == "Dr" and plant2.S_gene == "rr":
                scent = random.choice(["Scent2", "X-Scent"])
                return scent
            if plant1.S_gene == "rr" and plant2.S_gene == "DD":
                scent = "Scent2"
                return scent
            if plant1.S_gene == "rr" and plant2.S_gene == "Dr":
                scent = random.choice(["Scent2", "X-Scent"])
                return scent
            if plant1.S_gene == "rr" and plant2.S_gene == "rr":
                scent = "X-Scent"
                return scent

    def get_flower_size():

        if p_1_flower == "Small" and p_2_flower == "Small":
            if plant1.F_gene == "DD" and plant2.F_gene == "DD":
                flower_size = "Small"
                return flower_size
            if plant1.F_gene == "DD" and plant2.F_gene == "Dr":
                flower_size = "Small"
                return flower_size
            if plant1.F_gene == "DD" and plant2.F_gene == "rr":
                flower_size = "Small"
                return flower_size
            if plant1.F_gene == "Dr" and plant2.F_gene == "DD":
                flower_size = "Small"
                return flower_size
            if plant1.F_gene == "Dr" and plant2.F_gene == "Dr":
                flower_size = random.choice(["Small", "Small",
                                             "Small", "X-Size"])
                return flower_size
            if plant1.F_gene == "Dr" and plant2.F_gene == "rr":
                flower_size = random.choice(["Small", "X-Size"])
                return flower_size
            if plant1.F_gene == "rr" and plant2.F_gene == "DD":
                flower_size = "Small"
                return flower_size
            if plant1.F_gene == "rr" and plant2.F_gene == "Dr":
                flower_size = random.choice(["Small", "X-size"])
                return flower_size
            if plant1.F_gene == "rr" and plant2.F_gene == "rr":
                flower_size = "Small"
                return flower_size

        if p_1_flower == "Small" and p_2_flower == "Big":
            if plant1.F_gene == "DD" and plant2.F_gene == "DD":
                flower_size = "X-Size"
                return flower_size
            if plant1.F_gene == "DD" and plant2.F_gene == "Dr":
                flower_size = random.choice(["Small", "X-Size"])
                return flower_size
            if plant1.F_gene == "DD" and plant2.F_gene == "rr":
                flower_size = "Small"
                return flower_size
            if plant1.F_gene == "Dr" and plant2.F_gene == "DD":
                flower_size = random.choice(["Big", "X-Size"])
                return flower_size
            if plant1.F_gene == "Dr" and plant2.F_gene == "Dr":
                flower_size = random.choice(["X-Size", "X-Size",
                                             "Small", "Big"])
                return flower_size
            if plant1.F_gene == "Dr" and plant2.F_gene == "rr":
                flower_size = random.choice(["Small", "X-Size"])
                return flower_size
            if plant1.F_gene == "rr" and plant2.F_gene == "DD":
                flower_size = "Big"
                return flower_size
            if plant1.F_gene == "rr" and plant2.F_gene == "Dr":
                flower_size = random.choice(["Big", "X-Size"])
                return flower_size
            if plant1.F_gene == "rr" and plant2.F_gene == "rr":
                flower_size = "X-Size"
                return flower_size

        if p_1_flower == "Big" and p_2_flower == "Big":
            if plant1.F_gene == "DD" and plant2.F_gene == "DD":
                flower_size = "Big"
                return flower_size
            if plant1.F_gene == "DD" and plant2.F_gene == "Dr":
                flower_size = "Big"
                return flower_size
            if plant1.F_gene == "DD" and plant2.F_gene == "rr":
                flower_size = "Big"
                return flower_size
            if plant1.F_gene == "Dr" and plant2.F_gene == "DD":
                flower_size = "Big"
                return flower_size
            if plant1.F_gene == "Dr" and plant2.F_gene == "Dr":
                flower_size = random.choice(["Big", "Big", "Big", "X-Size"])
                return flower_size
            if plant1.F_gene == "Dr" and plant2.F_gene == "rr":
                flower_size = random.choice(["Big", "X-Size"])
                return flower_size
            if plant1.F_gene == "rr" and plant2.F_gene == "DD":
                flower_size = "Big"
                return flower_size
            if plant1.F_gene == "rr" and plant2.F_gene == "Dr":
                flower_size = random.choice(["Big", "X-size"])
                return flower_size
            if plant1.F_gene == "rr" and plant2.F_gene == "rr":
                flower_size = "Big"
                return flower_size

        if p_1_flower == "Big" and p_2_flower == "Small":
            if plant1.F_gene == "DD" and plant2.F_gene == "DD":
                flower_size = "X-Size"
                return flower_size
            if plant1.F_gene == "DD" and plant2.F_gene == "Dr":
                flower_size = random.choice(["Big", "X-Size"])
                return flower_size
            if plant1.F_gene == "DD" and plant2.F_gene == "rr":
                flower_size = "Big"
                return flower_size
            if plant1.F_gene == "Dr" and plant2.F_gene == "DD":
                flower_size = random.choice(["Small", "X-Size"])
                return flower_size
            if plant1.F_gene == "Dr" and plant2.F_gene == "Dr":
                flower_size = random.choice(["X-Size", "X-Size",
                                             "Small", "Big"])
                return flower_size
            if plant1.F_gene == "Dr" and plant2.F_gene == "rr":
                flower_size = random.choice(["Big", "X-Size"])
                return flower_size
            if plant1.F_gene == "rr" and plant2.F_gene == "DD":
                flower_size = "Small"
                return flower_size
            if plant1.F_gene == "rr" and plant2.F_gene == "Dr":
                flower_size = random.choice(["Small", "X-Size"])
                return flower_size
            if plant1.F_gene == "rr" and plant2.F_gene == "rr":
                flower_size = "X-Size"
                return flower_size

    def get_strain():
        if p_1_strain == "Indica" and p_2_strain == "Indica":
            if plant1.ST_gene == "DD" and plant2.ST_gene == "DD":
                strain = "Indica"
                return strain
            if plant1.ST_gene == "DD" and plant2.ST_gene == "Dr":
                strain = "Indica"
                return strain
            if plant1.ST_gene == "DD" and plant2.ST_gene == "rr":
                strain = "Indica"
                return strain
            if plant1.ST_gene == "Dr" and plant2.ST_gene == "DD":
                strain = "Indica"
                return strain
            if plant1.ST_gene == "Dr" and plant2.ST_gene == "Dr":
                strain = "Indica"
                return strain
            if plant1.ST_gene == "Dr" and plant2.ST_gene == "rr":
                strain = "Indica"
                return strain
            if plant1.ST_gene == "rr" and plant2.ST_gene == "DD":
                strain = "Indica"
                return strain
            if plant1.ST_gene == "rr" and plant2.ST_gene == "Dr":
                strain = "Indica"
                return strain
            if plant1.ST_gene == "rr" and plant2.ST_gene == "rr":
                strain = "Indica"
                return strain

        if p_1_strain == "Sativa" and p_2_strain == "Sativa":
            if plant1.ST_gene == "DD" and plant2.ST_gene == "DD":
                strain = "Sativa"
                return strain
            if plant1.ST_gene == "DD" and plant2.ST_gene == "Dr":
                strain = "Sativa"
                return strain
            if plant1.ST_gene == "DD" and plant2.ST_gene == "rr":
                strain = "Sativa"
                return strain
            if plant1.ST_gene == "Dr" and plant2.ST_gene == "DD":
                strain = "Sativa"
                return strain
            if plant1.ST_gene == "Dr" and plant2.ST_gene == "Dr":
                strain = "Sativa"
                return strain
            if plant1.ST_gene == "Dr" and plant2.ST_gene == "rr":
                strain = "Sativa"
                return strain
            if plant1.ST_gene == "rr" and plant2.ST_gene == "DD":
                strain = "Sativa"
                return strain
            if plant1.ST_gene == "rr" and plant2.ST_gene == "Dr":
                strain = "Sativa"
                return strain
            if plant1.ST_gene == "rr" and plant2.ST_gene == "rr":
                strain = "Sativa"
                return strain

        if p_1_strain == "Hybrid" and p_2_strain == "Hybrid":
            if plant1.ST_gene == "DD" and plant2.ST_gene == "DD":
                strain = random.choice(["Hybrid", "Hybrid", "Sativa", "Indica"])
                return strain
            if plant1.ST_gene == "DD" and plant2.ST_gene == "Dr":
                strain = random.choice(["Hybrid", "Hybrid", "Sativa", "Indica"])
                return strain
            if plant1.ST_gene == "DD" and plant2.ST_gene == "rr":
                strain = random.choice(["Hybrid", "Hybrid", "Sativa", "Indica"])
                return strain
            if plant1.ST_gene == "Dr" and plant2.ST_gene == "DD":
                strain = random.choice(["Hybrid", "Hybrid", "Sativa", "Indica"])
                return strain
            if plant1.ST_gene == "Dr" and plant2.ST_gene == "Dr":
                strain = random.choice(["Hybrid", "Hybrid", "Sativa", "Indica"])
                return strain
            if plant1.ST_gene == "Dr" and plant2.ST_gene == "rr":
                strain = random.choice(["Hybrid", "Hybrid", "Sativa", "Indica"])
                return strain
            if plant1.ST_gene == "rr" and plant2.ST_gene == "DD":
                strain = random.choice(["Hybrid", "Hybrid", "Sativa", "Indica"])
                return strain
            if plant1.ST_gene == "rr" and plant2.ST_gene == "Dr":
                strain = random.choice(["Hybrid", "Hybrid", "Sativa", "Indica"])
                return strain
            if plant1.ST_gene == "rr" and plant2.ST_gene == "rr":
                strain = random.choice(["Hybrid", "Hybrid", "Sativa", "Indica"])
                return strain

        if p_1_strain == "Indica" and p_2_strain == "Sativa":
            if plant1.ST_gene == "DD" and plant2.ST_gene == "DD":
                strain = "Hybrid"
                return strain
            if plant1.ST_gene == "DD" and plant2.ST_gene == "Dr":
                strain = random.choice(["Hybrid", "Indica"])
                return strain
            if plant1.ST_gene == "DD" and plant2.ST_gene == "rr":
                strain = "Indica"
                return strain

            if plant1.ST_gene == "Dr" and plant2.ST_gene == "DD":
                strain = random.choice(["Hybrid", "Sativa"])
                return strain
            if plant1.ST_gene == "Dr" and plant2.ST_gene == "Dr":
                strain = random.choice(["Hybrid", "Hybrid", "Indica", "Sativa"])
                return strain
            if plant1.ST_gene == "Dr" and plant2.ST_gene == "rr":
                strain = random.choice(["Hybrid", "Indica"])
                return strain

            if plant1.ST_gene == "rr" and plant2.ST_gene == "DD":
                strain = "Sativa"
                return strain
            if plant1.ST_gene == "rr" and plant2.ST_gene == "Dr":
                strain = random.choice(["Sativa", "Hybrid"])
                return strain
            if plant1.ST_gene == "rr" and plant2.ST_gene == "rr":
                strain = 'Hybrid'
                return strain

        if p_1_strain == "Sativa" and p_2_strain == "Indica":
            if plant1.ST_gene == "DD" and plant2.ST_gene == "DD":
                strain = "Hybrid"
                return strain
            if plant1.ST_gene == "DD" and plant2.ST_gene == "Dr":
                strain = random.choice(["Hybrid", "Sativa"])
                return strain
            if plant1.ST_gene == "DD" and plant2.ST_gene == "rr":
                strain = "Sativa"
                return strain

            if plant1.ST_gene == "Dr" and plant2.ST_gene == "DD":
                strain = random.choice(["Hybrid", "Indica"])
                return strain
            if plant1.ST_gene == "Dr" and plant2.ST_gene == "Dr":
                strain = random.choice(["Hybrid", "Hybrid", "Indica", "Sativa"])
                return strain
            if plant1.ST_gene == "Dr" and plant2.ST_gene == "rr":
                strain = random.choice(["Hybrid", "Sativa"])
                return strain

            if plant1.ST_gene == "rr" and plant2.ST_gene == "DD":
                strain = "Indica"
                return strain
            if plant1.ST_gene == "rr" and plant2.ST_gene == "Dr":
                strain = random.choice(["Indica", "Hybrid"])
                return strain
            if plant1.ST_gene == "rr" and plant2.ST_gene == "rr":
                strain = 'Hybrid'
                return strain

        if p_1_strain == "Indica" and p_2_strain == "Hybrid":
            if plant1.ST_gene == "DD" and plant2.ST_gene == "DD":
                strain = random.choice(["Indica", "Indica", "Indica", "Hybrid"])
                return strain
            if plant1.ST_gene == "DD" and plant2.ST_gene == "Dr":
                strain = random.choice(["Indica", "Hybrid"])
                return strain
            if plant1.ST_gene == "DD" and plant2.ST_gene == "rr":
                strain = "Indica"
                return strain

            if plant1.ST_gene == "Dr" and plant2.ST_gene == "DD":
                strain = random.choice(["Indica", "Hybrid", "Hybrid"])
                return strain
            if plant1.ST_gene == "Dr" and plant2.ST_gene == "Dr":
                strain = random.choice(["Indica", "Hybrid"])
                return strain
            if plant1.ST_gene == "Dr" and plant2.ST_gene == "rr":
                strain = random.choice(["Sativa", "Indica", "Indica", "Indica",
                                        "Indica", "Indica", "Indica", "Indica",
                                        "Hybrid", "Hybrid", "Hybrid", "Hybrid",
                                        "Hybrid", "Hybrid", "Hybrid", "Hybrid"])
                return strain

            if plant1.ST_gene == "rr" and plant2.ST_gene == "DD":
                strain = random.choice(["Indica", "Hybrid", "Hybrid", "Sativa"])
                return strain
            if plant1.ST_gene == "rr" and plant2.ST_gene == "Dr":
                strain = random.choice(["Indica", "Hybrid", "Hybrid", "Sativa"])
                return strain
            if plant1.ST_gene == "rr" and plant2.ST_gene == "rr":
                strain = "Hybrid"
                return strain

        if p_1_strain == "Sativa" and p_2_strain == "Hybrid":
            if plant1.ST_gene == "DD" and plant2.ST_gene == "DD":
                strain = random.choice(["Sativa","Sativa", "Sativa", "Hybrid"])
                return strain
            if plant1.ST_gene == "DD" and plant2.ST_gene == "Dr":
                strain = random.choice(["Sativa", "Hybrid"])
                return strain
            if plant1.ST_gene == "DD" and plant2.ST_gene == "rr":
                strain = "Sativa"
                return strain

            if plant1.ST_gene == "Dr" and plant2.ST_gene == "DD":
                strain = random.choice(["Sativa", "Hybrid", "Hybrid"])
                return strain
            if plant1.ST_gene == "Dr" and plant2.ST_gene == "Dr":
                strain = random.choice(["Sativa", "Hybrid"])
                return strain
            if plant1.ST_gene == "Dr" and plant2.ST_gene == "rr":
                strain = random.choice(["Indica", "Sativa", "Sativa", "Sativa",
                                        "Sativa", "Sativa", "Sativa", "Sativa",
                                        "Hybrid", "Hybrid", "Hybrid", "Hybrid",
                                        "Hybrid", "Hybrid", "Hybrid", "Hybrid"])
                return strain

            if plant1.ST_gene == "rr" and plant2.ST_gene == "DD":
                strain = random.choice(["Indica", "Hybrid", "Hybrid", "Sativa"])
                return strain
            if plant1.ST_gene == "rr" and plant2.ST_gene == "Dr":
                strain = random.choice(["Indica", "Hybrid", "Hybrid", "Sativa"])
                return strain
            if plant1.ST_gene == "rr" and plant2.ST_gene == "rr":
                strain = "Hybrid"
                return strain

    color = get_color()
    height = get_height()
    scent = get_scent()
    flower_size = get_flower_size()
    strain = get_strain()

    # Create new plant with random traits
    new_plant = BabyPlant(color, height, scent, flower_size, strain)

    plants.append(new_plant)

    # Create a string representing the plant's traits
    trait_string = f"{color}, {height}, {scent}," \
                   f" {flower_size} flowers, {strain} strain"

    # Increment the count for this trait combination
    if trait_string in trait_counts:
        trait_counts[trait_string] += 1
    else:
        trait_counts[trait_string] = 1


plants = []
trait_counts = {}
strain_counts = {"Indica": 0, "Sativa": 0, "Hybrid": 0}
smell_counts = {"Scent1": 0, "Scent2": 0, "X-Scent": 0}
color_counts = {"Green": 0, "Purple": 0, "X-Color": 0}
flower_counts = {"Big": 0, "Small": 0, "X-Size": 0}
height_counts = {"Tall": 0, "Short": 0, "X-Height": 0}
colors = []
scents = []
flowers = []
strains = []
heights = []


def breed_hundred_plants():
    disable_breed_button()
    for i in range(100):
        breed_plants()
    display_outcomes()



def display_outcomes():
    # Calculate total number of plants
    total_plants = sum(trait_counts.values())
    for trait_string, count in trait_counts.items():
        percentage = 100 * count / total_plants
        if percentage != 0.00:
            outcome_box.insert(0.0, text=f"{percentage:.2f}% of plants"
                                         f" have traits: {trait_string}\n")

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
            outcome_box.insert(0.0, text=f"{percentage:.2f}%"
                                         f" of plants are {color}\n")

    for height, count in height_counts.items():
        percentage = 100 * count / total_plants
        if percentage != 0.00:
            outcome_box.insert(0.0, text=f"{percentage:.2f}%"
                                         f" of plants are {height}\n")

    for smell, count in smell_counts.items():
        percentage = 100 * count / total_plants
        if percentage != 0.00:
            outcome_box.insert(0.0, text=f"{percentage:.2f}%"
                                         f" of plants smell {smell}\n")

    for flower, count in flower_counts.items():
        percentage = 100 * count / total_plants
        if percentage != 0.00:
            outcome_box.insert(0.0, text=f"{percentage:.2f}%"
                                         f" of plant flowers are {flower}\n")

    for strain, count in strain_counts.items():
        percentage = 100 * count / total_plants
        if percentage != 0.00:
            outcome_box.insert(0.0, text=f"{percentage:.2f}%"
                                         f" of plants are {strain}\n")


def reset_breed_button():
    breed_button.configure(state="normal")


def reset_strains():
    for key in strain_counts:
        strain_counts[key] = 0


def reset_colors():
    for key in color_counts:
        color_counts[key] = 0


def reset_heights():
    for key in height_counts:
        height_counts[key] = 0


def reset_flowers():
    for key in flower_counts:
        flower_counts[key] = 0


def reset_scents():
    for key in smell_counts:
        smell_counts[key] = 0


def reset_traits():
    for key in trait_counts:
        trait_counts[key] = 0


def reset_plants():
    plants.clear()
    colors.clear()
    heights.clear()
    flowers.clear()
    scents.clear()
    strains.clear()


def reset_textbox():
    outcome_box.delete("0.0", "end")


def reset_all():
    reset_textbox()
    reset_plants()
    reset_strains()
    reset_traits()
    reset_scents()
    reset_colors()
    reset_heights()
    reset_flowers()
    reset_breed_button()



breed_button = customtkinter.CTkButton(master=root, text="Breed Plants",
                                       command=breed_hundred_plants)
breed_button.place(relx=0.32, rely=0.39)


def disable_breed_button():
    breed_button.configure(state="disabled")


outcome_box = customtkinter.CTkTextbox(master=root, width=600, height=300)
outcome_box.place(relx=0.5, rely=0.7, anchor=CENTER)

reset_button = customtkinter.CTkButton(master=root, text="Reset",
                                       command=reset_all)
reset_button.place(relx=.52, rely=.39)

if __name__ == "__main__":
    root.mainloop()
