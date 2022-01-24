# # Write a function called dictionary_range(dict_list) which takes a list of dictionaries as input
# # and the output of the function is a dictionary with all the key having value as a list in the format
# # [start,end] that depicts the range of input dictionary values. If a key occurss only once then start and end value is
# # the same.
# #
# # Input:
# # dict_list, Type: list of dictionaries
# #
# # Output:
# # Type: dictionary
# #
# # Example:
# # dictionary_range([{'apple': 5, 'mango': 3,'banana': 2}, {apple': 6, 'mango': 1}]) =
# # {'apple': [5, 6], 'mango': [1, 3], 'banana': [2, 2]}
# # dictionary_range([{'red': 3,'yellow': 5, 'orange': 5}, {'red': -1,'yellow': 3, 'orange': 6}]) =
# # {'red': [-1, 3], 'yellow': [3, 5], 'orange': [5, 6]}
# # dictionary_range([{},{}]) = {}
#
# def main():
#
#     complete_dictionary = dictionary_range([{'apple': 5, 'mango': 3,'banana': 2}, {'apple': 6, 'mango': 1}])
#
#     print(complete_dictionary)
#
# def dictionary_range(dict_list):
#
#     all_keys = []
#     all_values = []
#     combined_values = []
#
#     for i in range(len(dict_list)):
#         list_keys = list(dict_list[i].keys())
#         list_values = list(dict_list[i].values())
#
#         for j in range(len(list_keys)):
#
#             if(all_keys.count(list_keys[j]) == 0):
#                 all_keys.append(list_keys[j])
#
#         all_values.append(list_values)
#
#     print(len(all_values))
#
#     for i in range(len(all_values)):
#
#         print(len(all_values[i]))
#         for j in range(len(all_values[i])):
#
#             if(j < len(all_values[i])):
#                 temp = [0] * 2
#                 temp[j][i] = (all_values[j][i])
#                 combined_values.append(temp)
#
#             print(temp)
#
#
#     print(combined_values)
#
# if __name__ == '__main__':
#     main()

def dictionary_range(dict_list):
    return_dictionary = {}

    for dictionary in dict_list:
        for key in dictionary.keys():
            if key not in return_dictionary.keys():
                return_dictionary[key] = [dictionary[key], dictionary[key]]
            else:
                if return_dictionary[key][0] > dictionary[key]:
                    return_dictionary[key][0] = dictionary[key]

                if return_dictionary[key][1] < dictionary[key]:
                    return_dictionary[key][1] = dictionary[key]

    return return_dictionary


    def dictionary_range(dict_list):
    final_dict = {}

    for dict in dict_list:
        for key in dict.keys():
            if key not in final_dict.keys():
                final_dict[key] = [dict[key], dict[key]]
            else:
                if final_dict[key][0] > dict[key]:
                    final_dict[key][0] = dict[key]
                if final_dict[key][1] < dict[key]:
                    final_dict[key][1] = dict[key]
    return final_dict
