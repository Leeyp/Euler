# define necessary import libraries
from itertools import count, islice

# define function to determine prime numbers
def isPrime(n):
    if n < 2: return False
    for number in islice(count(2), 9999999):
        if not n%number:
            return number
    return False

# define and initialise variables
prime = 2
number = 3

# find the 10001st prime number, incrementing by 2 because only odd numbers are prime
while prime != 10001:
    number += 2
    if isPrime(number) == number:
        prime += 1
    else:
        continue
    

print(number)
    


