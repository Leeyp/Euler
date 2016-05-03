# define and initialise variables
factorial = 1
answer = 0

# obtain the factorial of 100; i.e. 100!
for i in range(1,101):
    factorial *= i

# convert the factorial into a string for easy manipulation of digits
factorial = str(factorial)

# sum every digit of the factorial into the answer
for i in range(len(factorial)):
    answer += int(factorial[i])

# output
print(answer)
