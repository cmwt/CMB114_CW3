from lib.units import *
from lib.quantum import *


def opening_options():
    print("Welcome User to the CLI Unit Converter\n\
What unit type would you like to convert?")
    for i in range(len(unit_types)):
        print(f"{i+1}-{unit_types[i]}")
    print(f"{i+2}-Quantum Calculations\n{i+3}-About\n{i+4}-Exit")
#this ensures that the user input is an integer and within the options
    while True:
        try:
            choice = int(input())
            if 0 < choice < 9:
                break
            else:
                print("Choose a value between 1 and 8")
            
        except ValueError:
            print('You entered a non integer value, try again.')
            continue
    run_choice(choice)

def run_choice(x):
    global unit
#what unit we are converting to and from
    if x == 1:
        unit = length_units
    elif x == 2:
        unit = time_units
    elif x == 3:
        unit = vol_units
    elif x == 4:
        unit = pressure_units
    elif x == 5:
        unit = energy_units
    elif x ==6:
        property_type =  int(input("Please select a property type and input its corresponding value in SI units\
\n1-Time(s)\n2-Frequency(Hz)\n3-Energy(J)\n4-Wavelength(m)\n5-Wavenumber(m^-1)"))
        if 0 < property_type < 6: 
            quantum_calculator(property_type)
        else:
            print("invalid entry")
            run_choice(6)
    elif x ==7:
        about()
    else:
#this ends the python script and returns the user to the directory
        quit()
    print("These are the units which this Calculator can convert\nPick the starting unit below:")
    for i, unit_name in enumerate(unit, start=1):
        print(f"{i}-{unit_name}")
    print(f"{i+1}-Back to menu")

    # Ensure that the user input is an integer and within the options
    while True:
        try:
            starting_unit = int(input())
            if 1 <= starting_unit <= len(unit)+1:
                break
            else:
                print(f"Choose a value between 1 and {len(unit)+1}")
        except ValueError:
            print('You entered a non-integer value, try again.')
            continue
    if starting_unit == (i+1):
        opening_options()
    while True:
        try:
            input_value = int(input(f"What is the value in {list(unit)[starting_unit-1]}"))
            break
        except ValueError:
            print('You entered a non-integer value, try again.')
            continue
    print("What unit do you want to convert this to?")
    while True:
        try:
            end_unit = int(input())
            if 1 <= end_unit <= len(unit)+1:
                break
            else:
                print(f"Choose a value between 1 and {len(unit)+1}")
        except ValueError:
            print('You entered a non-integer value, try again.')
            continue
    if starting_unit == (i+1):
        opening_options()
#    print(list(unit)[starting_unit-1])#has the unit name as a string
#    print(list(unit)[end_unit-1])#has the unit name as a string
    conversion(starting_unit-1, end_unit-1,input_value)

def quantum_calculator(x):
    global unit
    val = int(input("Enter the value"))
    if x == 1:
        quantum_calc(val, "Time (s)")
    elif x == 2:
        quantum_calc(val, "Frequency (Hz)")
    elif x == 3:
        quantum_calc(val, "Energy (J)")
    elif x == 4:
        quantum_calc(val, "Wavelength (m)")
    elif x == 5:
        quantum_calc(val, "Wavenumber (m^-1)")
    
    print("\nReturning to the menu")
    opening_options()
        
    

def conversion(a,b,c):
    scale_factor = unit[list(unit)[a]]/unit[list(unit)[b]]
    print(f"Output value is:\n{c*scale_factor} {list(unit)[b]}")
#a - starting unit
#b - end unit
#c - value at the start
    # Call the function to perform the conversion based on the user's choice
    # Example: perform_conversion(x, starting_unit)
    opening_options()

        
def about():
    print("Simple Unit converter on the command line.\n\
Offers conversions for Length, Time, Volume, Pressure and Energy\n\
Created by:\n"+4*" ","Oliver Rhodes and Will Thomas\nReturning to menu\n")
    opening_options()
    
opening_options()
