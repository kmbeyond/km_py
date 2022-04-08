#Read file

#read file directly into a string
file = open('deploy_plan.csv')
contents = file.read()
file.close()

print(f"File data: {contents}")

#print each line (split by new line)
for line in contents.split('\n'):
    print(f"-> {line}")

    
#read file, split by space & load into list
AllWords = []
for line in open("/home/kiran/km/km_big_data/data/data_wordcount.txt"):
#for line in open("C:\km\hadoop\data\data_wordcount.txt"):
    row = line.split(' ')
    AllWords+=list(row)


#Write a string to file
str_data="line1\nline2\nline3"
with open("zz_test.txt", 'w') as file:
    file.write(f"{str_data}")



#insert every n words or period in a row & write into a file

'''
#Option#1
sFullString=""
flgPeriod=False
#with open("/home/kiran/km/km_big_data/data/data_wordcount_op.txt", 'a') as file:
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
with open("/home/kiran/km/km_big_data/data/data_wordcount_op.txt", 'a') as file:
#with open("C:\km\hadoop\data\data_wordcount_op.txt", 'a') as file:
    for word in AllWords:
        if("." in word or i==line_breaker):
            file.write(word.strip('\n')+"\n")
            sFullString+=word.strip('\n')+"\n"
            i=1
        else:
            file.write(word.strip('\n')+" ")
            sFullString+=word.strip('\n')+" "
            i+=1

print(sFullString)
