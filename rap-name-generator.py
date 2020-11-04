# Guided Exploration No. 3
# Tyler Bradshaw

# Imports the random library
import random

# Empty list
possible_names = []

# Create a text file to store the rap-names and write to it
outputFile = open('rap-names-output.txt', 'w')

# Opens the rap-names text file for read and assigns it to "datafile"
with open('rap-names.txt', 'r') as dataFile:
    # for loop too iterate through the names in the "datafile"
    for name in dataFile:
        # appends the names to our list with all the blank space to the right stripped off
        possible_names.append(name.rstrip())

# User input to determine how many names will be created
count = int(input('How many rap names would you like to create? '))
# user input to determine how many parts the rap- name should have
parts = int(input('How many parts should the name contain? '))

# for loop from the user input count to loop that many times to create diffrent names
for i in range(count):
    # blank list where the random rap-name parts will be stored
    name_parts = []
    # for loop too iterate the number from parts variable
    for j in range(parts):
        # this will append a random name from the possible_names list and append that too name_parts the amount of times you inputted for the variable parts
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])

    # writes the name_parts list as a string within the rap-names-output.txt file opened earlier
    outputFile.write(f"{' '.join(name_parts)}\n")
    # prints the name_parts list as a string using f string formatting
    print(f"{' '.join(name_parts)}")

# closes the output file opened earlier
outputFile.close()
