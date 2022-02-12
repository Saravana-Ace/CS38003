# These days usually passwords are required to be of at least a specific length, have some special characters etc.
# Write a function pswd_check(password) that takes a string, the password as input and decides if the password
#
# is at least 8-characters in length
# has both uppercase and lowercase letters
# has at least one of the following special characters: ~!@#$%^&*()
# has at least one number
# function pswd_check(password)
#
# Inputs: 1 input
#
# a string Outputs: 1 output
# returns True if the password entered fulfills all the four requirements, and False otherwise
# Examples
#
# pswd_check('BoilerUp!123') should return True
# pswd_check('boilerup!234') should return False (no uppercase letters)
# pswd_check('boilerUp123') should return False (no special characters)
# pswd_check('') should return False

import re

def pswd_check(password):

    lower = re.compile("[a-z]")
    upper = re.compile("[A-Z]")
    number = re.compile("\d")
    special = re.compile("[~!@#$%^&*()]")

    lowercase = False
    uppercase = False
    num = False
    special_char = False

    if(len(password) < 8):
        return False

    if(lower.search(password)):
        lowercase = True
    if(upper.search(password)):
        uppercase = True
    if(number.search(password)):
        num = True
    if(special.search(password)):
        special_char = True

    if(lowercase and uppercase and num and special_char):
        return True
    else:
        return False

print(pswd_check(''))
