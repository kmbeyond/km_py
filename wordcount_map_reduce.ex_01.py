
----- NOT COMPLETE ----------
import re
words = "Hello how are you? how are things?"
words = re.sub('[^a-zA-Z0-9- ]', '', words)

AllWordsList = words.lower().split(" ")


from functools import reduce


wordsCountList = reduce(lambda x, y: x + y, map(lambda x: (x,1), AllWordsList) )

print(wordsCountList)