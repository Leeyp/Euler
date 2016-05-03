# define function to generate Collatz sequences
def Collatz(number):
    counter = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            counter += 1
        else:
            number = (3*number) + 1
            counter += 1
    return counter


# define and initialise variables
highest = 0
starting = 0

# find the largest Collatz sequence with starting number under 1 million:
for x in range(1,1000000):
    num = Collatz(x)
    # if the length of Collatz sequence is found to be the highest, record it as well as its starting number
    if num > highest:
        highest = num
        starting = x
        


print(starting)
