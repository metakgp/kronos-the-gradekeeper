import requests
import json

fac_list=requests.get('https://hercules-10496.herokuapp.com/api/v1/faculty/info/all')
fac_name= [nam['name'] for nam in fac_list.json()]
fac_dep=  [dep['department']['code'] for dep in fac_list.json()]

fac_map_cour ={fac_name[x] : [] for x in range(len(fac_name)) }

def extract_func(cod_e, nam_e):
    r = requests.get('https://hercules-10496.herokuapp.com/api/v1/course/info/faculty?name=' + nam_e + '&dept=' + cod_e)
    if r.json() is not None:
        for i in r.json():
            lest.append(i['code'])
    else:
        lest.append("None")


for tot in range(len(fac_name)):
    nam_e = fac_name[tot]
    cod_e = fac_dep[tot]
    lest = fac_map_cour[fac_name[tot]]

    extract_func(cod_e, nam_e)

data = fac_map_cour

fac_names=data.keys()

course_codes=data.values()

all_courses_list=[]

reverse_map={}

for lest in course_codes:
    for particular_code in lest:
        if particular_code not in all_courses_list:
            all_courses_list.append(particular_code)
        else :
            pass

for particular in all_courses_list:
    reverse_map[particular]=[]
    for x in data :
        if particular in data[x]:
            reverse_map[particular].append(x)

final_dict ={}

for randome in reverse_map:
    final_dict[randome]={'2018Autumn':reverse_map[randome]}


with open('Course_Teaching_Faculties.json','w') as write_file :
    json.dump(final_dict,write_file,indent = 4)