# You are given a file records.csv containing the data for few students.
# Kindly take a look at the file.
# In this question, you shall write a Python class called Records, which shall have four methods, and two member dictionaries.
# The first dictionary shall be used to store student records, and the second a GPA scale:
#
# __init__(self, filename):
#
# This is the constructor method for the class.
# It should take the filename given as input (e.g. records.csv), and populate the first dictionary as follows:
#
# the keys of the dictionary should be student names
# the values of the dictionary should be a list, containing Department, Year, Course1 grade, Course2 grade,Course3 grade, and Course4 grade. This is the information that appears in the file records.csv for each student. E.g. {'Jd': ['CS', 'Fresher', 'C+', 'D+' , 'F', 'D-'], ...}
# This method should also populate the second dictionary, a grade-to-numerical value map, whose keys should be the letter grades from A+ to F, and whose values should be the numerical GPA for the letter grade that Purdue has in its grading system, e.g.
#
# {'A+': 4.3,
# 'A': 4.0,
# 'A-': 3.7,
# 'B+': 3.3,
# 'B': 3.0,
# 'B-': 2.7,
# 'C+': 2.3,
# 'C': 2.0,
# 'C-': 1.7,
# 'D+': 1.3,
# 'D': 1.0,
# 'D-': 0.7,
# 'F': 0.0}
# get_records(self, student):
#
# This methods should take a student name as input, and look up the record of this student in the first dictionary created by the __init__() method. If the student exists in the records, then it should return the student's record, which will be a list. If the student does not exist, then it should return a string saying "No record for <student> found!" (replace <student> with its actually string value).
#
# insert_record(self, info):
#
# This method should take a list containing a record for a student as input, e.g. ['Jason','Philosophy','Fresher','A','B','C','D'], and insert it in the first dictionary prepared by the __init__() method. So after running this method, there should be a record for student Jason in dictionary, i.e. an entry like {..., 'Jason': ['Philosophy','Fresher','A','B','C','D'],...}
#
# compute_gpa(self, student):
#
# This method shall take a student name as input. If the student exists in the first dictionary, then it should use the second dictionary, the grading scales, to compute and return the gpa for this student. Assume that each of the four courses whose grades are recorded are of 4 credit hours. If there is no record for the student passed as input, then the method should return a String saying "No record for <student> found!".

import pandas as pd

class Records:
    def __init__(self, filename):
        df = pd.read_csv(filename)
        keyList = list(df["Student"])
        depList = list(df["Department"])
        yrList = list(df["Year"])
        course1List = list(df["Course1"])
        course2List = list(df["Course2"])
        course3List = list(df["Course3"])
        course4List = list(df["Course4"])
        valueList = []
        self.dict = {}

        for i in keyList:
            self.dict[i] = None

        for i in range(len(keyList)):
            valueList.append(str(depList[i]))
            valueList.append(str(yrList[i]))
            valueList.append(str(course1List[i]))
            valueList.append(str(course2List[i]))
            valueList.append(str(course3List[i]))
            valueList.append(str(course4List[i]))
            self.dict[keyList[i]] = valueList
            valueList = []

        self.grade_to_numerical = {'A+': 4.3,'A': 4.0,'A-': 3.7,'B+': 3.3,'B': 3.0,
        'B-': 2.7,'C+': 2.3,'C': 2.0,'C-': 1.7,'D+': 1.3,'D': 1.0,'D-': 0.7,
        'F': 0.0}

    def get_records(self, student):
        if(student in list(self.dict.keys())):
            return self.dict.get(student)
        else:
            return "No record for " + student + " found!"

    def insert_record(self, info):
        self.dict[info[0]] = info[1:]

    def compute_gpa(self, student):
        points = 0
        vals = self.dict.get(student)
        if(student in list(self.dict.keys())):
            points = self.grade_to_numerical[vals[2]] + self.grade_to_numerical[vals[3]] + self.grade_to_numerical[vals[4]] + self.grade_to_numerical[vals[5]]
            return points/4
        else:
            return "No record for " + student + " found!"
