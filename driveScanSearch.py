import os
import sys

driveSet = ['A:','B:','C:','D:','E:','F:','G:','H:','I:','J:','K:','L:','M:','N:','O:','P:','Q:','R:','S:','T:','U:','V:','W:','X:','Y:','Z:']

def driveFind():
    dirs = []
    for drives in driveSet:
        if os.path.isdir(drives)==True:
            dirs.append(drives)
        if drives == driveSet[-1]:
            return dirs
        else:continue
            
def setFinder():
    for driveList in driveFind():
        try:os.chdir(driveList)
        except WindowsError:pass
        print 'Drive being scanned:',driveList
        for setFolder in os.listdir(os.getcwd()):
            if os.path.isdir(setFolder)==True and len(setFolder)==3 and setFolder.endswith('.sec')==False:
                try: type(int(setFolder[-3:]))
                except ValueError:continue
                yield driveList+'\\'+setFolder
        if driveList == driveList[-1]:
            sys.exit(0)

def missingFileSearch():
    dataList = []
    for line in setFinder():
        data = os.listdir(line)
        if('prft0002.'+line[-3:] in data):
            pass
        elif('PRFT0002.'+line[-3:] in data):
            pass
        else:
            print'Data is missing here:',line
            dataList.append(int(line[-3:])) 
    return dataList
missingFileSearch()
