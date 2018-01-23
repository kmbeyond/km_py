
'''
Program to read a file of words, break it at every period or every 1000th word & write to a new file.
Input:
    -file name
Output:
    -Write to file

Author: Kiran Miryala/7897655

Steps:
1.Read from file:
-data_words.txt

2.Split & add to list
3.Open file to write, write a new line for every
-period
-next 1000th word

Execution:
python uc_break_words.py /home/kiran/km/km_hadoop/data/data_words.txt /home/kiran/km/km_hadoop/data/data_words_op.txt
'''

import sys

#fileNameInput = sys.argv[1] #/home/kiran/km/km_hadoop/data/data_words.txt
fileNameInput = "/home/kiran/km/km_hadoop/data/data_wordcount.txt"

#fileNameOutput = sys.argv[2] #/home/kiran/km/km_hadoop/data/data_words.txt
fileNameOutput = "/home/kiran/km/km_hadoop/data/data_words_op.txt"

AllWords = []
for line in open(fileNameInput):
    row = line.split(' ')
    AllWords+=list(row)

print(AllWords)


line_breaker=3
i=1

with open(fileNameOutput, 'a') as file:
    for word in AllWords:
        if("." in word or i==line_breaker):
            file.write(word.strip('\n')+"\n")
            i=0
        else:
            file.write(word.strip('\n')+" ")

        i+=1


del file

