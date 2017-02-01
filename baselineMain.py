import os
import csv
import re
import glob
import sys
import pprint as p
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pylab

#os.chdir('y:\\\\PavementAnalysis\\\\Pavemgmt\\\\DATA_COLLECTION\\\\AUTOMATED_VANS\\\\02_COLLECTION_VEHICLES\\\\01_CALIBRATION\\\\calibrationFiles_2015\\\\North')

'''This code will take initial user input from the graphWriter2_manage.py code on line 103.
If the user enters Y then this code will be called. It will then graph or visualize the data
from a chosen .TXT file against averaged baseline data from a .csv file.
Like the others this code is activated in graphing_final_consol.py'''

def baseLineWriter():
        
    rwpIRIavg = [] # initializing empty lists for csv files
    lwpIRIavg = []
    rwpRUTavg = []
    lwpRUTavg = []
    
    files = [x for x in os.listdir(os.getcwd()) if x.endswith('.csv')] # searches for files ending in .csv
    for line in files:
        if re.search('RWP_IRI_baseline_',line): # searches for files with 'baseline' in file name
            with open(line,'rU') as file1: # opening .csv files for baseline data
                for row in csv.DictReader(file1):
                    rwpIRIavg.append(float(row['Average']))

        if re.search('LWP_IRI_baseline_',line): # searches for files with 'baseline' in file name
            with open(line,'rU') as file2:
                for row in csv.DictReader(file2):
                    lwpIRIavg.append(float(row['Average']))

        if re.search('RWP_RUT_baseline_',line): # searches for files with 'baseline' in file name
            with open(line,'rU') as file3:
                for row in csv.DictReader(file3):
                    rwpRUTavg.append(float(row['Average']))

        if re.search('LWP_RUT_baseline_',line): # searches for files with 'baseline' in file name
            with open(line,'rU') as file4:
                for row in csv.DictReader(file4):
                    lwpRUTavg.append(float(row['Average']))
    
    while True: # until this loop is broken, keep running code below
        
        try:
            print'-----------------------------------------------------------------------------'
            print'The length of current baseline dataset is:',len(rwpIRIavg)
            print''
            numRows = raw_input('Number of rows in baseline dataset (press enter if 50 or "done"): ')
            print''
            
            if numRows == 'done': break # leave loop if user enters "done"
            elif numRows == '': # if user leaves it empty and presses enter
                row_num = 50 # 50 is defualt setting for our verification 5 mile drive
                pass 
            else:
                row_num = int(numRows)
            
            startList = [] # initializing empty lists for .TXT files
            endList = [] # lists are emptied every iteration of while loop
            iriRList = []
            iriLList = []
            rutRList = []
            rutLList = []
            
            try:
                files = [x for x in os.listdir(os.getcwd()) if x.endswith('.TXT')] # searches for files ending with .TXT
                for positions,items in enumerate(files): # lists files and the positions of this files
                    print positions,':',items # prints the indexed position and name of each file
                print''
                newest = raw_input('Enter a file number to compare for baseline or enter "done": ')
                print''
                if newest.lower() == 'done': break # leave loop if user enters "done"
                else:
                    for positions,items in enumerate(files): # for the position and name of each file in the files list
                        if positions == int(newest): # if user chooses a file number that exists
                            with open(items, 'rU') as file: # open the file chosen by the user
                                for row in csv.DictReader(file): 
                                    try:
                                        startList.append(float(row['Start-Mi'])) # appends the columns of data from csv into empty lists
                                        endList.append(float(row['  End-Mi']))
                                    except KeyError:
                                        startList.append(float(row['Start-MP']))
                                        endList.append(float(row['  End-MP']))
                                    try:
                                        iriRList.append(float(row[' IRI R e']))
                                        iriLList.append(float(row['IRI LWP ']))
                                    except KeyError:
                                        iriRList.append(float(row[' IRI RWP']))
                                        iriLList.append(float(row['IRI LWP ']))
                                    try:    
                                        rutRList.append(float(row[' RUT R e']))
                                    except KeyError:pass
                                    try:
                                        rutRList.append(float(row[' RUT RWP']))
                                    except KeyError:pass
                                    try:
                                        rutLList.append(float(row[' RUT L e']))
                                    except KeyError:pass
                                    try:
                                        rutLList.append(float(row[' RUT LWP']))
                                    except KeyError:pass

            except ValueError: continue

            try:
                plt.subplot(2, 1, 1) # top graph plot in the window of two
                plt.grid(True) # show grid in the graph box
                plt.ylabel('IRI value', fontsize=12)
                pylab.ylim([0,300]) # limit of Y value in graph
                plt.title('Right IRI data per mile vs Baseline data')
                plt.tick_params(axis='both', which='major', labelsize=8)
                plt.hold(True)
                baseline2 = plt.plot(startList[:row_num],lwpIRIavg[:row_num]) # baseline plot indexed to the value of 
                plt.setp(baseline2, color='y', linewidth=5.0)                 # beginning of dataset to the value of row_num
                plt.plot(startList[:row_num],iriLList[:row_num])              # that was entered by user above
                plt.legend(['Baseline']) # graph legend

                plt.subplot(2, 1, 2)
                plt.grid(True)
                plt.ylabel('IRI value', fontsize=12)
                pylab.ylim([0,300])
                plt.title('Left IRI data per mile vs Baseline data:')
                plt.tick_params(axis='both', which='major', labelsize=8)
                plt.hold(True)
                baseline1 = plt.plot(startList[:row_num],rwpIRIavg[:row_num])
                plt.setp(baseline1, color='y', linewidth=5.0)
                plt.plot(startList[:row_num],iriRList[:row_num])

                plt.show()
            except ValueError: # errors will show if lengths of baseline,IRI or Rut data are not matched.
                print''
                print'Check dataset length'
                print'Length of baseline field:',len(rwpIRIavg)
                print'Length of IRI data field:',len(iriRList)
                print'Length of Rut data field:',len(rwpRUTavg)
                print''
                continue
            
            try:
                plt.subplot(2, 1, 1)
                plt.grid(True)
                plt.ylabel('RUT value', fontsize=12)
                pylab.ylim([0,.40])
                plt.title('Right RUT data per mile vs Baseline data')
                plt.tick_params(axis='both', which='major', labelsize=8)
                plt.hold(True)
                baseline2 = plt.plot(startList[:row_num],lwpRUTavg[:row_num])
                plt.setp(baseline2, color='y', linewidth=5.0)
                plt.plot(startList[:row_num],rutLList[:row_num])
                plt.legend(['Baseline'])

                plt.subplot(2, 1, 2)
                plt.grid(True)
                plt.ylabel('RUT value', fontsize=12)
                pylab.ylim([0,.40])
                plt.title('Left RUT data per mile vs Baseline data:')
                plt.tick_params(axis='both', which='major', labelsize=8)
                plt.hold(True)
                baseline1 = plt.plot(startList[:row_num],rwpRUTavg[:row_num])
                plt.setp(baseline1, color='y', linewidth=5.0)
                plt.plot(startList[:row_num],rutRList[:row_num])

                plt.show()
            except ValueError: 
                continue
        except ValueError: break
    
    plt.close('all')

#baseLineWriter()

