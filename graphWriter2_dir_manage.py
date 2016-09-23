import os
import re

from graphWriter2_New import *

def driveFind():
    driveList = ['A:','B:','C:','D:','E:','F:','G:',\
                 'H:','I:','J:','K:','L:','M:','N:',\
                 'O:','P:','Q:','R:','S:','T:','U:',\
                 'V:','W:','X:','Y:','Z:']
    dir_ = ['PavementAnalysis','Pavemgmt','DATA_COLLECTION',\
            'AUTOMATED_VANS','02_COLLECTION_VEHICLES','01_CALIBRATION']
    for drives in driveList:
        n = 0
        letter = drives[n]+':/'
        if os.path.isdir(letter) == True:
            for strings in dir_:
                folders = letter+'\\\\'+strings
                if os.path.isdir(folders) == True:
                    m = dir_.index(strings)
                    while True:
                        m = m + 1
                        folders = folders+'\\\\'+dir_[m]
                        if dir_[m] == dir_[-1]:
                            return folders
                            break
                        else:continue
                else:break
            
def yearPrint():
    try:
        os.chdir(driveFind())
        os.chdir('.')
        for line in os.listdir(os.getcwd()):
            if re.search('calibrationFiles_',line):
                print 'Data available for: '+line[-4:]
    except WindowsError:
        print 'Drive not found'
    print''
            
def directory():
    yearPrint()
    while True:
        try:
            os.getcwd()
            print''
            year = raw_input('Enter a year or "done" to leave: ')
            dir_year = drivePrint()+'\\\\calibrationFiles_'+str(year)
            try:
                if os.path.isdir(dir_year) == True:
                    os.chdir(dir_year)
                    while True:
                        os.chdir(dir_year)
                        print''
                        print'-----------------------------------------------------------------------------'
                        print'Data available for: '+str(os.walk('.').next()[1])+' for year '+str(year)
                        print''
                        van = raw_input('Enter a van name, or enter "year" to leave: ')
                        try:
                            if van.lower() == 'north':
                                dir_van = dir_year+'\\\\North'
                                os.chdir(dir_van)
                                #print os.getcwd()
                                yield dir_van
                            elif van.lower() == 'south':
                                dir_van = dir_year+'\\\\South'
                                os.chdir(dir_van)
                                #print os.getcwd()
                                yield dir_van
                            elif van.lower() == 'east':
                                dir_van = dir_year+'\\\\East'
                                os.chdir(dir_van)
                                #print os.getcwd()
                                yield dir_van
                            elif van.lower() == 'west':
                                dir_van = dir_year+'\\\\West'
                                os.chdir(dir_van)
                                #print os.getcwd()
                                yield dir_van
                            elif van.lower() == 'year':
                                break
                            else:continue
                        except ValueError:
                            continue
                        except WindowsError:
                            continue
            except ValueError:
                continue
            if year.lower() == 'done':
                print'Have a nice day'
                break
        except WindowsError:
            print 'Drive not found'
            break
