# Your rich uncle is giving his son 1000000 in cash. Your father claims he loves you a lot but is only giving
# you pennies a day for 30 days. He will start giving you 1 penny and double the amount every day
# (i.e. 1 penny today, 2 pennies tomorrow, 4 pennies the next day, 8 pennies the next day, etc.).

# Write a Python function named isBetterDeal that does the following:
# (a) Finds the amount of money in dollars that you’ll receive at the end of the 30 days

# The function returns two values:
# (1) The amount computed in (a) (type: float)
# (2) Boolean value True if the amount computed in (a) is greater than 1000000, otherwise the value will be False.(type: boolean)

def isBetterDeal():
    amt_pennies = 0
    more = False

    for i in range(30):
        amt_pennies += 2**i

    if (amt_pennies > 1000000):
        more = True

    amt_pennies = amt_pennies/100

    return amt_pennies, more
