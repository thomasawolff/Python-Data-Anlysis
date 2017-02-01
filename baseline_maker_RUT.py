import os
import re
import csv
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pylab

from textGrabber import * # import from the file that brings in text files

''' This program is meant to create a baseline graph for comparing to weekly
   5-miles verification data from the van. The data used in this code is Rut data
   which is acquired through text files from the textGrabber.py program. The text files
   are located on the sharedrive '''

def graphWriterRUT():
    
    rutRList1 = [] # empty lists for holding right and left Rut data from each text file
    rutLList1 = [] # being initiated
    rutRList2 = []
    rutLList2 = []
    rutRList3 = []
    rutLList3 = []
    rutRList4 = []
    rutLList4 = []
    rutRList5 = []
    rutLList5 = []
    rutRList6 = []
    rutLList6 = []
    rutRList7 = []
    rutLList7 = []
    rutRList8 = []
    rutLList8 = []
    rutRList9 = []
    rutLList9 = []
    rutRList10 = []
    rutLList10 = []
    rutRList11 = []
    rutLList11 = []
    rutRList12 = []
    rutLList12 = []
    
    try:
        for data in textGrab1(): # a function call to a textGrabber.py file
            for row in csv.DictReader(data): # reads data from text file
                try: # try the functionality below
                    rutRList1.append(float(row[' RUT R e'])) # append data to a list from above
                except KeyError:pass # if a KeyError exception occurs just pass and try next option
                try:
                    rutRList1.append(float(row[' RUT RWP'])) # row names must match whats listed 
                except KeyError:pass # KeyError occurs when a column name is incorrectly coded into program
                try:
                    rutLList1.append(float(row[' RUT L e'])) # the string is the column name from the text file
                except KeyError:pass
                try:
                    rutLList1.append(float(row[' RUT LWP']))
                except KeyError:pass
    except NameError:pass # if the file is not present pass
    
    try:            
        for data in textGrab2(): # a function from the textGrabber file
            for row in csv.DictReader(data): # reads data from text file
                try:    
                    rutRList2.append(float(row[' RUT R e'])) # append data to a list from above
                except KeyError:pass
                try:
                    rutRList2.append(float(row[' RUT RWP']))
                except KeyError:pass
                try:
                    rutLList2.append(float(row[' RUT L e']))
                except KeyError:pass
                try:
                    rutLList2.append(float(row[' RUT LWP']))
                except KeyError:pass
    except NameError:pass
    

    try:
        for data in textGrab3(): # a function from the textGrabber file
            for row in csv.DictReader(data): # reads data from text file
                try:    
                    rutRList3.append(float(row[' RUT R e'])) # append data to a list from above
                except KeyError:pass
                try:
                    rutRList3.append(float(row[' RUT RWP']))
                except KeyError:pass
                try:
                    rutLList3.append(float(row[' RUT L e']))
                except KeyError:pass
                try:
                    rutLList3.append(float(row[' RUT LWP']))
                except KeyError:pass
    except NameError:pass

    try:
        for data in textGrab4(): # a function from the textGrabber file
            for row in csv.DictReader(data):
                try:    
                    rutRList4.append(float(row[' RUT R e']))
                except KeyError:pass
                try:
                    rutRList4.append(float(row[' RUT RWP']))
                except KeyError:pass
                try:
                    rutLList4.append(float(row[' RUT L e']))
                except KeyError:pass
                try:
                    rutLList4.append(float(row[' RUT LWP']))
                except KeyError:pass
    except NameError:pass

    try:
        for data in textGrab5(): # a function from the textGrabber file
            for row in csv.DictReader(data):
                try:    
                    rutRList5.append(float(row[' RUT R e']))
                except KeyError:pass
                try:
                    rutRList5.append(float(row[' RUT RWP']))
                except KeyError:pass
                try:
                    rutLList5.append(float(row[' RUT L e']))
                except KeyError:pass
                try:
                    rutLList5.append(float(row[' RUT LWP']))
                except KeyError:pass
    except NameError:pass

    try:
        for data in textGrab6(): 
            for row in csv.DictReader(data):
                try:    
                    rutRList6.append(float(row[' RUT R e']))
                except KeyError:pass
                try:
                    rutRList6.append(float(row[' RUT RWP']))
                except KeyError:pass
                try:
                    rutLList6.append(float(row[' RUT L e']))
                except KeyError:pass
                try:
                    rutLList6.append(float(row[' RUT LWP']))
                except KeyError:pass
    except NameError:pass

    try:
        for data in textGrab7():
            for row in csv.DictReader(data):
                try:    
                    rutRList7.append(float(row[' RUT R e']))
                except KeyError:pass
                try:
                    rutRList7.append(float(row[' RUT RWP']))
                except KeyError:pass
                try:
                    rutLList7.append(float(row[' RUT L e']))
                except KeyError:pass
                try:
                    rutLList7.append(float(row[' RUT LWP']))
                except KeyError:pass
    except NameError:pass

    try:
        for data in textGrab8():
            for row in csv.DictReader(data):
                try:    
                    rutRList8.append(float(row[' RUT R e']))
                except KeyError:pass
                try:
                    rutRList8.append(float(row[' RUT RWP']))
                except KeyError:pass
                try:
                    rutLList8.append(float(row[' RUT L e']))
                except KeyError:pass
                try:
                    rutLList8.append(float(row[' RUT LWP']))
                except KeyError:pass
    except NameError:pass

    try:
        for data in textGrab9():
            for row in csv.DictReader(data):
                try:    
                    rutRList9.append(float(row[' RUT R e']))
                except KeyError:pass
                try:
                    rutRList9.append(float(row[' RUT RWP']))
                except KeyError:pass
                try:
                    rutLList9.append(float(row[' RUT L e']))
                except KeyError:pass
                try:
                    rutLList9.append(float(row[' RUT LWP']))
                except KeyError:pass
    except NameError:pass

    try:
        for data in textGrab10():
            for row in csv.DictReader(data):
                try:    
                    rutRList10.append(float(row[' RUT R e']))
                except KeyError:pass
                try:
                    rutRList10.append(float(row[' RUT RWP']))
                except KeyError:pass
                try:
                    rutLList10.append(float(row[' RUT L e']))
                except KeyError:pass
                try:
                    rutLList10.append(float(row[' RUT LWP']))
                except KeyError:pass
    except NameError:pass

    '''This code returns all of the lists that were appended to above. Each one
       of these lists can be accessed by indexing the function call as shown below'''
    
    try: return rutRList1,rutLList1,rutRList2,rutLList2,rutRList3,rutLList3,\
           rutRList4,rutLList4,rutRList5,rutLList5,rutRList6,rutLList6,\
           rutRList7,rutLList7,rutRList8,rutLList8,rutRList9,rutLList9,\
           rutRList10,rutLList10,rutRList11,rutLList11,rutRList12,rutLList12
    except NameError: pass
    except IOError: pass


