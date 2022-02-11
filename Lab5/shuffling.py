# One application of randomnness is to shuffle the elements of sequence. For example, when you play cards,
# you would shuffle the deck in the first place. When using quicksort to sort an array, a good start can also
# be shuffling the elements so that the worst running time of O(n^2) is more unlikely to happen.
# In this lab, you are asked to write a function called shuffle(x) that shuffle the input sequence x so that
# the shuffled sequence y is like shuffling a deck of x: it is of same length as x, and each element in x is shuffled to
# a unique position in y. There can be many ways to shuffle a sequence, and you simply need to output one that
# meets the requirements above.
# Do not simply use random.shuffle to solve this problem. Do not always return the original input as shuffled sequence.

# Input:
# a sequence of elements, x. Type: list
#
# Output:
# shuffled sequence. Type: list
#
# Example: (your implementation may return something different)
# shuffle([0,1,2,3]) = [0,3,2,1]
# shuffle([0,'a','b',3]) = [0,'a',3,'b']
#

import random

def shuffle(x):
    shuffled = [''] * len(x)

    rand = random.randrange(len(x))
    counter = 0
    while('' in shuffled):
        if(shuffled[rand] ==  ''):
            shuffled[rand] = x[counter]
            counter += 1
        rand = random.randrange(len(x))

    return shuffled


print(shuffle([0,1,2,3,4,5,6,7,8,9]))
