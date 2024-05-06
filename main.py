# *** Importing neccessary modules ***

import tkinter as tk
from tkinter import ttk
from tkinter import *


# *** Defining functions ***

# ***** Function to auto-select corect units for unit type selected *****
def pick_option(e): # Event to bind to dropdown to select correct list
    if type_combo.get() == "Length":
        unit_combo.config(values=list(length_units.keys()))
        unit_combo1.config(values=list(length_units.keys()))
    if type_combo.get() == "Time":
        unit_combo.config(value=list(time_units.keys()))
        unit_combo1.config(value=list(time_units.keys()))
    if type_combo.get() == "Volume":
        unit_combo.config(value=list(vol_units.keys()))
        unit_combo1.config(value=list(vol_units.keys()))
    if type_combo.get() == "Pressure":
        unit_combo.config(value=list(pressure_units.keys()))
        unit_combo1.config(value=list(pressure_units.keys()))
    if type_combo.get() == "Energy":
        unit_combo.config(value=list(energy_units.keys()))
        unit_combo1.config(value=list(energy_units.keys()))

# Calculation function to perform calculation and print answer to ouput entry
def calculation():
    value = user_input_box.get()
    value = float(value)
    if type_combo.get() == "Length":
        scale_factor = length_units.get(unit_combo.get())/length_units.get(unit_combo1.get())
        scale_factor = float(scale_factor)
    if type_combo.get() == "Time":
        scale_factor = time_units.get(unit_combo.get())/time_units.get(unit_combo1.get())
        scale_factor = float(scale_factor)
    if type_combo.get() == "Volume":
        scale_factor = vol_units.get(unit_combo.get())/vol_units.get(unit_combo1.get())
        scale_factor = float(scale_factor)
    if type_combo.get() == "Pressure":
        scale_factor = pressure_units.get(unit_combo.get())/pressure_units.get(unit_combo1.get())
        scale_factor = float(scale_factor)
    if type_combo.get() == "Energy":
        scale_factor = energy_units.get(unit_combo.get())/energy_units.get(unit_combo1.get())
        scale_factor = float(scale_factor)
    value = value * scale_factor
    output.insert(0, value)

# Prints reference text to a label above output entry
def displaytext(x):
    #print(text.get(x))
    example_label.config(text = text.get(x))

# Clears output entry ready for a new calculation
def clear():
    output.delete(0, END)

# Allows input entry to be placed relative to combobox
def get_combo_coords():
    coords_of_combox, coords_of_comboy = unit_combo.winfo_x(), unit_combo.winfo_y()
    print("Combo 1 coordinates:", coords_of_combox, coords_of_comboy)

    # Place the entry box relative to the combo box
    user_input_box.place(leftframe, x=coords_of_combox - 75, y=coords_of_comboy, width=50, height=20)
 
# *** Initiate Root Window + Labels ***

root = tk.Tk()
root.geometry("900x350")
root.title("Scientific Unit Converter - CW3")

# Left frame
leftframe = tk.Frame(root)
#leftframe.config(row=3, column=9)
leftframe.pack(side = LEFT)
# Right frame
rightframe = tk.Frame(root)
rightframe.pack(side = LEFT)


intro = tk.Label(leftframe,text="Scientific Unit Converter")
intro.grid(row=1, column=2)

type_label = tk.Label(leftframe,text="Select a unit type")
type_label.grid(row=2, column = 2)

##exaple text for the right frame
example_label = tk.Label(rightframe)
example_label.pack(padx = 100, pady= 0)

# *** Set Lists for Dropdowns ***

# Creating lists of units for their respecitve measure

unit_types = ["Length", "Time", "Volume", "Pressure", "Energy"]

length_units = {"Meter":1, "Centimeter":1e-2, "Millimeter":1e-3,
                "Micrometer":1e-6, "Nanometer":1e-9,
                "Picometer":1e-12, "Femtometer":1e-15,
                "Attometer":1e-18, "Angstrom":1e-10}
time_units = {"Second":1, "Millisecond":1e-3, "Nanosecond":1e-9, "Picosecond":1e-12, "Femtosecond":1e-15,
              "Minutes":60, "Hours":3600}
vol_units = {"Cubic Centimeters": 1, "Cubic Decimeters": 1e3, "Cubic Meters": 1e6,
             "Millilitres": 1, "Centilitres": 10, "Litres": 1e3}
pressure_units = {"Pa":1, "kPa":1e3, "Atm":101325, "Bar":1e5, "Torr":133.322, "PSI":6894.76}
energy_units = {"Joules":1, "Kilojoules":1e3, "Kilocalories":4184}

text = {"Length":"Reference Lengths:\n\
        Diameter of a hydrogen atom ≈ 106pm\n\
        Circumference of a football ≈ 70cm\n\
        Circumference of the earth ≈ 40,075m",
        "Time":"time text",
        "Volume":"volume text",
        "Pressure":"pressure text",
        "Energy":"energy text"}

# *** Sets dropdpown menus ***

type_combo = ttk.Combobox(leftframe, value=unit_types)
type_combo.grid(row=3, column=2)
type_combo.bind("<<ComboboxSelected>>", pick_option)
unit_label = tk.Label(leftframe, 
    text="Select the units between which you would \nlike to convert.")
unit_label.grid(row=4, column=2)

from_label = tk.Label(leftframe, text="From:")
from_label.grid(row=5, column=1)
unit_combo = ttk.Combobox(leftframe, value=[" "])
unit_combo.grid(row=6, column=1)

to_label = tk.Label(leftframe, text="To:")
to_label.grid(row=5, column=3)
unit_combo1 = ttk.Combobox(leftframe, value=[" "])
unit_combo1.grid(row=6, column = 3)

entry_label = tk.Label(leftframe, text="Entry")
entry_label.grid(row=7, column=2)
user_input_box = tk.Entry(leftframe)
user_input_box.grid(row=8, column=2)

output = tk.Entry(rightframe)
output.pack()

clear_but = tk.Button(rightframe, text="Clear", command=clear)
clear_but.pack(pady=5)


# Wait until the window is displayed to get the combo box coordinates
root.after(100, get_combo_coords)

calculate = tk.Button(
    leftframe,
    text="Calculate",
    width="10",
    height="2",
    command=lambda:[calculation(), displaytext(type_combo.get())]
)
calculate.grid(row=9, column=2)

root.mainloop()
