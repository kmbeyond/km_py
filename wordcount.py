import re

#------ Defining just print functions ------------
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



words = "Hello how are you? how are things?"
words = re.sub('[^a-zA-Z0-9- ]', '', words)

AllWordsList = words.lower().split(" ")
printList(AllWordsList)


print("-----read file, split & load into list-----")
AllWordsList = []
'''
#for line in open("/home/kiran/km/km_hadoop/data/data_wordcount.txt"):
for line in open("C:\km\hadoop\data\data_wordcount.txt"):
    row = line.upper().split(' ')
    AllWordsList+=list(row)
'''

file = open("C:\km\hadoop\data\data_wordcount.txt", 'r')
data = file.read()
data = re.sub('[^a-zA-Z0-9-]', ' ', data)
AllWordsList = data.lower().split(' ')
file.close()

printList(AllWordsList)



wordsCountDict = {}
for word in AllWordsList:
    count = wordsCountDict.get(word, 0)
    wordsCountDict[word] = count + 1


printDict(wordsCountDict)


#Sort into List & print
wordsCountSortedList = sorted(wordsCountDict.items(), key=lambda x: x[1], reverse=True)
printList(wordsCountSortedList)

with open("C:\km\hadoop\data\data_wordcount_op.txt", 'w') as file:
    file.write("----- writing using List/Dict ------\n")
    for (word, count) in wordsCountSortedList:
        file.write("{} : {}\n".format(word, count))

file.close()
