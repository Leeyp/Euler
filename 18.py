## author's comments: easier to read input from file! ##

# read input from file
try:
    inputfile = open("input.txt", "r")
    lines = inputfile.readlines()
except IOError:
    print("IOError.")

# define and initialise data structure
triangle = []

# define and initialise variables
pointer = 0
answer = 0

# treat input data
for line in lines:
    triangle.append(line.rstrip().split(" "))


# working from the bottom up is the best way to solve this problem; invert the triangle
triangle = list(reversed(triangle))

# choose the greatest number between the two leaf nodes, and add this information to the parent node
for i in range(1,len(triangle)):
    for j in range(len(triangle[i])):
        if int(triangle[i-1][j]) > int(triangle[i-1][j+1]):
            triangle[i][j] = int(triangle[i-1][j]) + int(triangle[i][j])
        else:
            triangle[i][j] = int(triangle[i-1][j+1]) + int(triangle[i][j])

# output
print(triangle[-1])
