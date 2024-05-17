"""
In this file, all of the constants that are required
for the quantum calculations can be found alongside the
functions used to calculate corresponding properties.
Properties list
"""

properties = ["Time (s)", "Frequency (Hz)",
              "Energy (J)", "Wavelength (m)",
              "Wavenumber (m⁻¹)"]

# Constants

h = 6.626e-34 # Planck constant (Js)
c = 2.997e8 # Speed of light (m/s)
e = 1.602e-19 # Unit charge (C)
k = 1.381e-23 # Boltzmann constant (J/K)
N = 6.022e23 # Avogadro's constant (mol^-1)
F = 96485 # Faraday constant (C mol^-1)
R = 8.314 # Ideal gas constant (JK^-1mol^-1)

def quantum_calc(val, choice):
    global calculation_label, v, lam, wvn, t, energy, a
    a = choice
    val = float(val)
    if choice == "Energy (J)":
        energy_val = val
        v = energy_val / h 
        lam = c/v                                       
        wvn = 1/lam
        t = 1/v         
    elif choice == "Time (s)":
        time_val = val
        v = 1/time_val
        energy = v*h
        lam = c/v
        wvn = 1/lam
    elif choice == "Frequency (Hz)":
        freq_val = val
        t = 1/freq_val
        energy = h*freq_val
        lam = c/freq_val
        wvn = 1/lam
    elif choice == "Wavelength (m)":
        lam_val = val
        wvn = 1/lam_val
        v = c/lam_val
        energy = h*v
        t = 1/v
    elif choice == "Wavenumber (m^-1)":
        wvn_val = val
        lam = 1/wvn_val
        v = c/lam
        energy = h*v
        t = 1/v
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
