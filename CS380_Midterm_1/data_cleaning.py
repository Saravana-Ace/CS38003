import re

def clean_data(filename):
    all_lines = []
    temp = []
    pattern = re.compile("^\w+")

    with open(filename, 'r') as fo:
        for line in fo:
            new_line = re.sub("[^A-Za-z0-9 ]+", "" , line)
            if(len(new_line) > 0):
                all_lines.append(new_line)
        return all_lines
print(clean_data("test1.txt"))
