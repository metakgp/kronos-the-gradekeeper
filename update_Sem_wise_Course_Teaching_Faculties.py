# it  imports the required libraries
import requests
import json

# collecting_required_URL's_and_making_them_global_strings

all_facs = 'https://hercules-10496.herokuapp.com/api/v1/faculty/info/all'
fac_info = 'https://hercules-10496.herokuapp.com/api/v1/course/info/faculty?name={nam_e}&dept={cod_e}'
sem_name=input("Enter the semester name whose data is currently hosted by Hercules")


def who_taught_which_sem(all_facs,fac_info,sem_name):
    with open('Sem_wise_Course_Teaching_Faculties.json', 'r') as avlbl_data:
        avalible_data =  json.loads(avlbl_data.read())


    # extract_func extracts the course codes of courses taught by a faculty given the faculty name and department code

    def extract_func(cod_e, nam_e,lest):
        r = requests.get(fac_info.format(nam_e=nam_e, cod_e=cod_e))
        if r.json() is not None:
            for i in r.json():
                lest.append(i['code'])
        else:
            lest.append("None")

    # this piece of code gets ready the input needed for extract_func and runs it with that input to get us a list of course codes of courses taught by a faculty

    def faculty_to_course_mapping():
        fac_list = requests.get(all_facs)
        fac_name_list = [nam['name'] for nam in fac_list.json()]
        fac_dep = [dep['department']['code'] for dep in fac_list.json()]

        fac_map_cour = {fac_name_list[x]: [] for x in range(len(fac_name_list))}

        for fac_num in range(len(fac_name_list)):
            nam_e = fac_name_list[fac_num]
            cod_e = fac_dep[fac_num]
            lest = fac_map_cour[fac_name_list[fac_num]]

            extract_func(cod_e, nam_e,lest)

        return (fac_map_cour)

    data = faculty_to_course_mapping()

    # fac_names = data.keys()

    course_codes = data.values()

    #makes a list of all different courses that are offered by all the faculties

    all_courses_list = []

    for lest in course_codes:
        for particular_code in lest:
            if particular_code not in all_courses_list:
                all_courses_list.append(particular_code)
            else:
                pass

    #creates a dictionary maps course codes to the faculties which teach that course  , which in other words is reverse of previous mapping

    reverse_map = {}

    for particular in all_courses_list:
        reverse_map[particular] = []
        for x in data:
            if particular in data[x]:
                reverse_map[particular].append(x)

    # it adds semester details to each entry of a  dictionary for easy further use

    sem_named_dict = {}

    for entry in reverse_map:
        sem_named_dict[entry] = {sem_name: reverse_map[entry]}

    #appends the semester details to the master file containing all semesters data
    for the_course in all_courses_list:
        if the_course not in avalible_data:
            avalible_data[the_course]=sem_named_dict[the_course]
        elif the_course in avalible_data:
            avalible_data[the_course].update(sem_named_dict[the_course])
    #Re dumps the final file in form of json
    with open('Sem_wise_Course_Teaching_Faculties.json', 'w') as sem_file:
        json.dump(avalible_data, sem_file, indent=4)


who_taught_which_sem(all_facs,fac_info,sem_name)