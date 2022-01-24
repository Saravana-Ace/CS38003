def readParagraphs(filename):
    a_file = open(filename, "r")

    lines = a_file.read()
    lines = lines.translate(str.maketrans('', '', string.punctuation)).lower()
    if "\n" in lines:
        lines1 = lines[:lines.index("\n")]
        lines2 = lines[lines.index("\n")+1:]

    para1 = lines1.split()
    para2 = lines2.split()

    a_file.close()

    return para1, para2

def similarityAnalysis(paragraph1, paragraph2):
    para3 = paragraph1 + paragraph2
    all_words = {}

    for word in para3:
        temp_list = []

        counter_para1 = 0
        counter_para2 = 0

        for para1_word in paragraph1:
            if word == para1_word:
                counter_para1 += 1

        for para2_word in paragraph2:
            if word == para2_word:
                counter_para2 += 1

        temp_list.append(counter_para1)
        temp_list.append(counter_para2)

        all_words[word] = temp_list

    return all_words
