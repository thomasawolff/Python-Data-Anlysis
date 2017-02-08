import os
import re
import sys

'''This program manages the entry of information from the user. It begins by changing the
directory of the program to the sharedrive path shown below:
'PavementAnalysis\Pavemgmt\DATA_COLLECTION\AUTOMATED_VANS\02_COLLECTION_VEHICLES\01_CALIBRATION'
it then asks the user to enter the year of data the want to see. From that point
information is entered about the van number. Once this data is entered the desired data visualization
will be displayed through graphWriter2_New.py and baseLineWriter.py if the baseline data is available. 
This code is run from the graphing_final_consol.py program'''

from graphWriter2_New import *
from driveAlgorithm import *
from baselineMain import *

def yearPrint():
    try:
        os.chdir(str(driveFind())) # try changing directory to the path created in the driveFind() code
    except WindowsError: # if this fails try the driveFindNewAlg() shown below the driveFind() code
        if os.path.isdir(driveFindNewAlg()) == True:
            os.chdir(str(driveFindNewAlg()))
            pass
        else:
            print'Cannot find drive'
            sys.exit(0) # exits from system if sharedrive path cannot be found
    os.chdir('.') 
    print''
    for line in os.listdir(os.getcwd()): # get list of files in current directory
        if re.search('calibrationFiles_',line): # look for folders named 'calibrationFiles'
            print 'Data available for: '+line[-4:] # prints the years the data is available for viewing

def directory():
    while True: # stays in the loop asking for input
        yearPrint() # yearPrint function is callled
        print''
        os.getcwd()
        print''
        year = raw_input('Enter a year or "done" to leave: ') # user input is entered
        print''
        dir_year = driveFind()+'\\\\calibrationFiles_'+str(year) # directory path is created 
        if os.path.isdir(dir_year) == True: # if dir_year is a directory
            os.chdir(dir_year) # change directory to dir_year
            while True: # stays in the loop asking for input
                os.chdir(dir_year) # keeps the directory in dir_year
                print''
                print'-----------------------------------------------------------------------------'
                ''' this code prints the years for which viewable data is available
                    for visualization by looking one folder up and checking if
                    data exists. If data is available the that year is shown as
                    a possible entry'''
                print''
                print'Data available for: '+str(os.walk('.').next()[1])+' for year '+str(year)
                print''
                van = raw_input('Enter a van name, or enter "done" to leave: ') # enter van name north,south,east or west
                print''
                try:
                    if van.lower() == 'north': # if input = north
                        dir_van = dir_year+'\\\\North' # append 'north' to original directory path
                        os.chdir(dir_van) # change directory to dir_van
                        yield dir_van  # sends new directory to graphWriter2_New.py
                        files = [x for x in os.listdir(os.getcwd()) if x.endswith('.csv')] # searches for files ending in .csv
                        for line in files:
                            if re.search('baseline',line): # searches for files with 'baseline' in file name
                                info=raw_input('Baseline data is available: press Y or enter "done": ')
                                print''
                                if info.lower() == 'y':baseLineWriter() # function call the baseLineWriter() in baselineMain.py
                                elif info.lower()=='done': break # if user enters "done" leave loop
                                else:continue
                            else:pass
                    elif van.lower() == 'south': # or other directions entered
                        dir_van = dir_year+'\\\\South'
                        os.chdir(dir_van)
                        yield dir_van
                        files = [x for x in os.listdir(os.getcwd()) if x.endswith('.csv')]
                        for line in files:
                            if re.search('baseline',line):
                                info=raw_input('Baseline data is available: press Y or enter "done": ')
                                print''
                                if info.lower() == 'y':baseLineWriter()
                                elif info.lower()=='done':break
                                else:continue
                            else:pass
                    elif van.lower() == 'east':
                        dir_van = dir_year+'\\\\East'
                        os.chdir(dir_van)
                        yield dir_van
                        files = [x for x in os.listdir(os.getcwd()) if x.endswith('.csv')]
                        for line in files:
                            if re.search('baseline',line):
                                info=raw_input('Baseline data is available: press Y or enter "done": ')
                                print''
                                if info.lower() == 'y':baseLineWriter()
                                elif info.lower()=='done':break
                                else:continue
                            else:pass
                    elif van.lower() == 'west':
                        dir_van = dir_year+'\\\\West'
                        os.chdir(dir_van)
                        yield dir_van
                        files = [x for x in os.listdir(os.getcwd()) if x.endswith('.csv')]
                        for line in files:
                            if re.search('baseline',line):
                                info=raw_input('Baseline data is available: press Y or enter "done": ')
                                print''
                                if info.lower() == 'y':baseLineWriter()
                                elif info.lower()=='done':break
                                else:continue
                            else:pass
                    elif van.lower() == 'done': # if user enters 'year'
                        break # break from loop and go back one step
                    else:continue # else continue within current loop
                except ValueError: # handles bad user input
                    continue # nevermind/ignore bad user input and ask question again
                except WindowsError:
                    continue
        if year == 'done':
            print'Have a nice day' # Have a nice day!!
            break








##def driveFind():
##    driveList = ['A:','B:','C:','D:','E:','F:','G:',\
##                 'H:','I:','J:','K:','L:','M:','N:',\
##                 'O:','P:','Q:','R:','S:','T:','U:',\
##                 'V:','W:','X:','Y:','Z:']
##    dir_ = ['PavementAnalysis','Pavemgmt','DATA_COLLECTION',\
##            'AUTOMATED_VANS','02_COLLECTION_VEHICLES','01_CALIBRATION']
##    for drives in driveList:
##        n = 0
##        letter = drives[n]+':'
##        if os.path.isdir(letter) == True:
##            while True:
##                folders = letter+'\\'+dir_[n]
##                n = n + 1
##                if os.path.isdir(folders) == True:
##                    m = dir_.index(dir_[n])
##                    while True:
##                        m = m + 1
##                        folders = folders+'\\'+dir_[m]
##                        if dir_[m] == dir_[-1]:
##                            return folders
##                        else:continue
##                if n == len(dir_):break
