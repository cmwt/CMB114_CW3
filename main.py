import tkinter as tk
from tkinter import *

root = tk.Tk()

root.geometry("400x350")

intro = tk.Label(text = "Scientific Unit Converter")
intro.pack()

default_1 = tk.StringVar()
default_1.set("Choose a unit to convert from.")
left_dropdown = tk.OptionMenu(root, default_1, "Metre", "Centimetre", "Millimetre")
left_dropdown.pack()

default_2 = tk.StringVar()
default_2.set("Choose a unit to convert to.")
right_dropdown = tk.OptionMenu(root, default_2, "Metre", "Centimetre", "Millimetre")
right_dropdown.pack()

entry = tk.Entry()
entry.pack()

calculate = tk.Button(
    text = "Calculate", 
    width = "10", 
    height = "2", 
    )
calculate.pack()

root.mainloop()
