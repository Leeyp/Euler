# define function to determine prime numbers
def isPrime(n, primes):
    if n % 2 == 0:
        return False
    # since we have already calculated all the prime numbers
    # all factors must be prime
    # optimise code by not having to repeat the search for factors
    # i thought of this myself
    for number in primes:
        if n % number == 0:
            return False
        if number * number > n:
            return True
    return True

# define and initialise data structure
primes = [2,3]

# define and initialise variables
answer = 5
number = 3

# find all the primes under 2 million, incrementing by 2 because only odd numbers are prime
while number < 2000000:
    number += 2
    if isPrime(number, primes):
        primes.append(number)
        answer += number
    else:
        continue
    
print(answer)
