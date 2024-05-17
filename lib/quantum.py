"""
In this file, all of the constants that are required
for the quantum calculations can be found alongside the
functions used to calculate corresponding properties.
Properties list
"""

properties = ["Time (s)", "Frequency (Hz)",
              "Energy (J)", "Wavelength (m)",
              "Wavenumber (m^-1)"]

# Constants

h = 6.626e-34 # Planck constant (Js)
c = 2.997e8 # Speed of light (m/s)
e = 1.602e-19 # Unit charge (C)
k = 1.381e-23 # Boltzmann constant (J/K)
N = 6.022e23 # Avogadro's constant (mol^-1)
F = 96485 # Faraday constant (C mol^-1)
R = 8.314 # Ideal gas constant (JK^-1mol^-1)

def quantum_calc(val,choice):
    global calculation_label, v, lam, wvn, t, energy, a
    a = choice
    if choice == "Energy (J)":
        val = int(val)
        energy_val = val
        v = energy_val / h 
        print(v) # can later apply this to print to an output
        lam = c/v                                       
        print(lam) # can later apply this to print to an output
        wvn = 1/lam
        print(wvn) # can later apply this to print to an output
        t = 1/v         
        print(t) # can later apply this to print to an output
        #calculation_label.configure(text = f"{v}\n{lam}\n{wvn}\n{t}")
    elif choice == "Time (s)":
        val = int(val)
        time_val = val
        v = 1/time_val
        print(v) # can later apply this to print to an output
        energy = v*h
        print(energy) # can later apply this to print to an output
        lam = c/v
        print(lam) # can later apply this to print to an output
        wvn = 1/lam
        print(wvn) # can later apply this to print to an output
    elif choice == "Frequency (Hz)":
        val = int(val)
        freq_val = val
        t = 1/freq_val
        print(t) # can later apply this to print to an output
        energy = h*freq_val
        print(energy) # can later apply this to print to an output
        lam = c/freq_val
        print(lam) # can later apply this to print to an output
        wvn = 1/lam
        print(wvn) # can later apply this to print to an output
    elif choice == "Wavelength (m)":
        val = int(val)
        lam_val = val
        wvn = 1/lam_val
        print(wvn) # can later apply this to print to an output
        v = c/lam_val
        print(v) # can later apply this to print to an output
        energy = h*v
        print(energy) # can later apply this to print to an output
        t = 1/v
        print(t) # can later apply this to print to an output
    elif choice == "Wavenumber (m^-1)":
        val = int(val)
        wvn_val = val
        lam = 1/wvn_val
        print(lam) # can later apply this to print to an output
        v = c/lam
        print(v) # can later apply this to print to an output
        energy = h*v
        print(energy) # can later apply this to print to an output
        t = 1/v
        print(t) # can later apply this to print to an output
    else:
        print("error")
def configure_label(label):
    global v, lam, wvn, t, energy, a
    if a == "Energy (J)":
        label.config(text=f"Frequency: {v}Hz\nWavelength: {lam}m\nWavenumber: {wvn}cm^-1\nTime: {t}s")
    elif a == "Time (s)":
        label.config(text=f"Frequency: {v}Hz\nEnergy: {energy}J\nWavenumber: {wvn}cm^-1\nWavelength: {lam}m")
    elif a == "Frequency (Hz)":
        label.config(text=f"Time: {t}s\nEnergy: {energy}J\nWavenumber: {wvn}cm^-1\nWavelength: {lam}m")
    elif a == "Wavelength (m)":
        label.config(text=f"Wavenumber: {wvn}cm^-1\nFrequency: {v}Hz\nEnergy: {energy}J\nTime: {t}s")
    elif a == "Wavenumber (m^-1)":
        label.config(text=f"Frequency: {v}Hz\nWavelength: {lam}m\nEnergy: {energy}J\nTime: {t}s")


#e  prints v,lam,wvn,t
#t  prints v,energy,wvn,lam
#f  prints t,energy,wvn,lam
#w  prints wvn,v,energy,t
#wn prints lam,v,energy,t
