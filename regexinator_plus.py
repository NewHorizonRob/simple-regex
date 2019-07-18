# Robert Thomas
# AIST 2120
# Homework 4
# 6/17/19
# regexinator_plus.py

import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)



emailRegex = re.compile(r'''(
 [a-zA-Z0-9._%+-]+
  @
 [a-zA-Z0-9.-]+
 (\.[a-zA-Z]{2,4})
 )''', re.VERBOSE)


print ("Welcome to the Regexinator Plus Program")

input_file = open(input("Enter the input Filename: "))
output_file = open(input("Enter the name of the output file: "), 'w')


matches = []
for groups in phoneRegex.findall(input_file):
     matches.append(groups[0])
for groups in emailRegex.findall(input_file):
    matches.append(groups[0])
     




for item in matches:
    output_file.write(item)

input_file.close()
output_file.close()