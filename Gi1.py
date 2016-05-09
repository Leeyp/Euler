# define function to find prime numbers
def find_prime(number, primes):
    if number == 0:
        return False
    elif number == 1:
        return False
    elif number == 2:
        return True
    else:
        if number % 2 == 0:
            return False
        else:
            for i in primes:
                if number % i == 0:
                    return False
                if i * i > number:
                    break
            return True


# define and initialise data structures
primes = [2,3]

# define and initialise variables
input_number = int(input("Input your number."))
found = False

# determine the prime numbers from 2 to input_number
for i in range(input_number):
    if find_prime(i, primes):
        if i not in primes:
            primes.append(i)
    else:
        continue

# determine two prime numbers that add up to input_number
while found is False:
    for i in primes:
        for j in primes:
            if i + j == input_number:
                # output
                print(i,"+",j,"=",input_number)
                found = True
    if found is False:
        # output
        print("Not found.")
        break
                
