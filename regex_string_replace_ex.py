

str2 = "Love your neighbor, help your neighbor, work with your neighbor"

print("----- using string function-----")
newStr1 = str2.replace("your", "thy")
print("Updated string: {}".format(newStr1) )



print("----- using regex sub()-------")
import re

newStr2 = re.sub(r'(your)', 'thy', str2)
print("Updated string: {}".format(newStr2) )


