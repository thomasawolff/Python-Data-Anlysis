
import os
import sys

driveList = ['z:','q:','r:','w:']

def missingFileSearch():
    n = 0
    d = 0
    collSet = []
    setList = []
    while True:
        os.chdir(driveList[d])
        print 'Drive being scanned:',driveList[d]
        for setFolder in os.listdir(os.getcwd()):
            if os.path.isdir(setFolder)==True and \
               len(setFolder)==3 and setFolder != 'sec':
                collSet.append(os.listdir(setFolder))
                if (('prft')+'0002.'+setFolder) or\
                (('PRFT')+'0002.'+setFolder) in collSet[n]:
                    pass
                else:
                    try:setList.append(int(setFolder))
                    except ValueError:pass
                n = n + 1
        if driveList[d] == driveList[-1]:
            sys.exit(0)
        else:
            d = d + 1
            continue
    return setList

def binarySearch():
    n = 0
    d = 0
    setFolder = []
    while True:
        os.chdir(driveList[d]) 
        print''
        print os.getcwd()
        for line in os.listdir(os.getcwd()):
            if len(line)==3 and line != 'sec':
                setFolder.append(int(line)) 
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
        print setFolder
        d = d + 1
        continue
binarySearch()
