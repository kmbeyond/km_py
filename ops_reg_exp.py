


#data is in format:
#33- (33534545)
#45- (73727479)
#67- (53512368)
#Expected: return the number between brackets (, )

for line in open("/home/kiran/km/km_hadoop/data/list_phones.txt"):
    print(line.strip('\n'))

import re
AllWords = []
regexpr = r"\(([0-9]+)\)"

for line in open("/home/kiran/km/km_hadoop/data/list_phones.txt"):
    AllWords.append(re.search(regexpr, line).group(1))

for word in AllWords:
    print(word)
#=>
#33534545
#73727479
#53512368



