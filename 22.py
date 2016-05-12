# import necessary libraries
import csv

# define and initialise data structure
namelist = []

# input
with open("names.txt", "r") as infile:
    names = csv.reader(infile, delimiter = ",")
    for i in names:
        namelist = i


namelist = sorted(namelist, key=str.upper)
print(namelist)
