# Write a function called dictionary_range(dict_list) which takes a list of dictionaries as input
# and the output of the function is a dictionary with all the key having value as a list in the format
# [start,end] that depicts the range of input dictionary values. If a key occurss only once then start and end value is
# the same.
#
# Input:
# dict_list, Type: list of dictionaries
#
# Output:
# Type: dictionary
#
# Example:
# dictionary_range([{'apple': 5, 'mango': 3,'banana': 2}, {apple': 6, 'mango': 1}]) =
# {'apple': [5, 6], 'mango': [1, 3], 'banana': [2, 2]}
# dictionary_range([{'red': 3,'yellow': 5, 'orange': 5}, {'red': -1,'yellow': 3, 'orange': 6}]) =
# {'red': [-1, 3], 'yellow': [3, 5], 'orange': [5, 6]}
# dictionary_range([{},{}]) = {}

dict_list = [{'red': 3,'yellow': 5, 'orange': 5}, {'red': -1,'yellow': 3, 'orange': 6}]

for dict in dict_list:
    for key in dict.keys():
        if key not in final_dict.keys():
            final_dict[key] = [dict[key], dict[key]]
        else:
            if final_dict[key][0] > dict[key]:
                final_dict[key][0] = dict[key]
            if final_dict[key][1] < dict[key]:
                final_dict[key][1] = dict[key]


print(final_dict)
