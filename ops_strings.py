

str1="Hello World"

print(str1)

print("Length: {}".format(len(str1)))

print("Length: {}".format(str1[:-3]))

strings = str1.split()
print("{0}\n{1}".format(strings, type(strings)))

s_new_line="""
"""
new_string = "line1 line2 line3".replace(' ',s_new_line)
print(new_string)