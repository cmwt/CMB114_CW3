import tkinter as tk
from tkinter import ttk
from tkinter import *
from lib.units import *
from lib.quantum import *

# *** Functions ***

# Function to auto-select corect units for unit type selected
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
    try:
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
    except ValueError:
        output.insert(0, "Invalid. Enter a number.")

# Prints reference text to a label above output entry
def displaytext(x):
    example_label.config(text = text.get(x))

# Clears output entry ready for a new calculation
def clear():
    output.delete(0, END)

# Setting out the root window

root = tk.Tk()
root.geometry("800x450")
root.title("Scientific Unit Converter - CW3")

notebook_1 = ttk.Notebook(root) # Notebook allows for separate tabs, breaking up the GUI
notebook_1.pack(fill="both", expand=1)

tabframe1 = tk.Frame(notebook_1)
tabframe2 = tk.Frame(notebook_1)
tabframe1.pack(fill="both", expand=1)
tabframe2.pack(fill="both", expand=1)

notebook_1.add(tabframe1, text="Unit Converter")
notebook_1.add(tabframe2, text="Quantum Calculator")

# ******************************************
# *                                        *
# *  Setting out the "Unit Converter" tab  *
# *                                        *
# ******************************************

leftframe = tk.Frame(tabframe1)
leftframe.pack(side = TOP)
rightframe = tk.Frame(tabframe1)
rightframe.pack(side = TOP)

intro = tk.Label(leftframe,text="Scientific Unit Converter")
intro.grid(row=1, column=2, pady=10)

type_label = tk.Label(leftframe,text="Select a unit type")
type_label.grid(row=2, column = 2)

# *** Widgets for "Unit Converter" ***

type_combo = ttk.Combobox(leftframe, value=unit_types)
type_combo.grid(row=3, column=2)
type_combo.bind("<<ComboboxSelected>>", pick_option)
unit_label = tk.Label(leftframe, 
    text="Select the units between which you would \nlike to convert.")
unit_label.grid(row=4, column=2, pady=5)

from_label = tk.Label(leftframe, text="From:")
from_label.grid(row=5, column=1)
unit_combo = ttk.Combobox(leftframe, value=[" "])
unit_combo.grid(row=6, column=1)

to_label = tk.Label(leftframe, text="To:")
to_label.grid(row=5, column=3)
unit_combo1 = ttk.Combobox(leftframe, value=[" "])
unit_combo1.grid(row=6, column = 3)

entry_label = tk.Label(leftframe, text="Enter a number")
entry_label.grid(row=7, column=2)
user_input_box = tk.Entry(leftframe)
user_input_box.grid(row=8, column=2)

output = tk.Entry(rightframe)
output.pack()

clear_but = tk.Button(rightframe, text="Clear", command=clear)
clear_but.pack(pady=5)

calculate = tk.Button(
    leftframe,
    text="Convert",
    width="10",
    height="2",
    command=lambda:[calculation(), displaytext(type_combo.get())]
)
calculate.grid(row=9, column=2, pady=5)

# Example text for the right frame
example_label = tk.Label(rightframe)
example_label.pack(padx = 100, pady= 0)

text = {"Length":"Reference Lengths:\n\
        Diameter of a hydrogen atom ≈ 106pm\n\
        Circumference of a football ≈ 70cm\n\
        Circumference of the earth ≈ 40,075km",
        "Time":"Reference Times:\n\
        Blink of an eye ≈ 100ms\n\
        Time taken for light to travel from the Sun to the Earth ≈ 500s\n\
        Half life of uranium 235 ≈ 7e8 years\n",
        "Volume":"volume text",
        "Pressure":"pressure text",
        "Energy":"energy text"}

# **********************************************
# *                                            *
# *  Setting out the "Quantum Calculator" tab  *
# *                                            *
# **********************************************

properties_label = tk.Label(tabframe2, text="Please select a property type and input its corresponding\n"
                            "value in SI units.")
properties_label.pack(pady=10)

property_combo = ttk.Combobox(tabframe2, value=properties)
property_combo.pack(pady=10)

property_input = tk.Entry(tabframe2)
property_input.pack(pady=10)

quant_calculate = tk.Button(tabframe2,
                            text="Calculate",
                            command=lambda:[])
quant_calculate.pack(pady=10)

root.mainloop()
