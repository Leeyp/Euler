# define a function to determine if a number is prime
def is_prime(number):
    for i in range(2,number):
        if i * i > number:
            break
        if number % i == 0:
            return False
    return True

# define and initialise data structure
factors = []

# define and initialise variables
target = 600851475143
largest = 0
divisor = 2
answer = 0

# find the prime factors of 600851475143
while target != 0:
    if divisor ** 2 > target:
        break
    if target % divisor == 0:
        if is_prime(divisor):
            factors.append(divisor)
            target // divisor
        else:
            target // divisor
    divisor += 1

# traverse array factors, finding the largest prime factor
for x in factors:
    if x > largest:
        largest = x

#output
print(largest)
