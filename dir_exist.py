#from __future__ import print_function
import os  # Import the OS Module
import sys


def main():
    input_func = input          # otherwise use 'raw_input'

    CheckDir = input_func("Enter the name of the directory to check : ")
    print()

    if os.path.exists(CheckDir):  # Checks if the dir exists
        print("The directory exists")
    else:
        print("No directory found for " + CheckDir)  # Output if no directory
        print()
        os.makedirs(CheckDir)  # Creates a new dir for the given name
        print("Directory created for " + CheckDir)


if __name__ == '__main__':
    main()