def dataZipp():
    RUTplotR = [] # initiating new lists
    RUTplotL = []
    startList = []
    endList = []
    plt.subplot(2, 1, 1) # setting the dialog box for the 1st subplot
    plt.grid(True) # sets a grid for subplot
    plt.ylabel('IRI value', fontsize=12)
    pylab.ylim([0,.40]) # limits y axis values for 1st subplot
    plt.title('Baseline Right RUT data per mile')
    plt.tick_params(axis='both', which='major', labelsize=8)
    plt.hold(True)
    plt.subplot(2, 1, 2) # setting the dialog box for the 2nd subplot
    plt.grid(True)
    plt.ylabel('IRI value', fontsize=12)
    pylab.ylim([0,.40]) # limits y axis values for 1st subplot
    plt.title('Baseline Left RUT data per mile:')
    plt.tick_params(axis='both', which='major', labelsize=8)
    plt.hold(True)
    try:
        for data in textGrab1():
            for row in csv.DictReader(data):
                try: # try the functionality below
                    startList.append(float(row['Start-Mi']))  # gets start and end miles
                    endList.append(float(row['  End-Mi']))    # from a text file  
                except KeyError: # KeyError occurs when a column name is incorrectly coded into program
                    startList.append(float(row['Start-MP']))
                    endList.append(float(row['  End-MP']))
    except IOError: # if this occurs the name of the baseline file may be incorrect
        print'Error: Did you name the file correctly as BASELINE1.TXT?'
        sys.exit(0) # exits from the program

    '''This code uses zip() which transposes the lists from the graphWriter() function
       then takes the average of the transposed data. It then appends the data to a
       list which is then plotted below. Each function call is an index to the list being
       returned from the function. Odd numbers are Right Rut and even number indexes are Left Rut data'''
    
    for column1 in zip(graphWriterRUT()[1],graphWriterRUT()[3],graphWriterRUT()[5],\
                       graphWriterRUT()[7],graphWriterRUT()[9],graphWriterRUT()[11],\
                       graphWriterRUT()[13],graphWriterRUT()[15],\
                       graphWriterRUT()[17],graphWriterRUT()[19]):
        RUTplotR.append(round(np.average(column1),4)) # list averaged Rut data for right laser
                                                      # rounded to four leading digits

    for column2 in zip(graphWriterRUT()[0],graphWriterRUT()[2],graphWriterRUT()[4],\
                       graphWriterRUT()[6],graphWriterRUT()[8],graphWriterRUT()[10],\
                       graphWriterRUT()[12],graphWriterRUT()[14],\
                       graphWriterRUT()[16],graphWriterRUT()[18]):
        RUTplotL.append(round(np.average(column2),4)) # list of averaged Rut data for left laser
                                                      # rounded to four leading digits

    '''This is where the plotting of the average Rut data is done. There are two
    subplots, one for right and one for left'''
    try:
        plt.subplot(2, 1, 1) # first subplot box
        plt.plot(startList,RUTplotR) # plot startmiles as X and Right Rut data as Y
        lines = plt.plot(startList,RUTplotR)
        plt.setp(lines, color='y', linewidth=5.0) # adjusting the plot lines properties
        plt.subplot(2, 1, 2)
        plt.plot(startList,RUTplotL) # plot startmiles as X and left Rut data as Y
        lines = plt.plot(startList,RUTplotL)
        plt.setp(lines, color='y', linewidth=5.0)
    except ValueError:pass

    plt.show() # show the plots very important command
    plt.close('all')

dataZipp()





    



    
    
