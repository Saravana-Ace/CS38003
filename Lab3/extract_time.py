# Information extraction is an important process in data science.
# In this exercise, you will write a function called extract_date
# to collect the timestamp information from a given file, the addresses are in the format below:
# [2 digits]:[2 digits]:[2digits]
#
# extract_time takes filename as input, which is the path to the file you need to collect timestamp
# from and returns a list. The list contains all the timestamps. The list should be sorted ascendingly
#
# Note: You need to use regular expressions to extract the addresses.

# Examples:
# If the file contains following lines:
# From r  Wed Oct 30 21:41:56 2002
# Return-Path: <james_ngola2002@maktoob.com>
# X-Sieve: cmu-sieve 2.0
# Return-Path: <james_ngola2002@maktoob.com>
# Message-Id: <200210310241.g9V2fNm6028281@cs.CU>
# From: "MR. JAMES NGOLA." <james_ngola2002@maktoob.com>
# Reply-To: james_ngola2002@maktoob.com
# To: webmaster@aclweb.org

# From r  Wed Oct 30 21:41:56 2002
# Date: Thu, 31 Oct 2002 02:38:20 +0000


# You need to return
# ['02:38:20', '21:41:56']

import re

def extract_time(filename):
    times = []
    final_times = []
    p = re.compile("[0-2][0-9]:[0-5][0-9]:[0-5][0-9]")

    with open(filename, "r") as fo:
        for line in fo:
            if(p.search(line)):
                times.append(p.findall(line))

    for time in times:
        for i in time:
            final_times.append(i)

    final_times.sort()

    # print(final_times)
    return final_times



extract_time("email_list.txt")
