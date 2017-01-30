import os
import re
import csv
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pylab

from textGrabber import * # import from the file that brings in text files

''' This program is meant to create a baseline graph for comparing to weekly
   5-miles verification data from the van. The data used in this code is IRI data
   which is acquired through text files from the textGrabber.py program. The text files
   are located on the sharedrive '''

def graphWriterIRI():
    iriRList1 = [] # empty lists for holding right and left IRI data from each text file
    iriLList1 = [] # being initiated
    iriRList2 = []
    iriLList2 = []
    iriRList3 = [] # empty lists for holding right IRI data from text file 3
    iriLList3 = [] # empty lists for holding left IRI data from text file 3
    iriRList4 = []
    iriLList4 = []
    iriRList5 = []
    iriLList5 = []
    iriRList6 = []
    iriLList6 = []
    iriRList7 = []
    iriLList7 = []
    iriRList8 = []
    iriLList8 = []
    iriRList9 = []
    iriLList9 = []
    iriRList10 = []
    iriLList10 = []
    iriRList11 = []
    iriLList11 = []
    iriRList12 = []
    iriLList12 = []
    
    try:
        for data in textGrab1(): # a function call to a textGrabber.py file
            for row in csv.DictReader(data): # reads data from text file
                try: # try the functionality below
                    iriRList1.append(float(row[' IRI R e'])) # append data to a list from above
                    iriLList1.append(float(row['IRI LWP '])) 
                except KeyError: # if a KeyError exception occurs just pass and try next option
                    iriRList1.append(float(row[' IRI RWP']))
                    iriLList1.append(float(row['IRI LWP ']))# KeyError occurs when a column name is incorrectly coded into program
    except NameError:pass # if the file is not present pass
    
    try:            
        for data in textGrab2():
            for row in csv.DictReader(data):
                try:
                    iriRList2.append(float(row[' IRI R e']))
                    iriLList2.append(float(row['IRI LWP ']))
                except KeyError:
                    iriRList2.append(float(row[' IRI RWP']))
                    iriLList2.append(float(row['IRI LWP ']))
    except NameError:pass
    

    try:
        for data in textGrab3():
            for row in csv.DictReader(data):
                try:
                    iriRList3.append(float(row[' IRI R e']))
                    iriLList3.append(float(row['IRI LWP ']))
                except KeyError:
                    iriRList3.append(float(row[' IRI RWP']))
                    iriLList3.append(float(row['IRI LWP ']))
    except NameError:pass

    try:
        for data in textGrab4():
            for row in csv.DictReader(data):
                try:
                    iriRList4.append(float(row[' IRI R e']))
                    iriLList4.append(float(row['IRI LWP ']))
                except KeyError:
                    iriRList4.append(float(row[' IRI RWP']))
                    iriLList4.append(float(row['IRI LWP ']))
    except NameError:pass

    try:
        for data in textGrab5():
            for row in csv.DictReader(data):
                try:
                    iriRList5.append(float(row[' IRI R e']))
                    iriLList5.append(float(row['IRI LWP ']))
                except KeyError:
                    iriRList5.append(float(row[' IRI RWP']))
                    iriLList5.append(float(row['IRI LWP ']))
    except NameError:pass

    try:
        for data in textGrab6():
            for row in csv.DictReader(data):
                try:
                    iriRList6.append(float(row[' IRI R e']))
                    iriLList6.append(float(row['IRI LWP ']))
                except KeyError:
                    iriRList6.append(float(row[' IRI RWP']))
                    iriLList6.append(float(row['IRI LWP ']))
    except NameError:pass

    try:
        for data in textGrab7():
            for row in csv.DictReader(data):
                try:
                    iriRList7.append(float(row[' IRI R e']))
                    iriLList7.append(float(row['IRI LWP ']))
                except KeyError:
                    iriRList7.append(float(row[' IRI RWP']))
                    iriLList7.append(float(row['IRI LWP ']))
    except NameError:pass

    try:
        for data in textGrab8():
            for row in csv.DictReader(data):
                try:
                    iriRList8.append(float(row[' IRI R e']))
                    iriLList8.append(float(row['IRI LWP ']))
                except KeyError:
                    iriRList8.append(float(row[' IRI RWP']))
                    iriLList8.append(float(row['IRI LWP ']))
    except NameError:pass

    try:
        for data in textGrab9():
            for row in csv.DictReader(data):
                try:
                    iriRList9.append(float(row[' IRI R e']))
                    iriLList9.append(float(row['IRI LWP ']))
                except KeyError:
                    iriRList9.append(float(row[' IRI RWP']))
                    iriLList9.append(float(row['IRI LWP ']))
    except NameError:pass

    try:
        for data in textGrab10():
            for row in csv.DictReader(data):
                try:
                    iriRList10.append(float(row[' IRI R e']))
                    iriLList10.append(float(row['IRI LWP ']))
                except KeyError:
                    iriRList10.append(float(row[' IRI RWP']))
                    iriLList10.append(float(row['IRI LWP ']))
    except NameError:pass

    '''This code returns all of the lists that were appended to above. Each one
       of these lists can be accessed by indexing the function call as shown below'''
    
    try: return iriRList1,iriLList1,iriRList2,iriLList2,iriRList3,iriLList3,\
           iriRList4,iriLList4,iriRList5,iriLList5,iriRList6,iriLList6,\
           iriRList7,iriLList7,iriRList8,iriLList8,iriRList9,iriLList9,\
           iriRList10,iriLList10,iriRList11,iriLList11,iriRList12,iriLList12
    except NameError: pass
    except IOError: pass


