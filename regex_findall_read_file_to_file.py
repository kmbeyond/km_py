
import re

re_ph = re.compile(r'.*?(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4}).*?')
with open("/home/kiran/km/km_big_data/data/data_phone_no_scraping_output.txt", 'a') as fpa:
 with open("/home/kiran/km/km_big_data/data/data_phone_no_scraping.txt") as fpr:
  for line in fpr:
   result = re_ph.findall(line)
   for i in result: fpa.write(str(i)+"\n")

fpa.close()
fpr.close()


#extract email address from file & write to file
re_email= re.compile(r'[a-zA-Z0-9_]+@[a-zA-Z0-9_.]+[^., \t]+')
re_email=re.compile(r'.*?([a-zA-Z0-9_.]+@[a-zA-Z0-9_.]+).*?')
with open("/home/kiran/km/km_big_data/data/data_scala_users_email_output.txt", 'a') as fpa:
 with open("/home/kiran/km/km_big_data/data/data_scala_users") as fpr:
  for line in fpr:
   result = re_email.findall(line)
   print(result)
   #for i in result: fpa.write(str(i)+"\n")

fpa.close()
fpr.close()
