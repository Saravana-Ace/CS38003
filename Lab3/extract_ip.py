# Information extraction is an important process in data science.
# In this exercise, you will write a function to check whether an
# ip address is valid. If it is valid, return True. Else, return
# False.
#
# An valid IP address is a 32-bit numeric address written as four
# decimal numbers separated by periods; each number can be written
# from 0 to 255 (0.0.0.0 to 255.255.255.255).
#
# Note: You need to use regular expressions to extract the addresses.

# Examples:
# (1) valid_ip("155.155.155.155")
# return True
# (2) valid_ip("155.155.155-155")
# return False
# (3) valid_ip("256.155.155.155")
# return False

import re


def valid_ip(IP):
    # p = re.compile("\d*[0-2]\d*[0-5]\d*[0-5][.]\d*[0-2]\d*[0-5]\d*[0-5][.]\d*[0-2]\d*[0-5]\d*[0-5][.]\d*[0-2]\d*[0-5]\d*[0-5]")
    # p = re.compile("\d*\d*\d*[.]\d*\d*\d*[.]\d*\d*\d*[.]\d*\d*\d*")

    p = re.compile("[0-2]{0,3}[0-5]{0,3}[0-5]{0,3}\.[0-2]{0,3}[0-5]{0,3}[0-5]{0,3}\.[0-2]{0,3}[0-5]{0,3}[0-5]{0,3}\.[0-2]{0,3}[0-5]{0,3}[0-5]{0,3}")

    if(p.match(IP)):
        return True
    else:
        return False

print(valid_ip("0.0.0.0"))
print(valid_ip("155.155.155-155"))
print(valid_ip("256.155.155.155"))
