from bs4 import BeautifulSoup
import requests 
import re
import json
Courselink=""
code = "CH31007"
courseFile = requests.get("https://wiki.metakgp.org/index.php?title=Category:Courses")
soup=BeautifulSoup(courseFile.text,'html.parser')
coursecodes=[]
codes=[]
pattern="[A-Z][A-Z][0-9][0-9][0-9][0-9][0-9]"
for a in soup.find_all('a',href = True):
    if(re.search(pattern,a['href'][3:10])):
        coursecodes.append(a['href'])
        codes.append(a['href'][3:10])
for i in range(2,201):
    for a in soup.find_all('a',href=True,text = 'next page'):
        nextpagelink = a['href']
        courseFile=requests.get("https://wiki.metakgp.org"+nextpagelink)
        soup=BeautifulSoup(courseFile.text,'html.parser')
        pattern="[A-Z][A-Z][0-9][0-9][0-9][0-9][0-9]"
        for a in soup.find_all('a',href = True):
            if(re.search(pattern,a['href'][3:10])):
                coursecodes.append(a['href'])
                codes.append(a['href'][3:10])
Data={}
for i in range(len(codes)):
    new_key = codes[i]
    new_value = coursecodes[i]
    Data[new_key] = new_value
with open("data_file.json","w") as write_file:
    json.dump(Data,write_file)
        
       