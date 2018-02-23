import re

def printList(AllWords):
    print("------- Words put into list ---------")
    for word in AllWords:
        print(word)
    print("------- Words put into list Complete---------")
    #for i in range(len(AllWords)):
    #    print("{} = {}".format(i, AllWords[i]))

def printDict(AllWordsDict):
    print("------- Words put into Dict ---------")
    for key, val in AllWordsDict.items():
        print("{} = {}".format(key, val))
    print("------- Words put into Dict Complete---------")
    #for i in range(len(AllWords)):
    #    print("{} = {}".format(i, AllWords[i]))



words = """Hello how are you easter-egg? 
how are things?
how?"""
words = open("C:\km\hadoop\data\data_wordcount.txt").read()
words = re.sub('[^a-zA-Z0-9-]', ' ', words)

#AllWordsList = re.split(r"\s+", words.lower())
AllWordsList = re.findall(r"\S+", words.lower())
printList(AllWordsList)

'''
print("-----read file, split & load into list-----")
AllWordsList = []
#for line in open("/home/kiran/km/km_hadoop/data/data_wordcount.txt"):
for line in open("C:\km\hadoop\data\data_wordcount.txt"):
    row = line.upper().split(' ')
    AllWordsList+=list(row)

printList(AllWordsList)
'''



#using Collections package
import collections
#print(collections.Counter(words.upper().split(" ")))
#print(collections.Counter(AllWords))
#=> Counter({'HOW': 2, 'ARE': 2, 'HELLO': 1, 'YOU': 1, 'THINGS': 1})

wordsCountDict = collections.Counter(AllWordsList)

for (word, count) in wordsCountDict.items():
    print("{} : {}".format(word, count))

printDict(wordsCountDict)

'''
print("----- write the dictionary")
with open("C:\km\hadoop\data\data_wordcount_op.txt", 'w') as file:
    file.write("----- writing dictionary: count using collections.Counter ------\n")
    for (word, count) in wordsCountDict.items():
        file.write("{} : {}\n".format(word, count))

file.close()
'''


#sort using OrderedDict; NOTE: sorts Key ONLY, NOT value
#wordsCountDict = collections.OrderedDict()
#d_sorted_by_value = collections.OrderedDict(sorted(wordsCountDict.items(), key=lambda x: x[1]))

#Sort into List & print
wordsCountSortedList = sorted(wordsCountDict.items(), key=lambda x: x[1], reverse=True)

printList(wordsCountSortedList)

with open("C:\km\hadoop\data\data_wordcount_op.txt", 'w') as file:
    file.write("----- writing using collections ------\n")
    for (word, count) in wordsCountSortedList:
        file.write("{} : {}\n".format(word, count))

file.close()