# define and initialise data structure
numbers = range(1,101)

# define and initialise variables
sumsquares = 0
squaresum = 0

# determine sumsquares
for i in numbers:
    sumsquares += i * i

# determine squaresum
for i in numbers:
    squaresum += i
squaresum = squaresum ** 2

# output
if sumsquares > squaresum:
    print(sumsquares - squaresum)
else:
    print(squaresum - sumsquares)


