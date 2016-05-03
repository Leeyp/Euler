# define and initialise data structure
numbers = range(1,21)

# define and initialise variables
answer = 2520
alldivided = False

# determine if the number can be divided by numbers from 1 to 20
while alldivided == False:
    for x in numbers:
        if answer % x != 0:
            alldivided = False
            break
        else:
            alldivided = True
    # using mathematical concepts, numbers divisible from 11 to 20 need to first
    # be divisible by 1 to 10. So we increment by the LCM of 1 to 10 instead 
    if alldivided == False:
        answer += 2520
    else:
        print(answer)
        break
