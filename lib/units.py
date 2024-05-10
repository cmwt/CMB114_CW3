unit_types = ["Length", "Time", "Volume", "Pressure", "Energy"]

length_units = {"Meters":1, "Centimeters":1e-2, "Millimeters":1e-3,
                "Micrometers":1e-6, "Nanometers":1e-9,
                "Picometers":1e-12, "Femtometers":1e-15,
                "Attometers":1e-18, "Angstroms":1e-10}
time_units = {"Seconds":1, "Milliseconds":1e-3, "Nanoseconds":1e-9, "Picoseconds":1e-12, "Femtoseconds":1e-15,
              "Minutes":60, "Hours":3600}
vol_units = {"Cubic Centimeters": 1, "Cubic Decimeters": 1e3, "Cubic Meters": 1e6,
             "Millilitres": 1, "Centilitres": 10, "Litres": 1e3}
pressure_units = {"Pa":1, "kPa":1e3, "Atm":101325, "Bar":1e5, "Torr":133.322, "PSI":6894.76}
energy_units = {"Joule":1, "Kilojoules":1e3, "Kilocalories":4184} # kJ/mol, eV, Hartree
