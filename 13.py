## author's comments: easier to read input from file! ##

# read input from file
try:
    inputfile = open("input.txt", "r")
    lines = inputfile.readlines()
except IOError:
    print("IOError.")
    
# define and initialise variables
answer = 0

# traverse the lines of the input file, finding the sum of the large numbers
for line in lines:
    answer += int(line)

# convert the answer to a string to obtain the first 10 digits
stringanswer = str(answer)

# output
print(stringanswer[0:10])

    
