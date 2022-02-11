# A valid password nowadays generally requires to be of some length containing at least one lower case
# character, one upper case character, one digit and one special character (e.g., ?!@#$%^&*). Under
# this requirement, "Purdue2022-1" is a valid password of length 12, while "Purdue20220110" is not as it
# does not contain any special character.
# Since a randomly generated password may be hard to memorize, some user want to control the generation
# process by fixing some part of it to be meaningful ones, like inserting their names or birthday inside (not recommended
# to do so). In this task, you are asked to write a function named generate_password(prompt, N) that generates
# a password of length N (12<=N<=30) that satisfies the standard above while including the word prompt completely
# .To make things easier, special characters are limited to be one of the following:
# ?!@#$%^&*_.
# There can be multiple ways to generate such passwords, and you only need to output one that meets the
# requirements.
#
# Input:
# prompt. Type: str.
# N . Type: int
#
# Output:
# A password of length N satisfying the conditions described above. Type: string.
#
# Example:
# generate_password('20220110', 12) = 'One-20220110'
# generate_password('A_short_one', 12) = '1A_short_one'
# at least one lower case character, one upper case character, one digit and one special character (e.g., ?!@#$%^&*)

import random
import re

def generate_password(prompt, N):
    length_left = N - len(prompt)

    lower = re.compile("[a-z]")
    upper = re.compile("[A-Z]")
    number = re.compile("\d")
    special = re.compile("[?!@#$%^&*_]")

    lowercase = False
    uppercase = False
    num = False
    special_char = False

    if(lower.search(prompt)):
        lowercase = True
    if(upper.search(prompt)):
        uppercase = True
    if(number.search(prompt)):
        num = True
    if(special.search(prompt)):
        special_char = True

    add = ''
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_letters = "abcdefghijklmnopqrstuvwxyz".upper()
    digits = "0123456789"
    chars = "?!@#$%^&*_"

    for i in range(length_left):
        if(lowercase == False):
            add += random.choice(lower_letters)
        if(uppercase == False):
            add += random.choice(upper_letters)
        if(num == False):
            add += random.choice(digits)
        if(special_char == False):
            add += random.choice(chars)

    prompt += add[0:length_left]

    return prompt

print(generate_password('20220110', 12))
