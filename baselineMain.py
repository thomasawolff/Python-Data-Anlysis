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

def baseLineWriter():
        
    while True:
        rwpIRIavg = []
        lwpIRIavg = []
        rwpRUTavg = []
        lwpRUTavg = []

        with open('baselineNorth2015_RWP_IRI.csv','rU') as file1:
            for row in csv.DictReader(file1):
                rwpIRIavg.append(float(row['Average'][:]))

        with open('baselineNorth2015_LWP_IRI.csv','rU') as file2:
            for row in csv.DictReader(file2):
                lwpIRIavg.append(float(row['Average'][:]))

        with open('baselineNorth2015_RWP_RUT.csv','rU') as file1:
            for row in csv.DictReader(file1):
                rwpRUTavg.append(float(row['Average'][:]))

        with open('baselineNorth2015_LWP_RUT.csv','rU') as file2:
            for row in csv.DictReader(file2):
                lwpRUTavg.append(float(row['Average'][:]))

        try:
            print'-----------------------------------------------------------------------------'
            print'The length of current baseline dataset is:',len(rwpIRIavg)
            print''
            numRows = raw_input('Number of rows in baseline dataset (press enter if 50 or "done"): ')
            print''
            if numRows == 'done':break
            elif numRows == '':
                row_num = 50
                pass
            else:
                row_num = int(numRows)

            while True:

                files = [x for x in os.listdir(os.getcwd()) if x.endswith('.TXT')]
                for positions,items in enumerate(files):
                    print positions,':',items
                print''
                
                startList = []
                endList = []
                iriRList = []
                iriLList = []
                rutRList = []
                rutLList = []
                try:
                    newest = raw_input('Enter a file number to compare for baseline or enter "done": ')
                    print''
                    if newest.lower() == 'done': sys.exit(0)
                    else:
                        for positions,items in enumerate(files):
                            if positions == int(newest):
                                with open(items, 'rU') as file:
                                    for row in csv.DictReader(file): 
                                        try:
                                            startList.append(float(row['Start-Mi']))
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
                    plt.subplot(2, 1, 1)
                    plt.grid(True)
                    plt.ylabel('IRI value', fontsize=12)
                    pylab.ylim([0,140])
                    plt.title('Right IRI data per mile vs Baseline data')
                    plt.tick_params(axis='both', which='major', labelsize=8)
                    plt.hold(True)
                    baseline2 = plt.plot(startList[:row_num],lwpIRIavg[:row_num])
                    plt.setp(baseline2, color='y', linewidth=5.0)
                    plt.plot(startList[:row_num],iriLList[:row_num])
                    plt.legend(['Baseline'])

                    plt.subplot(2, 1, 2)
                    plt.grid(True)
                    plt.ylabel('IRI value', fontsize=12)
                    pylab.ylim([0,140])
                    plt.title('Left IRI data per mile vs Baseline data:')
                    plt.tick_params(axis='both', which='major', labelsize=8)
                    plt.hold(True)
                    baseline1 = plt.plot(startList[:row_num],rwpIRIavg[:row_num])
                    plt.setp(baseline1, color='y', linewidth=5.0)
                    plt.plot(startList[:row_num],iriRList[:row_num])

                    plt.show()
                except ValueError: continue
                
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
                except ValueError: continue
        except ValueError: continue
        
    plt.close('all')

#baseLineWriter()

