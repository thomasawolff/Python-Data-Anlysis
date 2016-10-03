import os
import re
import sys

driveList = ['H:','Q:','R:','T:','Z:']

def missingFileSearch():
    d = 0
    collSet = []
    setList = []
    while d < len(driveList):
        os.chdir(driveList[d])
        for setFolder in os.listdir(os.getcwd()):
            if os.path.isdir(setFolder)==True and\
               (len(setFolder)==2 or\
                len(setFolder)==3) and\
                setFolder != 'sec':
                try:collSet.append(int(setFolder))
                except ValueError:pass
                for line in os.listdir(setFolder):
                    if ('prft000' in line or\
                       'PRFT000' in line):
                        try:setList.append(int(setFolder))
                        except ValueError:pass
        if driveList[d] == driveList[-1]:
            break
        d = d + 1
        continue
    return list(set(collSet)-set(setList))

def binarySearch():
    setFolder = []
    print missingFileSearch()
    for drives in driveList:
        os.chdir(drives)
        print 'Drive being scanned:',drives
        for line in os.listdir(os.getcwd()):
            if (len(line)==2 or len(line)==3)\
               and line != 'sec':
               try:setFolder.append(int(line))
               except ValueError:pass
        setFolder.sort()
        for value in missingFileSearch():
            [value].sort()
            first = 0 
            last = len(line)-1 
            found = False 
            while first<=last and not found: 
                midpoint = (first + last)//2 
                if setFolder[midpoint] == value: 
                    found = True
                else:
                    if value < setFolder[midpoint]: 
                        last = midpoint-1 
                    else: 
                        first = midpoint+1
            if found == True:
                print value,found,drives
            else:
                break
binarySearch()
