import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import os
from os import listdir
from PIL import Image
import shutil
from io import BytesIO

#val = {'2017Autumn': {'A': 12, 'C': 2, 'B': 3, 'D': 0, 'F': 0, 'P': 0, 'EX': 8}, '2018Spring': {'A': 6, 'C': 3, 'B': 6, 'D': 3, 'F': 0, 'P': 3, 'EX': 4}, '2016Spring': {'A': 2, 'C': 0, 'B': 1, 'D': 0, 'F': 0, 'P': 0, 'EX': 3}, '2017Spring': {'A': 12, 'C': 2, 'B': 3, 'D': 0, 'F': 0, 'P': 0, 'EX': 8}}


x_groups = ['EX', 'A', 'B', 'C', 'D', 'P', 'F']

def DrawLineHistorical():
    im = Image.open('Grades/Temp_files/HistoricalAverage.png')

    width, height = im.size
    for x in range(width):
        for y in range(12):
            im.putpixel((x,y),(146,138,138))
    
    im.save('Grades/Temp_files/HistoricalAverage.png')

def RemovePreviousStitichedImage(): #Deletes the previously stiched graph containg image.
    mydir = 'figure/'
    filelist = [ f for f in os.listdir(mydir) if f.endswith(".jpg") ]

    for f in filelist:
        os.remove(os.path.join(mydir, f))

def RemovePreviousInvidualGraphs(): #Deletes the previously stiched graph containg image.
    mydir = 'Grades/Temp_files/'
    filelist = [ f for f in os.listdir(mydir) if f.endswith(".png") ]

    for f in filelist:
        os.remove(os.path.join(mydir, f))


def CombineImage(val, code, number_courses): #Function to stich gaphs together into one image
    total_height = 0
    max_width = 0
    courses_available_sorted = []
    for semester, grades in val.items():
        im = Image.open('Grades/Temp_files/%s.png' % semester)
        width, height = im.size
        total_height = total_height + height
        max_width = max(max_width,width)
        courses_available_sorted.append(semester)

    courses_available_sorted.sort()
    #The following code is for historical average
    if(number_courses>1):
        im = Image.open('Grades/Temp_files/HistoricalAverage.png')
        width, height = im.size
        total_height = total_height + height
        max_width = max(max_width,width)
        courses_available_sorted.append('HistoricalAverage')
    
    img = Image.new('RGB', (max_width, total_height ))
    y_offset = 0

    for semester in courses_available_sorted:
        im = Image.open('Grades/Temp_files/%s.png' % semester)
        img.paste(im, (0,y_offset))
        y_offset += im.size[1]

    img.save('figure/%s.jpg' % code)
    RemovePreviousInvidualGraphs()
    

def GeneratePlots(x_groups,x,y_values,semester) :

        
        plt.bar(x,y_values)
        plt.title(semester)

        plt.ylabel('No of students')
        plt.xticks(x, x_groups)

        for i in range(0,7):
            if(y_values[i]>0):
                plt.text ( x = i-0.3, y = y_values[i]+0.005, s = y_values[i], size = 12)

        plt.savefig('Grades/Temp_files/%s.png' % semester)
        plt.close()


def MakeGraphs(val, code) :

    number_courses = 0
    total_grades = [0] * 7 #This variable stores sum of grades corresponding to EX, A, B, C, D, P, F

    #print("Makegraphbegin")
    for semester, grades in val.items():
        x = range(7)
        y_values = [grades['EX'],grades['A'],grades['B'],grades['C'],grades['D'],grades['P'],grades['F']]

        for i in range(7):
            total_grades[i] = total_grades[i] + y_values[i]

        GeneratePlots(x_groups,x,y_values,semester)
        number_courses = number_courses+1

    avg_grades = [0.0] * 7

    for i in range(7):
        avg_grades[i] = float(total_grades[i])/number_courses

    if(number_courses>1):
        GeneratePlots(x_groups,x,avg_grades,'HistoricalAverage')
        DrawLineHistorical()
    RemovePreviousStitichedImage()

    CombineImage(val, code, number_courses)
    #print ("Makegraph_end")

#MakeGraphs(val,'2')