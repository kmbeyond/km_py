
import collections as cl

import re

#From list
words = ["cat", "rat", "tiger", "cat", "dog", "rat", "cat", "dog", "cat", "dog"]

#From a file
#words = re.findall(r'\w+', open('/home/kiran/km/km_hadoop/data/data_wordcount.txt').read().lower())

#words = re.split(r"\s+", "d c b a e a b d a b f f a")


wordsCountDict = cl.Counter(words).most_common(10)

for word, cnt in wordsCountDict:
    print("{} - {}".format(word, cnt))



#from keyword args

wordsCountDict = cl.Counter(cats=4, dogs=8)             # a new counter from keyword args


for word in wordsCountDict:
    print("{} - {}".format(word, wordsCountDict[word]))
