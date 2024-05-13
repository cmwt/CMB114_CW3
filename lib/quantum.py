# In this file, all of the constants that are required
# for the quantum calculations can be found alongside the
# functions used to calculate corresponding properties.

# Properties list

properties = ["Time (s)", "Frequency (Hz)",
              "Energy (J)", "Wavelength (m)",
              "Wavenumber (m^-1)"]
t = ""
v = ""
energy = ""
lam = ""
wvn = ""

# Constants

h = 6.626e-34 # Planck constant (Js)
c = 2.997e8 # Speed of light (m/s)
e = 1.602e-19 # Unit charge (C)
k = 1.381e-23 # Boltzmann constant (J/K)
N = 6.022e23 # Avogadro's constant (mol^-1)
F = 96485 # Faraday constant (C mol^-1)
R = 8.314 # Ideal gas constant (JK^-1mol^-1)

def quantum_calc():
    if property_combo.get() == "Energy (J)":
        energy_val = property_input.get()
        energy_val/h = v
        print(v) # can later apply this to print to an output
        c/v = lam
        print(lam) # can later apply this to print to an output
        1/lam = wvn
        print(wvn) # can later apply this to print to an output
        1/v = t        
        print(t) # can later apply this to print to an output
    if property_combo.get() == "Time (s)":
        time_val = property_input.get()
        v = 1/time_val
        print(v) # can later apply this to print to an output
        energy = v*h
        print(energy) # can later apply this to print to an output
        lam = c/v
        print(lam) # can later apply this to print to an output
        wvn = 1/lam
        print(wvn) # can later apply this to print to an output
    if property_combo.get() == "Frequency (Hz)":
        freq_val = property_input.get()
        t = 1/freq_val
        print(t) # can later apply this to print to an output
        energy = h*freq_val
        print(energy) # can later apply this to print to an output
        lam = c/freq_val
        print(lam) # can later apply this to print to an output
        wvn = 1/lam
        print(lam) # can later apply this to print to an output
    if property_combo.get() == "Wavelength (m)":
        lam_val = property_input.get()
        wvn = 1/lam_val
        print(wvn) # can later apply this to print to an output
        v = c/lam_val
        print(v) # can later apply this to print to an output
        energy = h*v
        print(energy) # can later apply this to print to an output
        t = 1/v
        print(t) # can later apply this to print to an output
    if property_combo.get() == "Wavenumber (m^-1)":
        wvn_val = property_input.get()
        lam = 1/wvn_val
        print(lam) # can later apply this to print to an output
        v = c/lam
        print(v) # can later apply this to print to an output
        energy = h*v
        print(energy) # can later apply this to print to an output
        t = 1/v
        print(t) # can later apply this to print to an output
