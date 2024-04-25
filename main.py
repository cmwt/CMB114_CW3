import tkinter as tk
from tkinter import ttk

# ***** Initiate Root Window + Labels *****

root = tk.Tk()

root.geometry("400x350")
root.title("Scientific Unit Converter - CW3")

intro = tk.Label(text = "Scientific Unit Converter")
intro.pack(pady=10)

type_label = tk.Label(text = "Select a unit type")
type_label.pack(pady=10)

unit_label = tk.Label(text = "Select the units between which you would \nlike to convert.")

from_label = tk.Label(text="From:")
to_label = tk.Label(text= "To:")

# ***** Set Lists for Dropdowns *****

# Creating a list of unit types
unit_types = [ 
 
    "Length",
    "Time",
    "Volume",
    "Pressure",
    "Energy"
]

# Creating lists of units for their respecitve measure

length_units = [
    
    "Meter",
    "Centimeter",
    "Millimeter",
    "Micrometer",
    "Nanometer",
    "Picometer",
    "Femtometer",
    "Attometer",
    "Angstrom"
]

time_units = [
    
    "Second",
    "Millisecond",
    "Nanosecond",
    "Picosecond",
    "Femtosecond",
    "Minutes",
    "Hours"
]

vol_units = [
    
    "Cubic Centimeters",
    "Cubic Decimeters",
    "Cubic Meters",
    "Millilitres",
    "Centilitres",
    "Litres"
    
]

pressure_units = [

    "Pa",
    "kPa",
    "Atm",
    "Bar",
    "Torr",
    "PSI"
]

energy_units = [
    
    "Joules",
    "Kilojoules",
    "Kilocalories",
    
]

# ***** Function to auto-select corect units for unit type selected *****

def pick_option (e): # Event to bind to dropdown to select correct list
    if type_combo.get() == "Length":
        unit_combo.config(value= length_units)
        unit_combo1.config(value= length_units)
    if type_combo.get() == "Time":
        unit_combo.config(value= time_units)
        unit_combo1.config(value= time_units)
    if type_combo.get() == "Volume":
        unit_combo.config(value= vol_units)
        unit_combo1.config(value= vol_units)
    if type_combo.get() == "Pressure":
        unit_combo.config(value= pressure_units)
        unit_combo1.config(value= pressure_units)
    if type_combo.get() == "Energy":
        unit_combo.config(value= energy_units)
        unit_combo1.config(value= energy_units)
        
# ***** Sets dropdpown menus *****

type_combo = ttk.Combobox(root, value = unit_types)
type_combo.pack(pady=2)
type_combo.bind("<<ComboboxSelected>>", pick_option)

unit_label.pack(pady=2)

from_label.pack(pady=1)

unit_combo = ttk.Combobox(root, value = [" "])
unit_combo.pack(pady=5)

to_label.pack(pady=1)

unit_combo1 = ttk.Combobox(root, value = [" "])
unit_combo1.pack(pady=5)

# ***** Create Entry for Converter Input *****

#entry = tk.Entry()
#entry.pack()

# ***** Calculate Button *****

#calculate = tk.Button(
    #text = "Calculate", 
    #width = "10", 
    #height = "2", 
    #)
#calculate.pack()

root.mainloop()
