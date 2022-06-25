# Description
# Covid-19 is a pandemic over the world, file covid_report_county_noisy.csv contains the record of some counties,
# including district, county name, covid test, covid count and covid death.
# The first several rows in the csv file is as follow:
#      DISTRICT  COVID_COUNT  COVID_DEATHS  COVID_TEST  COUNTY_NAME
# 0  District 3        230.0           3.0      3982.0        Adams
# 1  District 3       5785.0         198.0     59360.0        Allen
# 2  District 8       1132.0           NaN     15911.0  Bartholomew
# 3  District 4         88.0           0.0      1630.0       Benton
# 4  District 6        107.0           2.0      1827.0    Blackford
# ...
# But as the filename shows, the data in this file is noisy, with some data missing and some rows duplicated.
# You task is to write the function positive_death_rate to implement the following steps:
# the function takes two arguments: filepath is the path to the csv file, covid_test is an integer.
# (1) use the given filepath to read the data from the csv file.
# (2) drop the rows with NaN.
# (3) drop the duplicated rows, except for the FIRST occurrence.
# (4) select the rows with COVID_TEST greater than or equal to the given argument covid_test.
# (5) for every row selected from (4), calculate the positive rate (positive rate = covid count / covid test)
# (6) for every row selected from (4), calculate the death rate (death rate = covid deaths / covid count)
# (7) add two columns named "POSITIVE_RATE" and "DEATH_RATE" to the dataframe selected from (4),
# and record the positive rate and death rate into the corresponding column for every row.
# (8) return the dataframe get from (7), but only with columns "COUNTY_NAME", "POSITIVE_RATE" and "DEATH_RATE".

# Example:
# > print(positive_death_rate('covid_report_county_noisy.csv', 60000))
# >    COUNTY_NAME  POSITIVE_RATE  DEATH_RATE
# 29    Hamilton       0.065517    0.023696
# 49      Marion       0.105256    0.037215
# 72  St. Joseph       0.081758    0.016363

# > print(positive_death_rate('covid_report_county_noisy.csv', 50000))
# >    COUNTY_NAME  POSITIVE_RATE  DEATH_RATE
# 1        Allen       0.097456    0.034226
# 29    Hamilton       0.065517    0.023696
# 49      Marion       0.105256    0.037215
# 72  St. Joseph       0.081758    0.016363

# > print(positive_death_rate('covid_report_county_noisy.csv', 47920))
# >    COUNTY_NAME  POSITIVE_RATE  DEATH_RATE
# 1        Allen       0.097456    0.034226
# 29    Hamilton       0.065517    0.023696
# 49      Marion       0.105256    0.037215
# 72  St. Joseph       0.081758    0.016363
# 80  Tippecanoe       0.042914    0.006152

import pandas as pd
def positive_death_rate(filepath, covid_test):
    ###
    ### YOUR CODE HERE
    ###
