
import re
import string

wordsCountDict = {}

words = "Hello how are you? how are things?"

#file = open("/home/kiran/km/km_hadoop/data/data_wordcount.txt", 'r')
file = open("C:\km\hadoop\data\data_wordcount.txt", 'r')
text_string = file.read().lower()

text_string = re.sub('[^a-zA-Z0-9-]', ' ', text_string)

match_pattern = re.findall(r'(\w+)', text_string)

for word in match_pattern:
    count = wordsCountDict.get(word ,0)
    wordsCountDict[word] = count + 1


def printDict(AllWordsDict):
    print("------- Words put into Dict ---------")
    for key, val in AllWordsDict.items():
        print("{} = {}".format(key, val))
    print("------- Words put into Dict Complete---------")
    #for i in range(len(AllWords)):
    #    print("{} = {}".format(i, AllWords[i]))

printDict(wordsCountDict)

#Sort into List & print
wordsCountSortedList = sorted(wordsCountDict.items(), key=lambda x: x[1], reverse=True)
printList(wordsCountSortedList)


#frequency_list = wordsCountDict.keys()

