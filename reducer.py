#!/usr/bin/python

import sys
import json


individual2count = {}
pair2count = {}


for line in sys.stdin:

    line = line.strip()
    line_list = line.split('\t')

    # Create a dictionary that holds individual counts
    if line_list[0] == "Individual":
        if line_list[1] in individual2count:
            individual2count[line_list[1]] += int(line_list[2])
        else:
            individual2count[line_list[1]] = int(line_list[2])
    # Create a dictionary that holds pair counts
    if line_list[0] == "Pair":
        if line_list[1] in pair2count:
            pair2count[line_list[1]] += int(line_list[2])
        else:
            pair2count[line_list[1]] = int(line_list[2])


for pair in pair2count:
    A, B = pair.split()
    # To display the probability for each pair when encountered
    print(B+"|"+A+"\t"+str(float(float(pair2count[pair])/float(individual2count[A]))))

# To generate the pair2count dictionary as a text file to use it for the next question
f1 = open('/Users/gowthamc/Desktop/SJSU/Spring_2022/Topics_in_DB/HW/2/answers/part-2/pair2count.txt','a')
f1.write(json.dumps(pair2count))
f1.close()
