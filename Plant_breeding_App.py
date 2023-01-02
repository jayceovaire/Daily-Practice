import tkinter as tk

# Create the main window
window = tk.Tk()

# Create a frame to hold the radio buttons
frame = tk.Frame(window)

# Create a variable to hold the selected option
selected_option1 = tk.StringVar()
selected_option2 = tk.StringVar()
selected_option3 = tk.StringVar()
selected_option4 = tk.StringVar()
selected_option5 = tk.StringVar()
selected_option6 = tk.StringVar()
selected_option7 = tk.StringVar()
selected_option8 = tk.StringVar()
selected_option9 = tk.StringVar()
selected_option10 = tk.StringVar()
selected_option11 = tk.StringVar()
selected_option12 = tk.StringVar()

# Create the radio buttons
label1 = tk.Label(frame, text="Color")
label2 = tk.Label(frame, text="Height")
label3 = tk.Label(frame, text="Smell")
label4 = tk.Label(frame, text="Flower size")
label5 = tk.Label(frame, text="Strain")
option1 = tk.Radiobutton(frame, text='Green', variable=selected_option1, value='Option 1')
option2 = tk.Radiobutton(frame, text='Purple', variable=selected_option1, value='Option 2')
option3 = tk.Radiobutton(frame, text='Short', variable=selected_option2, value='Option 3')
option4 = tk.Radiobutton(frame, text='Tall', variable=selected_option2, value='Option 4')
option5 = tk.Radiobutton(frame, text='Sweet', variable=selected_option3, value='Option 5')
option6 = tk.Radiobutton(frame, text='Sour', variable=selected_option3, value='Option 6')
option7 = tk.Radiobutton(frame, text='Light', variable=selected_option4, value='Option 7')
option8 = tk.Radiobutton(frame, text='Medium', variable=selected_option4, value='Option 8')
option9 = tk.Radiobutton(frame, text='Heavy', variable=selected_option4, value='Option 9')
option10 = tk.Radiobutton(frame, text='Indica', variable=selected_option5, value='Option 10')
option11 = tk.Radiobutton(frame, text='Sativa', variable=selected_option5, value='Option 11')
option12 = tk.Radiobutton(frame, text='Hybrid', variable=selected_option5, value='Option 12')
# Pack the radio buttons into the frame
label1.grid(row=3, column=0)
option1.grid(row=3, column=1)
option2.grid(row=3, column=2)

label2.grid(row=4, column=0)
option3.grid(row=4, column=1)
option4.grid(row=4, column=2)

label3.grid(row=5, column=0)
option5.grid(row=5, column=1)
option6.grid(row=5, column=2)

label4.grid(row=6, column=0)
option7.grid(row=6, column=1)
option8.grid(row=6, column=2)
option9.grid(row=6, column=3
             )
label5.grid(row=7, column=0)
option10.grid(row=7, column=1)
option11.grid(row=7, column=2)
option12.grid(row=7, column=3)
# Pack the frame containing the radio buttons into the main window
frame.pack()

# Run the Tkinter event loop
window.mainloop()