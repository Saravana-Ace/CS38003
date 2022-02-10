def common_elements(data):
    multiples = {}
    final_list = []

    for list in data:
        keys = multiples.keys()

        for number in list:
            if number in keys:
                multiples[number] += 1
            else:
                multiples[number] = 1

    for number in multiples:
        if(multiples[number] > 1):
                final_list.append(number)
    final_list.sort()

    return final_list
