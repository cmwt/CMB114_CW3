"""
This file contains the list for the unit types dropdown menu along with
all of the scale factors for the unit conversions in the unit converter tab
of the GUI
"""

unit_types = ["Length", "Time", "Volume", "Pressure", "Energy"]

length_units = {"Meters (m)":1, "Centimeters (cm)":1e-2, "Millimeters (mm)":1e-3,
                "Micrometers (μm)":1e-6, "Nanometers (nm)":1e-9,
                "Picometers (pm)":1e-12, "Femtometers (fm)":1e-15,
                "Attometers (am)":1e-18, "Angstroms (Å)":1e-10}
time_units = {"Seconds (s)":1, "Milliseconds (ms)":1e-3, "Nanoseconds (ns)":1e-9,
              "Picoseconds (ps)":1e-12, "Femtoseconds (fs)":1e-15,
              "Minutes (min)":60, "Hours (hr)":3600}
vol_units = {"Cubic Centimeters (cm³)": 1, "Cubic Decimeters (dm³)": 1e3,
             "Cubic Meters (m³)": 1e6,
             "Millilitres (ml)": 1, "Centilitres (cl)": 10, "Litres (l)": 1e3}
pressure_units = {"Pascals (Pa)":1, "Kilopascals (kPa)":1e3, "Atmospheres (Atm)":101325,
                  "Bar":1e5, "Torr":133.322, "Pounds per square Inch (PSI)":6894.76}
energy_units = {"Joule (J)":1, "Kilojoules (kJ)":1e3, "Kilocalories (kcal)":4184,
                "Electron-volts (eV)":1.60218e-19, "Hartree (Eh)": 4.35974e-18}
