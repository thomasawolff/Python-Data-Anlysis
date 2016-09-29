import os

def missingFileSearch():
    n = 0
    collSet = []
    driveList = []
    setList = []
    driveList.append('drive 1 to be scanned')
    driveList.append('drive 2 to be scanned')
    driveList.append('drive 3 to be scanned')
    driveList.append('drive n to be scanned') ## This code will scan any number of drives
    ##print drives
    os.chdir(driveList[n])
    ##print 'Drive being scanned:',drives
    for setFolder in os.listdir(os.getcwd()):
        if os.path.isdir(setFolder)==True and \
           len(setFolder)==3 and setFolder != 'sec':
            collSet.append(os.listdir(setFolder))
            if (('prft')+'0002.'+setFolder)in collSet[n]:
                pass
            elif (('PRFT')+'0002.'+setFolder)in collSet[n]:
                pass
            else:
                setList.append(int(setFolder))
            n = n + 1
            continue
    return setList

def binarySearch():
    n = 0
    driveList = []
    driveList.append('drive 1 to be scanned')
    driveList.append('drive 2 to be scanned')
    driveList.append('drive 3 to be scanned')
    driveList.append('drive n to be scanned') ## This code will scan any number of drives
    setFolder = []
    os.chdir(driveList[n]) 
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
    n = n + 1
    continue
binarySearch()
