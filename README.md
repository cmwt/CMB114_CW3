# Introduction

Within this repository is the paired coursework content for Felix Plasser's CMB114 CW3 project.
The students working in this repository are William Thomas (F223975) and Oliver Rhodes (F228544). 

Our programme is a simple graphical user-interface (GUI) application, with a command line interface (CLI) counterpart, that has the 
ability to convert between a selection of SI and non-SI units that relate to the field of Chemistry and Physics.

# Running Unit Converter

The user will need to install the latest version of Python on their computer. The python download links can be found at:

https://www.python.org/downloads/

In order to run the Unit Converter, the user should clone this repository to their local machine using Git CMD,
download available from the following link:

https://git-scm.com/downloads

Once this has downloaded, open Git CMD, navigate to the directory within which the user would like to clone 
the repository then run:

`git clone https://github.com/cmwt/CMB114_CW3.git`

To run the GUI, navigate to the CMB114_CW3 directory that has just been cloned in and type:

`python main.py`

If the user would like to run the CLI version, type:

`python main_cli.py`

# Guide to Unit Converter

There are two sections to the Unit Converter GUI, a simple unit converter, and a quantum calculator. 

Within the 'Unit Converter' tab, the user can select the unit type for which they would like to run a conversion for and then set which units they would like to convert between. The 'Convert' button then outputs the converted value in an entry, and prints some reference measurements for each of the unit types to provide some real-world context to the user, for the conversions they are running. 

The 'Quantum Calculator' tab allows the user to input a quantum property and the 'Calculate' button will output the associated quantum properties such as energy, wavelength, etc. 
This can be used in conjunction with the unit converter to assist the user with any calculations they have to do when working in the field of quantum chemistry. 

The CLI version of the application has the same functionality, the difference being the user has to run it from Command Prompt (on Windows), Terminal (on MacOS or Linux).

# Tutorials and Testing

For information regarding specific tutorials of the features of this application and the testing of the software, please see the 'CMB114_CW3_Tutorials_and_Testing.docx' file in the 'docs' directory. 
