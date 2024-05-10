from lib.units import *

def opening_options():
    print("Welcome User to the CLI Unit Converter\n\
What unit type would you like to convert?")
    for i in range(len(unit_types)):
        print(f"{i+1}-{unit_types[i]}")
    print(f"{i+2}-About")
#this ensures that the user input is an integer and within the options
    while True:
        try:
            choice = int(input())
            if 0 < choice < 7:
                break
            else:
                print("Choose a value between 1 and 6")
            
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
    else:
        about()
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
