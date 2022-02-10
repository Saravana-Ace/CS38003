# Part 1
# In this assignment, you will be experimenting with a popular python data analysis library - Pandas.
# This assignment should use a file similar to sample.csv for grading purpose
# Given a csv file in which each row has the following information of a movie (represented as columns): "Year, Length, Title, Subject, Actor, Actress, Director, Popularity, Awards, and Image The given csv file might not be perfect and contains some missing information or errors. Thus, your first task is to write a function called read_input(filename) that takes a string as parameter. This string specifies the name of the csv file to read. This function should:
#
# read the csv file into a pandas DataFrame
# remove all rows that has missing information
# remove all duplicated rows
# return a clean DataFrame
import pandas as pd

def read_input(filename):
    df_grades = pd.read_csv(filename)
    df_grades = df_grades.dropna()
    df_grades = df_grades.drop_duplicates()

    return df_grades

def mean_length(df):
    group = df.groupby(["Subject"])["Length"].mean()
    return group

mean_length(read_input("sample.csv"))
