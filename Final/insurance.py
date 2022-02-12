# You're given a file named insurance.csv that contains the information of some people, including age, sex, bmi, children, smoker, region, and charges.
# The first several rows in the csv file are as follow:
#
#      age     sex        bmi      children      smoker      region      charges
#      19     female     27.9        0            yes      southwest    16884.924
#      18     male       33.77       1            no       southeast    1725.5523
#      28     male       33          3            no       southeast    4449.462
#      33     male       22.705      0            no       northwest    21984.47061
#
#      ...
# However, the data in this file is noisy, with some data missing and some rows duplicated.
# You task is to write the function rate(filepath, max_children) to implement the following steps:
#
# use the given filepath to read the data from the csv file.
# drop the rows with NaN.
# drop the duplicated rows, except for the LAST occurrence.
# select the rows with non-smokers whose children smaller than or equal to the given argument max_children.
# for every row selected from (4), calculate the charge-age rate (charge-age rate = charges / age)
# for every row selected from (4), calculate the charge-bmi rate (charge-bmi rate = charges / bmi)
# add two columns named CHARGE_AGE and CHARGE_BMI to the dataframe selected from (4).
# return the dataframe get from (7), but only with these columns age, sex, region, CHARGE_AGE and CHARGE_BMI.
# function: rate(filepath, max_children)
#
# Input: 2 inputs
#
# filepath (string): path to the csv file
# max_children (integer): max number of children
# Example:
#
#  > print(rate('insurance.csv', 5))
#
#     age  sex      region    CHARGE_AGE   CHARGE_BMI
#  1  18   male   southeast   95.864017    51.097196
#  2  28   male   southeast   158.909357   134.832182
#  3  33   male   northwest   666.196079   968.265607
#  4  32   male   northwest   120.839225   133.893878
#  5  31   female southeast   121.181342   145.944895
#  ...

import pandas as pd

def rate(filepath, max_children):
    df = pd.read_csv(filepath)
    df = df.dropna()
    df = df.drop_duplicates(keep="last")
    df = df.loc[(df["smoker"] == "no") & (df["children"] <= max_children)]
    df["CHARGE_AGE"] = df["charges"]/df["age"]
    df["CHARGE_BMI"] = df["charges"]/df["bmi"]
    df1 = df[["age", "sex", "region", "CHARGE_AGE", "CHARGE_BMI"]]
    return df1

print(rate('insurance.csv', 5))
