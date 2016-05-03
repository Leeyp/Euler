# define and initialise data structure
fibonacci = [1,2]

# define and initialise variables
pointer = 2
answer = 0

# traverse the fibonacci sequence, stopping at 4 million
while fibonacci[-1] < 4000000:
    fibonacci.append(fibonacci[pointer-1] + fibonacci[pointer-2])
    pointer += 1

# if the final element is above 4 million, ignore it
if fibonacci[-1] > 4000000:
    del fibonacci[-1]
    
# traverse array fibonacci to find the sum of its even terms
for y in fibonacci:
    if y % 2 == 0:
        answer += y

#output
print(answer)
