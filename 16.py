# define and initialise variables
answer = 0
bignumber = 2 ** 1000

# convert bignumber into string for easy slicing of digits
stringnumber = str(bignumber)

# traverse each digit of the string, finding its sum
for x in range(len(stringnumber)):
    answer += int(stringnumber[x])

# output
print(answer)
