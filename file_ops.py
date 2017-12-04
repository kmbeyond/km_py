

#read file, split & load into list
AllWords = []
for line in open("/home/kiran/km/km_hadoop/data/data_wordcount.txt"):
    row = line.split(' ')
    AllWords+=list(row)



for word in AllWords:
    print(word)

for i in range(len(AllWords)):
    print("{} = {}".format(i, AllWords[i]))



#insert newline after every words in a file

with open("/home/kiran/km/km_hadoop/data/data_wordcount_op.txt", 'a') as file:
    for i in range(len(AllWords)):
        if(i%3==0):
            file.write("\n"+AllWords[i].strip('\n'))
        else:
            file.write(" "+AllWords[i].strip('\n'))
