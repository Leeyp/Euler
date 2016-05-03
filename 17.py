## seems like a tedious question! ##

# define and initialise data structures
# manually spell out the numbers
basic_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                 "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

# define and initialise variables
firstnineteen = 0
next80 = 0
answer = 0

# determine the number of letters in 1-19:
for x in basic_numbers:
    # to record the length of first nineteen numbers for easy retrieval
    firstnineteen += len(x)

answer += firstnineteen

# determine the number of letters in 20 - 99:
for x in range(20, 100):
    if x % 10 == 9:
        # to record the length of next 79 numbers for easy retrieval
        next80 += len(tens[(x // 10)-2])
    else:
        next80 += len(tens[(x // 10)-2])
        next80 += len(basic_numbers[x % 10])

answer += next80

# determine the number of letters in 100 - 999:
for x in range(100,1000):
    if x % 100 == 9:
        answer += len(basic_numbers[(x // 100)-1])
        answer += len("hundred")
    else:
        answer += len(basic_numbers[(x // 100)-1])
        answer += len("hundred")
        answer += len("and")

answer += (firstnineteen + next80) * 9

# add the length of "one thousand" to the final answer
answer += len("one")
answer += len("thousand")

#output
print(answer)
