def sum_grades(gradesList):
    final_dict = {}
    if(len(gradesList) == 0):
        return -1

    for list in gradesList:
        if(list[0] not in final_dict):
            final_dict[list[0]] = list[1]
        else:
            final_dict[list[0]] += list[1]
    return final_dict
