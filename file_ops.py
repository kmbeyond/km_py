

#read file, split & load into list
AllWords = []
#for line in open("/home/kiran/km/km_hadoop/data/data_wordcount.txt"):
for line in open("C:\km\hadoop\data\data_wordcount.txt"):
    row = line.split(' ')
    AllWords+=list(row)


print("------- words put into list ---------")
for word in AllWords:
    print(word)
print("------- words put into list Complete---------")
#for i in range(len(AllWords)):
#    print("{} = {}".format(i, AllWords[i]))


'''
#insert newline after every words in a file
#Option#1
sFullString=""
flgPeriod=False
#with open("/home/kiran/km/km_hadoop/data/data_wordcount_op.txt", 'a') as file:
with open("C:\km\hadoop\data\data_wordcount_op.txt", 'a') as file:
    for i in range(len(AllWords)):
        if("." in AllWords[i]):
            #AllWords.insert(i, "*")
            flgPeriod=True

        if(i%3==0 or flgPeriod):
            #file.write("\n"+AllWords[i].strip('\n'))
            sFullString+="\n"+AllWords[i].strip("\n")
        else:
            #file.write(" "+AllWords[i].strip('\n'))
            sFullString+=" "+AllWords[i].strip("\n")
        flgPeriod=False

print(sFullString)
'''

#Option#2
print("******Option#2************")
sFullString=""
line_breaker=3
i=1
#with open("/home/kiran/km/km_hadoop/data/data_wordcount_op.txt", 'a') as file:
with open("C:\km\hadoop\data\data_wordcount_op.txt", 'a') as file:
    for word in AllWords:
        if("." in word or i==line_breaker):
            file.write(word.strip('\n')+"\n")
            sFullString+=word.strip('\n')+"\n"
            i=0
        else:
            file.write(word.strip('\n')+" ")
            sFullString+=word.strip('\n')+" "

        i+=1

print(sFullString)