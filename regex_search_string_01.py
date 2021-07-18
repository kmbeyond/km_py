import re


print("------ Pattern matching ------")
emailString='Email address is abc@abc.com, my phone is (123)22-3444; alternate email abc2@abc.com.'
print('STRING: '+emailString+'\n\n')

print("----- match -------")
print("Words (non-whitespace)=                          " , re.findall(r'[^ ]+',emailString))
print("Words (non-whitespace & strip ending chars(.,;))= " , re.findall(r'[^ ]+[^.,; ]+',emailString))

print("Words (\w OR [a-zA-Z0-9_])=       " , re.findall(r'[\w]+', emailString))
print("Words (\w and @.()-)= " , re.findall(r'[\w@.()-]+', emailString))

print("Email addresses matched= " , re.findall(r'[a-zA-Z0-9_]+@[a-zA-Z0-9_.]+[^., \t]+', emailString))
print("Email addresses matched= " , re.findall(r'.*?([a-zA-Z0-9_.]+@[a-zA-Z0-9_.]+).*?', emailString))

print("Words of 5 chars= ",re.findall(r'\b[\w]{5}\b', emailString) ) #Gives first 5 characters of words if \b not used
print("Words of 5 chars= ",re.findall(r'\b(\w{5})\b', emailString) )

lst_phones=[
'My Ph#: Home: (123)222-3444, Off: (123)222-3444',
'My Ph#: Home: 222-222-3444, Off: 333-222-3444',
'My Ph#: Home: 222.222.3444, Off: 333.222.3444'
]
for itm in lst_phones:
    print('-->', itm, ': ', str(re.findall(r'\(?[\d]{3}[)-.]*[\d]{3}[-.][\d]{4}', itm)) )


sPhone1='My Ph#: Home: (123)222-3444, Off: (123)222-3444'
sPhone2='My Ph#: Home: 222-222-3444, Off: 333-222-3444'
sPhone3='My Ph#: Home: 222.222.3444, Off: 333.222.3444'

print("Phone#s= " , re.findall(r'.*?(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4}).*?', sPhone1)  )

#---match() returns True or False for matches
#re.match(pattern, string, flags=0)
print("Phone# match= " , re.match(r'.*[(]*[\d]{3}[)-.]*[\d]{3}[-.][\d]{4}.*', sPhone1)  )
sPhone='414-217-2655'
if re.match(r'.*[ ]*(\d{3})-(\d{3})-(\d{4})[ ]*.*$', sPhone2):
    print("phone number is good")
else:
    print("Bad phone number format")

regexMatch =  r'(.*) are (.*?) .*'
#(.*) - group of 0 or more repetition of any character
# (.*?) - group of 0 or1 repetition of a string
#.* - 0 or more repetion of any character
line = "Cats222 are smarter33 than44 dogs"

matchObj = re.match(regexMatch, line, re.M|re.I)

if matchObj:
   print("matchObj.group() : ", matchObj.group() )
   print("matchObj.group(0) : ", matchObj.group(0))
   print("matchObj.group(1) : ", matchObj.group(1) )
   print("matchObj.group(2) : ", matchObj.group(2) )
else:
   print("No match!!")


print("----- search: Extract only date -------")
regex = r".* ([a-zA-Z]+) (\d){1,2}[,]? (\d{4})"
#.* - (Optional) 0 or more repetion of any character
#([a-zA-Z]+) - group of 1 or more repetition of upper or lower case character
#(\d+) - group to 1 or more repetition of decimal
#[,]? - comma for 0 or 1 repetion (due to ?)
#(\d{4}) - group of exactly 4 decimals
sDateMon = "Date: Jan 4, 2018 Wednesday"
if re.search(regex, sDateMon):
    match = re.search(regex, sDateMon)
    print("Match at index %s, %s" % (match.start(), match.end()))

    print("Full match/group(0): %s" % (match.group(0)))
    # So this will print "June"
    print("Month/group(1): %s" % (match.group(1)))
    # So this will print "24"
    print("Day/group(2): %s" % (match.group(2)))
    # So this will print 2017"
    print("Day/group(3): %s" % (match.group(3)))


else:
    # If re.search() does not match, then None is returned
    print("The regex pattern does not match. :(")

print("----- search: Extract date in single group-------")
#Get whole date in single group
regex = r".* ([a-zA-Z]+ \d{1,2}[,]? \d{4})"
if re.search(regex, sDateMon):
    match = re.search(regex, sDateMon)
    print("Full match/group(0): %s" % (match.group(0)))
    # So this will print "June"
    print("Month/group(1): %s" % (match.group(1)))
else:
    print("The regex pattern does not match. :(")


#get a string before -egg
match = re.search(r'(\w+)[-]{1}.*', 'spam-egg')
print("String after hyphen: %s" % (match.group(1)))

match = re.search(r'(\w+)[-]{1}.*', 'easter-egg')
print("String after hyphen: %s" % (match.group(1)))




print("----- findall: multiple occurences -----")
matches = re.findall(r'(\w+)-egg', 'easter-egg spam-egg caster-egg')
for l in matches:
    print(l)

text = """
1. ricochet robots
2. settlers of catan
3. acquire
"""
matches = re.findall(r'^(\d+)\.(.*)$', text, re.MULTILINE)
for ind, val in matches:
    print(ind, val)

print("----- sub: search & replace")
#re.sub(pattern, repl, string, max=0)
