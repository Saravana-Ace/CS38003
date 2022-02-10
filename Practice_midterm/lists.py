# Write a Python function divisible_position(list1, num) that takes one list and a positive integer as input.
# The input list1 contains several lists.
# every list in list1 could have no element or have several positive integers as elements.
#
# And your function does the following:
#
# determine the length of each list in list1, if the length is more than 3, keep the first three elements by slicing the list.
# compute the sum of the elements in every list separately.
# determine whether those sums computed in 2. could be divisible by the input num.
# use a new list to save all the positions of those lists whose sums of elements could be divisible.
# if you can't find such a position of a list or the list1 has no list, return False.
# if a list in list1 has no element, we should not add its index to the new list.
# Function divisible_position(list1, num)
#
# Inputs: 1 list and 1 positive integer
#
# -list1: a list of distinct lists, each list contains distinct positive integers
#
# -num: a positive integer
# Outputs: 1 output
#
# -an output contains the indexes of lists in list1 or a boolean value False.
# Example:
#
# divisible_position([[3,8],[2,4],[1,2,3]],2) should return [1,2]
#
# divisible_position([[3,4,2,1],[6,3],[2,7,1],[9],[]],5) should return [2]
#
# divisible_position([],4) should return False
#
# divisible_position([[2,6],[1,3,8],[1,1,1,1],[10]],7) should return False

def divisible_position(list1,num):
    list_sum = []
    counter = 0
    for list in list1:
        if len(list) > 3:
            list = list[0,3]

        list_sum[]

divisible_position([[3,8],[2,4],[1,2,3]],2)