def dataZipp():
    IRIplotR = [] # initiating new lists
    IRIplotL = []
    startList = []
    endList = []
    plt.subplot(2, 1, 1) # setting the dialog box for the 1st subplot
    plt.grid(True) # sets a grid for subplot
    plt.ylabel('IRI value', fontsize=12)
    pylab.ylim([0,150]) # limits y axis values for 1st subplot
    plt.title('Baseline Right IRI data per mile') # title of subplot box
    plt.tick_params(axis='both', which='major', labelsize=8)
    plt.hold(True)
    plt.subplot(2, 1, 2) # setting the dialog box for the 2nd subplot
    plt.grid(True)
    plt.ylabel('IRI value', fontsize=12)
    pylab.ylim([0,150]) # limits y axis values for 1st subplot
    plt.title('Baseline Left IRI data per mile:')
    plt.tick_params(axis='both', which='major', labelsize=8)
    plt.hold(True)
    try:
        for data in textGrab1():
            for row in csv.DictReader(data):
                try: # try the functionality below
                    startList.append(float(row['Start-Mi'])) # gets start and end miles
                    endList.append(float(row['  End-Mi']))   # from a text file  
                except KeyError: # KeyError occurs when a column name is incorrectly coded into program
                    startList.append(float(row['Start-MP']))
                    endList.append(float(row['  End-MP']))
    except IOError: # if this occurs the name of the baseline file may be incorrect
        print'Error: Did you name the file correctly as BASELINE1.TXT?'
        sys.exit(0) # exits from the program
        
    '''This code uses zip() which transposes the lists from the graphWriter() function
       then takes the average of the transposed data. It then appends the data to a
       list which is then plotted below. Each function call graphWriterIRI()[n] is an index to the list being
       returned from the function. Odd numbers are Right IRI and even number indexes are Left IRI'''
        
    for column1 in zip(graphWriterIRI()[1],graphWriterIRI()[3],graphWriterIRI()[5],\
                       graphWriterIRI()[7],graphWriterIRI()[9],graphWriterIRI()[11],\
                       graphWriterIRI()[13],graphWriterIRI()[15],\
                       graphWriterIRI()[17],graphWriterIRI()[19]):
        IRIplotR.append(round(np.average(column1),4)) # list averaged IRI data for right laser
                                                      # rounded to four leading digits
        
    for column2 in zip(graphWriterIRI()[0],graphWriterIRI()[2],graphWriterIRI()[4],\
                       graphWriterIRI()[6],graphWriterIRI()[8],graphWriterIRI()[10],\
                       graphWriterIRI()[12],graphWriterIRI()[14],\
                       graphWriterIRI()[16],graphWriterIRI()[18]):
        IRIplotL.append(round(np.average(column2),4)) # list averaged IRI data for left laser
                                                      # rounded to four leading digits
    try:
        plt.subplot(2, 1, 1) # first subplot box
        plt.plot(startList,IRIplotR) # plot startmiles as X and Right IRI data as Y
        lines = plt.plot(startList,IRIplotR)
        plt.setp(lines, color='y', linewidth=5.0) # adjusting the plot lines properties
        plt.subplot(2, 1, 2)
        plt.plot(startList,IRIplotL)
        lines = plt.plot(startList,IRIplotL) # plot startmiles as X and left IRI data as Y
        plt.setp(lines, color='y', linewidth=5.0)
    except ValueError:pass

    plt.show() # show the plots very important command
    plt.close('all')

dataZipp()





    



    
    
