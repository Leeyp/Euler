# create function d(n) to find the sum of proper divisors of n
def d(number):
    divisors = [1]
    for i in range(2, number):
        if i * i > number:
            break
        if i not in divisors:
            if number % i == 0:
                divisors.append(i)
                divisors.append(number // i)
    answer = 0
    for j in divisors:
        answer += j
    return answer

# define and initialise data structures
amicable = []

# define and initialise variables
amicablesum = 0

# main program to find sum of all amicable numbers under 10000
for a in range(1,10000):
    b = d(a)
    if a == b:
        continue
    else:
        if d(a) == b and d(b) == a:
            if a not in amicable:
                amicable.append(a)
            if b not in amicable:
                amicable.append(b)
        else:
            continue

# traverse array amicable, finding its sum
for i in amicable:
    amicablesum += i

# output
print(amicablesum)
