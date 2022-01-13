# A Pythagorean triple consists of three positive integers. The sum of the square of any two integers is equal to the square of the third integer.

# For example: given a, b, and c:

# a^2 + b^2 = c^2
# a^2 + c^2 = b^2
# b^2 + c^2 = a^2

# Write a function named checkPythagoreanTriple that receives three numbers as parameters and returns:
# True, if the three numbers represent a Pythagorean triple.
# False, otherwise
# None, if any of the parameters is not a positive number

def checkPythagoreanTriple(a, b, c):

    if (a < 0 or b < 0 or c < 0):
        return None

    counter = 0

    if(a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2):
        counter += 1

    if(counter == 1):
        return True
    else:
        return False
