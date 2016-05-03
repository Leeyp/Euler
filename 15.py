# define and initialise variables
paths = 1

# using binomial theorem(!), find (n  r), where n is 20 
for x in range(20):
    paths *= (2 * 20) - x
    paths /= x + 1
    

print(paths)
    
