# define and initialise data structure
numbers = []

# define and initialise variables
answer = 0

# traverse numbers 1 to 1000, inserting multiples of 3 or 5 into array numbers
for x in range(1000):
    if x % 3 == 0:
        if x not in numbers:
            numbers.append(x)
    elif x % 5 == 0:
        if x not in numbers:
            numbers.append(x)
    else:
        continue

# traverse array number to find its sum
for y in numbers:
    answer += y

#output
print(answer)
