# Write a function file_analysis(filename) that does the following:
#
# read the contents of the file passed as the parameter.
# remove all but alphanumeric characters from the contents of the file read in step 1.
# This means removing all punctuation marks, and special characters like '$', '@', '*', curly quotation marks etc.
# create and return a list of tuples of the form (word, count).
# sort the list from 3. in descending order of the count of words.
# return the first ten elements in the sorted list from 4. If the list in 4. has less than ten tuples in it, then return the whole list
# function file_analysis(filename)
#
# Inputs: 1 input
#
# filename: a string representing the file, e.g. '/Users/user1/Desktop/file.txt'. Type: String
# Outputs: 1 output
#
# a list of tuples
# Examples
#
# for test1.txt, the function should return the following
#
# [('editing', 2), ('against', 1), ('for', 1), ('are', 1), ('see', 1), ('content', 1), ('about', 1), ('around', 1),('Some', 1), ('Python', 1)]

import re
import collections

def file_analysis(filename):
    word_dict = {}
    tuple_list = []

    with open(filename, "r") as fo:
        for line in fo:
            y = re.sub('[^A-Za-z0-9]+', ' ', line).strip()
            words = y.split(" ")

            for word in words:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1

        tuple_list = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
        if(len(tuple_list) > 10):
            tuple_list = tuple_list[0:10]

    return tuple_list

print(file_analysis("test1.txt"))
