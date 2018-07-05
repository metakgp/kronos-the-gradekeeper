import matplotlib.pyplot as plt
import sys
import os
from os import listdir
from PIL import Image
import shutil

#val = {'2017Autumn': {'A': 12, 'C': 2, 'B': 3, 'D': 0, 'F': 0, 'P': 0, 'EX': 8}, '2018Spring': {'A': 6, 'C': 3, 'B': 6, 'D': 3, 'F': 0, 'P': 3, 'EX': 4}, '2016Spring': {'A': 2, 'C': 0, 'B': 1, 'D': 0, 'F': 0, 'P': 0, 'EX': 3}, '2017Spring': {'A': 12, 'C': 2, 'B': 3, 'D': 0, 'F': 0, 'P': 0, 'EX': 8}}

def RemovePreviousImage():
    mydir = 'figure/'
    filelist = [ f for f in os.listdir(mydir) if f.endswith(".jpg") ]
    for f in filelist:
        os.remove(os.path.join(mydir, f))

def CombineImage(val, code):
    list_graphs = []
    for semester, grades in val.iteritems():
        list_graphs.append('Grades/Temp_files/%s.png' % semester)
        list_graphs.sort()

    images = map(Image.open, list_graphs)
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height = max(heights)
    new_im = Image.new('RGB', (total_width, max_height))
    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]

    new_im.save('figure/%s.jpg' % code)

    for deleteImage in list_graphs:
        os.remove('%s' % deleteImage)


def MakeGraphs(val, code) :
    numberOfImage=0
    for semester, grades in val.iteritems():
        x_groups = ['EX', 'A', 'B', 'C', 'D', 'P', 'F']
        y_values = [grades['EX'],grades['A'],grades['B'],grades['C'],grades['D'],grades['P'],grades['F']]
        plt.bar(x_groups,y_values)
        plt.title(semester)
        plt.ylabel('No of students')
        plt.savefig('Grades/Temp_files/%s.png' % semester)
        plt.close()
        numberOfImage = numberOfImage+1

    RemovePreviousImage()
    CombineImage(val, code)


#MakeGraphs(val)