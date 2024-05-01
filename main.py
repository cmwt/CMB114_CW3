import tkinter as tk
from tkinter import ttk

# ***** Function to auto-select corect units for unit type selected *****
def pick_option(e): # Event to bind to dropdown to select correct list
    if type_combo.get() == "Length":
        unit_combo.config(value=length_units)
        unit_combo1.config(value=length_units)
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
    print("Text entry value:", value)
    
# ***** Initiate Root Window + Labels *****

root = tk.Tk()
root.geometry("400x350")
root.title("Scientific Unit Converter - CW3")

intro = tk.Label(text="Scientific Unit Converter")
intro.pack(pady=10)

type_label = tk.Label(text="Select a unit type")
type_label.pack(pady=10)


# ***** Set Lists for Dropdowns *****
# Creating lists of units for their respecitve measure

unit_types = ["Length", "Time", "Volume", "Pressure", "Energy"]

length_units = ["Meter", "Centimeter", "Millimeter", "Micrometer", "Nanometer",
                "Picometer", "Femtometer", "Attometer", "Angstrom"]
time_units = ["Second", "Millisecond", "Nanosecond", "Picosecond", "Femtosecond",
              "Minutes", "Hours"]
vol_units = ["Cubic Centimeters", "Cubic Decimeters", "Cubic Meters",
             "Millilitres", "Centilitres", "Litres"]
pressure_units = ["Pa", "kPa", "Atm", "Bar", "Torr", "PSI"]
energy_units = ["Joules", "Kilojoules", "Kilocalories"]

# ***** Sets dropdpown menus *****

type_combo = ttk.Combobox(root, value=unit_types)
type_combo.pack(pady=2)
type_combo.bind("<<ComboboxSelected>>", pick_option)
unit_label = tk.Label(
    text="Select the units between which you would \nlike to convert.")
unit_label.pack(pady=10)
from_label = tk.Label(text="From:")
from_label.pack(pady=1)
unit_combo = ttk.Combobox(root, value=[" "])
unit_combo.pack(pady=5)
to_label = tk.Label(text="To:")
to_label.pack(pady=1)

unit_combo1 = ttk.Combobox(root, value=[" "])
unit_combo1.pack(pady=5)

user_input_box = tk.Entry(root)
user_input_box.pack()

def get_combo_coords():
    coords_of_combox, coords_of_comboy = unit_combo.winfo_x(), unit_combo.winfo_y()
    print("Combo 1 coordinates:", coords_of_combox, coords_of_comboy)

    # Place the entry box relative to the combo box
    user_input_box.place(x=coords_of_combox - 75, y=coords_of_comboy, width=50, height=20)

# Wait until the window is displayed to get the combo box coordinates
root.after(100, get_combo_coords)

calculate = tk.Button(
    text="Calculate",
    width="10",
    height="2",
    command=calculation
)
calculate.pack(pady=10)

root.mainloop()
