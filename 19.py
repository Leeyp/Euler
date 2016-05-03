# import necessary libraries
## may have to refer to official python documentation if you forget the libraries and commands!
import calendar
import datetime


# define and initialise variables
sundays = 0

# traverse the dates from 1901 to 2000
# remember that range should always be one extra, because it is exclusive of the latter value
for year in range(1901, 2001):
    for month in range(1, 13):
        
        # note that they want the Sundays on the FIRST of each month!
        date = datetime.date(year,month,1)
        if date.weekday() == 6:
            sundays += 1
        else:
            continue

# output
print(sundays)
