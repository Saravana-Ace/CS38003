# Bob got his first of set grades back, and he wants to improve them!
# Given nested dictionary bob_grades with key:value pairs
#  {Course: {Homework #: Grades}} write function improve_semester(bob_grades) that determines the course with
# the worst average grade, and the new rounded average grade across all courses if he improves
# the worst grade by 15 percentage points total (up to a max of 100).
# Return both in a list, I.e. [Course_name, new_average] = [“Math”, 85]
#
# If bob_grades is empty, return None. But if a course has no grades yet, do not include it in the average or minimum calculations
#
# Note: you may assume that all of the initial grade averages will be unique.
# Hint: remember that you are returning an int, not a double. Round it!!
#
# Examples of Python rounding
#
# 1.2 -> 1
#
# 2.6 -> 3
#
# 4.5 -> 4
#
# Input: dictionary
# Output: list [string, int]
#
# Example:
#
# improve_semester({"Math": {1: 86, 2: 81}, "English": {1: 60, 2: 71}, "Science": {1: 90}}) = ['English', 85]
#
#  Average of math homeworks is 83.5, average of english is 65.5, and average of science is 90. The worst grade is english.
#  If he improves English by 15 points, he will get 80.5, and the new rounded average across the three courses becomes 85.
#
# improve_semester({"Spanish": {1: 97}, "English": {1: 100}, "Science": {1: 90}}) = ['Science', 99]
#
# In this case, Bob's worse average is a 90. He can improve this to a 100%, and the new rounded average is 99.
#
# improve_semester({"Spanish": {1: 50}, "English": {}) = ['Spanish', 65]
#
# Because English has no grades yet, do not include it. The average across the courses is 50, add 15 to get 65, which is the new average.

def improve_semester(bob_grades):
    if(len(bob_grades) == 0):
        return None

    all_courses = list(bob_grades.keys())
    averages = []
    worst_grade = []

    for course in bob_grades:
        grade = 0
        avg = 0

        len(bob_grades.get(course))
        if(len(bob_grades.get(course)) == 0):
            continue
        temp_course = bob_grades.get(course)

        for hw_number in bob_grades.get(course):

            grade += temp_course.get(hw_number)

        avg = grade/len(bob_grades.get(course))
        averages.append(avg)

    lowest = averages[0]
    lowest_name = ""

    for i in range(len(averages)):
        if (averages[i] < lowest):
            lowest = averages[i]
            lowest_name = all_courses[i]

    if(len(averages) == 1):
        lowest_name = all_courses[0]
    sum = 0
    for i in range(len(averages)):
        if (lowest == averages[i]):
            averages[i] += 15

        if(averages[i] > 100):
            averages[i] = 100
        sum += averages[i]

    overall_avg = sum/len(averages)
    overall_avg = round(overall_avg)

    return_list = []
    return_list.append(lowest_name)
    return_list.append(overall_avg)

    return return_list
#
# print(improve_semester({"Math": {1: 86, 2: 81}, "English": {1: 60, 2: 71}, "Science": {1: 90}}))
# print(improve_semester({"Spanish": {1: 97}, "English": {1: 100}, "Science": {1: 90}}))
# print(improve_semester({"Spanish": {1: 50}, "English": {}}))
