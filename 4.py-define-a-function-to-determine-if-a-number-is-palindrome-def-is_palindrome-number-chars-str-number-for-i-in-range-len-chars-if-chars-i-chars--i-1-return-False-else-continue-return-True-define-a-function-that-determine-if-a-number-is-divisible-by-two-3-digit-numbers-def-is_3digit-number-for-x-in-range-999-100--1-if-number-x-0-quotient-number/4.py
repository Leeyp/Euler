# define a function to determine if a number is palindrome
def is_palindrome(number):
    chars = str(number)
    for i in range(len(chars)):
        if chars[i] != chars[-i-1]:
            return False
        else:
            continue
    return True

# define a function that determine if a number is divisible by two 3-digit numbers
def is_3digit(number):
    for x in range(999,100,-1):
        if number % x == 0:
            quotient = number // x
            if 999 > quotient > 100:
                return True
    return False

# the largest number made from 3 digit numbers is less than 998001
# search for the greatest palindrome
palindrome = 998001
while palindrome > 0:
    if is_palindrome(palindrome):
        if is_3digit(palindrome):
            print(palindrome)
            break
        else:
            palindrome -= 1
    else:
        palindrome -= 1
