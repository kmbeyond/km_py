

str1 = "Hello How are you?"


#without using regex
matches1 = str1.split()
for word in matches1:
    print(word)


print("----- regex split-----")
import re

matches2 = re.split(r" +", str1)
for word in matches2:
    print(word)



matches3 = re.split(r"\s+", str1)
for word in matches3:
    print(word)


print("---- findall() ------")
#findall - get all non-whitespace strings
matches4 = re.findall("\S+", str1)
for word in matches4:
    print(word)
