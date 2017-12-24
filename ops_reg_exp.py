


#data is in format:
#33- (33534545)
#45- (73727479)
#67- (53512368)
#Expected: return the number between brackets (, )

for line in open("/home/kiran/km/km_hadoop/data/list_phones.txt"):
    print(line.strip('\n'))

import re
AllWords = []
for line in open("/home/kiran/km/km_hadoop/data/list_phones.txt"):
    AllWords.append(re.search(r"\(([0-9]+)\)", line).group(1))

for word in AllWords:
    print(word)
#=>
#33534545
#73727479
#53512368
