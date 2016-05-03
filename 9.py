# import necessary libraries
from math import sqrt

# define and initialise variables
a = 3
b = 4

# define and initialise data structures
triplets = []

# define a function to determine if a and b form a Pythagorean triplet
def triplet(a,b):
    c = a ** 2 + b ** 2
    if sqrt(c).is_integer():
        return True
    else:
        return False

# increment a and b, trying to find valid pythagorean triplets
while a < 500:
    b = 4
    while b < 500:
        if triplet(a,b):
            triplets.append([a,b,int(sqrt(a ** 2 + b ** 2))])
        b += 1
    a += 1

# traverse the list of pythagorean triplets, finding the triplet that adds to 1000
for x in triplets:
    if x[0] + x[1] + x[2] == 1000:
        print(x[0] * x[1] * x[2])
                        
                      
    

