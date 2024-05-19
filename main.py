import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from lib.units import *
from lib.quantum import *
import os
from PIL import Image, ImageTk

# *******************
# *                 *
# *    Functions    *
# *                 *
# *******************

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

def displaytext(x):
    example_label.config(text = text.get(x))

def clear():
    output.delete(0, tk.END)
#this clears the output label for the unit converter

def clear_quant():
    calculation_label.configure(text="")
#this clears the output label for the quantum calculator
# Setting out the root window

root = tk.Tk()
root.geometry("800x500")
root.title("Scientific Unit Converter - CW3")
root.configure(bg="#f0f0f0")

# Applying styles
#ttk.style is a class that can be used to have consistent
#visual elements to all of the widgets
style = ttk.Style()
#these define the style which will be used for all 
style.configure("TLabel", font=("Helvetica", 10), background="#f0f0f0")
style.configure("TButton", font=("Helvetica", 10))
style.configure("TCombobox", font=("Helvetica", 10))
style.configure("TEntry", font=("Helvetica", 10))

notebook_1 = ttk.Notebook(root)
notebook_1.pack(fill="both", expand=1)

tabframe1 = tk.Frame(notebook_1, bg="#f0f0f0")
tabframe2 = tk.Frame(notebook_1, bg="#f0f0f0")
tabframe1.pack(fill="both", expand=1)
tabframe2.pack(fill="both", expand=1)

notebook_1.add(tabframe1, text="Unit Converter")
notebook_1.add(tabframe2, text="Quantum Calculator")

# ******************************************
# *                                        *
# *  Setting out the "Unit Converter" tab  *
# *                                        *
# ******************************************

leftframe = tk.Frame(tabframe1, bg="#f0f0f0")
leftframe.pack(side=tk.LEFT, padx=20, pady=20)
rightframe = tk.Frame(tabframe1, bg="#f0f0f0")
rightframe.pack(side=tk.RIGHT, padx=20, pady=20)

intro = ttk.Label(leftframe, text="Scientific Unit Converter", font=("Helvetica", 16))
intro.grid(row=0, column=0, columnspan=2, pady=10)

type_label = ttk.Label(leftframe, text="Select a unit type:")
type_label.grid(row=1, column=0, pady=5, sticky="e")

type_combo = ttk.Combobox(leftframe, value=unit_types, width=25)
type_combo.grid(row=1, column=1, pady=5, sticky="w")
type_combo.bind("<<ComboboxSelected>>", pick_option)

unit_label = ttk.Label(leftframe, text="Select the units between which you would like to convert:")
unit_label.grid(row=2, column=0, columnspan=2, pady=5)

from_label = ttk.Label(leftframe, text="From:")
from_label.grid(row=3, column=0, pady=5, sticky="e")

unit_combo = ttk.Combobox(leftframe, value=[" "], width=25)
unit_combo.grid(row=3, column=1, pady=5, sticky="w")

to_label = ttk.Label(leftframe, text="To:")
to_label.grid(row=4, column=0, pady=5, sticky="e")

unit_combo1 = ttk.Combobox(leftframe, value=[" "], width=25)
unit_combo1.grid(row=4, column=1, pady=5, sticky="w")

entry_label = ttk.Label(leftframe, text="Enter value:")
entry_label.grid(row=5, column=0, pady=5, sticky="e")

user_input_box = ttk.Entry(leftframe, width=27)
user_input_box.grid(row=5, column=1, pady=5, sticky="w")

output = ttk.Entry(rightframe, width=40)
output.pack(pady=10)

clear_but = ttk.Button(rightframe, text="Clear", command=clear)
clear_but.pack(pady=5)

# Load and resize the image for the calculate button using Pillow
directory = os.getcwd()
image_path = os.path.join(directory, "lib", "button_convert.png")
image = Image.open(image_path)
image = image.resize((100, 35), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

calculate = ttk.Button(
    leftframe,
    image=photo,
    command=lambda: [calculation(), displaytext(type_combo.get())]
)
calculate.grid(row=6, column=0, columnspan=2, pady=10)
calculate.image = photo

example_label = ttk.Label(rightframe)
example_label.pack(pady=10)

text = {
    "Length": "Reference Lengths:\nDiameter of a hydrogen atom ≈ 106pm\nCircumference of a football ≈ 70cm\nCircumference of the earth ≈ 40,075km",
    "Time": "Reference Times:\nBlink of an eye ≈ 100ms\nTime taken for light to travel from the Sun to the Earth ≈ 500s\nHalf life of uranium 235 ≈ 7e8 years",
    "Volume": "Reference Volumes:\nVolume of the Earth: 1.086 trillion km^3\nVolume of an average bathtub: 302 litres\nVolume of an average coffee: 240ml",
    "Pressure": "Reference Pressures:\nAverage tire pressure on a car: 33psi\nPressure to cause a diamond to break: 3000MPa\nPressure of the average boiler: 1.3 Bar",
    "Energy": "Reference Energies:\nEnergy released upon hydration of an alkene: 10kcal/mol\nEnergy released from the Fat Man bomb: 88 TJ\nCalories burnt on a 5K run: ~350kcal"
}

# **********************************************
# *                                            *
# *  Setting out the "Quantum Calculator" tab  *
# *                                            *
# **********************************************

properties_label = ttk.Label(tabframe2, text="Please select a property type and input its corresponding value in SI units.")
properties_label.pack(pady=10)

property_combo = ttk.Combobox(tabframe2, value=properties, width=40)
property_combo.pack(pady=10)

property_input = ttk.Entry(tabframe2, width=42)
property_input.pack(pady=10)

calculation_label = ttk.Label(tabframe2, text="")
calculation_label.pack(pady=10)

quant_calculate = ttk.Button(tabframe2,
                            image=photo,
                            command=lambda: [quantum_calc(property_input.get(), property_combo.get()), configure_label(calculation_label)])
quant_calculate.image = photo
quant_calculate.pack(pady=10)

quant_clear = ttk.Button(tabframe2, text="Clear", command=clear_quant)
quant_clear.pack(pady=5)

root.mainloop()
