from tkinter import *
import customtkinter
from PIL import Image, ImageTk


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

height_button1 = customtkinter.CTkSegmentedButton(master=root, values=["Tall", "Short"])
height_button1.grid(row=1, column=5, pady=5, padx=10)
height_button2 = customtkinter.CTkSegmentedButton(master=root, values=["Tall","Short"])
height_button2.grid(row=2, column=5, pady=5, padx=10)

scent_button1 = customtkinter.CTkSegmentedButton(master=root, values=["Scent1", "Scent2"])
scent_button1.grid(row=1, column=6, pady=5, padx=10)
scent_button2 = customtkinter.CTkSegmentedButton(master=root, values=["Scent1", "Scent2"])
scent_button2.grid(row=2, column=6, pady=5, padx=10)

flower_button1 = customtkinter.CTkSegmentedButton(master=root, values=["Light", "Medium", "Heavy"])
flower_button1.grid(row=1, column=7, pady=5, padx=10)
flower_button2 = customtkinter.CTkSegmentedButton(master=root, values=["Light", "Medium", "Heavy"])
flower_button2.grid(row=2, column=7, pady=5, padx=10)

strain_button1 = customtkinter.CTkSegmentedButton(master=root, values=["Light", "Medium", "Heavy"])
strain_button1.grid(row=1, column=8, pady=5, padx=10)
strain_button2 = customtkinter.CTkSegmentedButton(master=root, values=["Light", "Medium", "Heavy"])
strain_button2.grid(row=2, column=8, pady=5, padx=10)





if __name__ == "__main__":
    root.mainloop()

