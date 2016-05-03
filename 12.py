from math import sqrt

# define a function to determine number of divisors
def Divisors(number):
    if number == 1:
        return [1]
    else:
        storage = []
        for i in range(1,int(sqrt(number))+1):
            if number % i == 0:
                storage.append(i)
                if number // i != i:
                    storage.append(number // i)
    return storage

# define and initialise data structure
factors = [[1]]

while len(factors[-1]) <= 500:
    temp = 0
    for i in range(1,len(factors)):
        temp += i
    factors.append(Divisors(temp))

print(temp)


