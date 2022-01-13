# Write a function named checkDuplicates that receives three numbers as parameters and returns
# True if at least two numbers are duplicates.
# False if there are no two duplicate numbers

def checkDuplicates(num1, num2, num3):
    counter = 0

    if (num1 == num2):
        counter += 1

    if (num1 == num3):
        counter += 1

    if (num2 == num3):
        counter += 1

    if (counter >= 1):
        return True
    else:
        return False
