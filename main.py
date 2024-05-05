import tkinter as tk
from tkinter import ttk
from tkinter import *


# ***** Function to auto-select corect units for unit type selected *****
def pick_option(e): # Event to bind to dropdown to select correct list
    if type_combo.get() == "Length":
        unit_combo.config(values=list(length_units.keys()))
        unit_combo1.config(values=list(length_units.keys()))
    if type_combo.get() == "Time":
        unit_combo.config(value=time_units)
        unit_combo1.config(value=time_units)
    if type_combo.get() == "Volume":
        unit_combo.config(value=vol_units)
        unit_combo1.config(value=vol_units)
    if type_combo.get() == "Pressure":
        unit_combo.config(value=pressure_units)
        unit_combo1.config(value=pressure_units)
    if type_combo.get() == "Energy":
        unit_combo.config(value=energy_units)
        unit_combo1.config(value=energy_units)

#unfinished function for the calculation
def calculation():
    value = user_input_box.get()
    value = float(value)
    if type_combo.get() == "Length":
        scale_factor = length_units.get(unit_combo.get())/length_units.get(unit_combo1.get())
        scale_factor = float(scale_factor)
    value = value * scale_factor
    print(value)

def displaytext(x):
    #print(text.get(x))
    example_label.config(text = text.get(x))
# ***** Initiate Root Window + Labels *****

root = tk.Tk()
root.geometry("800x350")
root.title("Scientific Unit Converter - CW3")

##code for the left frame
leftframe = Frame(root, borderwidth = 2, relief = tk.GROOVE)
leftframe.pack(side = LEFT)
##code for the right frame
rightframe = Frame(root, borderwidth = 2, relief = tk.GROOVE)
rightframe.pack(side = RIGHT)


intro = tk.Label(leftframe,text="Scientific Unit Converter")
intro.pack(pady=10)

type_label = tk.Label(leftframe,text="Select a unit type")
type_label.pack(pady=10)

##exaple text for the right frame
example_label = tk.Label(rightframe)
example_label.pack(padx = 100, pady= 0)

# ***** Set Lists for Dropdowns *****
# Creating lists of units for their respecitve measure

unit_types = ["Length", "Time", "Volume", "Pressure", "Energy"]

length_units = {"Meter":1, "Centimeter":1e-2, "Millimeter":1e-3,
                "Micrometer":1e-6, "Nanometer":1e-9,
                "Picometer":1e-12, "Femtometer":1e-15,
                "Attometer":1e-18, "Angstrom":1e-10}
time_units = ["Second", "Millisecond", "Nanosecond", "Picosecond", "Femtosecond",
              "Minutes", "Hours"]
vol_units = ["Cubic Centimeters", "Cubic Decimeters", "Cubic Meters",
             "Millilitres", "Centilitres", "Litres"]
pressure_units = ["Pa", "kPa", "Atm", "Bar", "Torr", "PSI"]
energy_units = ["Joules", "Kilojoules", "Kilocalories"]

text = {"Length":"Reference Lengths:\n\
        Diameter of a hydrogen atom ≈ 106pm\n\
        Circumference of a football ≈ 70cm\n\
        Circumference of the earth ≈ 40,075m",
        "Time":"time text",
        "Volume":"volume text",
        "Pressure":"pressure text",
        "Energy":"energy text"}

# ***** Sets dropdpown menus *****

type_combo = ttk.Combobox(leftframe, value=unit_types)
type_combo.pack(padx = 100, pady=2)
type_combo.bind("<<ComboboxSelected>>", pick_option)
unit_label = tk.Label(leftframe, 
    text="Select the units between which you would \nlike to convert.")
unit_label.pack(pady=10)
from_label = tk.Label(leftframe, text="From:")
from_label.pack(pady=1)
unit_combo = ttk.Combobox(leftframe, value=[" "])
unit_combo.pack(pady=5)
to_label = tk.Label(leftframe, text="To:")
to_label.pack(pady=1)

unit_combo1 = ttk.Combobox(leftframe, value=[" "])
unit_combo1.pack(pady=5)

entry_label = tk.Label(leftframe, text="Entry")
entry_label.pack()
user_input_box = tk.Entry(leftframe)
user_input_box.pack()

def get_combo_coords():
    coords_of_combox, coords_of_comboy = unit_combo.winfo_x(), unit_combo.winfo_y()
    print("Combo 1 coordinates:", coords_of_combox, coords_of_comboy)

    # Place the entry box relative to the combo box
    user_input_box.place(leftframe, x=coords_of_combox - 75, y=coords_of_comboy, width=50, height=20)

# Wait until the window is displayed to get the combo box coordinates
root.after(100, get_combo_coords)

calculate = tk.Button(
    leftframe,
    text="Calculate",
    width="10",
    height="2",
    command=lambda:[calculation(), displaytext(type_combo.get())]
)
calculate.pack(pady=10)

root.mainloop()
