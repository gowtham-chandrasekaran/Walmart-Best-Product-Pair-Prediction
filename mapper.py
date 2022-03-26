#!/usr/bin/python

import sys

# f = open("retail.txt","r")
# Lines = f.readlines()
# for line in Lines:

for line in sys.stdin:

    line = line.strip()

    # set will remove possible repetition of numbers in the line
    numbers = list(set(line.split()))

    # print(numbers)
    for i in range(len(numbers)):
        # Print individual number and count 1
        line1 = "Individual" +"\t"+ numbers[i] + "\t"+"1"+"\n"
        print(line1)

        for j in range(len(numbers)):
            # Avoid pairing a number with itself
            if numbers[i] != numbers[j]:
                # Print pairs with count 1
                line2 = "Pair" +"\t"+ numbers[i]+" "+numbers[j]+"\t"+"1" +"\n"
                print(line2)


