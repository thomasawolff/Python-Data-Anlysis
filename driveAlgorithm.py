import os

'''This program figures out how the sharedrive is configured
on a networked computer. It begins by looking to see which letters
in the alphabet, or driveList is a active directory. It then iterates
through the dir_ list placing each string element in front of the
active drive letters testing to see which strings match the drive letters.
By iterating through the letters and drives,the drive letter combined
with the pathway to the correct folder should be found'''

driveList = ['A:','B:','C:','D:','E:','F:','G:',\
                 'H:','I:','J:','K:','L:','M:','N:',\
                 'O:','P:','Q:','R:','S:','T:','U:',\
                 'V:','W:','X:','Y:','Z:'] # list of possible drive letters

dir_ = ['PavementAnalysis','Pavemgmt','DATA_COLLECTION',\
        'AUTOMATED_VANS','02_COLLECTION_VEHICLES',\
        '01_CALIBRATION'] # list of strings that comprise the path to the
                          # correct folder on the sharedrive

def driveFind():
    for drives in driveList:
        n = 0 # iterator is initiated at 0
        letter = drives[n]+':/'     # letter = drives indexed to 
        if os.path.isdir(letter) == True:   # if the letter is an active drive
            for strings in dir_:    # iterate through the strings in dir_ list
                folders = letter+'\\'+strings   # create the possible directory
                if os.path.isdir(folders) == True:  # if the pathway is a directory
                    m = dir_.index(strings)     # m = the index level value of the string in dir_ list
                    while True:
                        m = m + 1   # increment m
                        folders = folders+'\\'+dir_[m]  # keep adding strings to the sharedrive path
                        if dir_[m] == dir_[-1]:     # until the last value is reached in the dir_ list
                            return folders      # returns the drive path and now it can be used to
                                                # change the directory of another program.
                        else:continue
                else:break

def driveFindNewAlg():
    for drives in driveList:
        n = 0
        letter = drives[n]+':/'
        if os.path.isdir(letter) == True:
            while True:
                folders = letter+'\\'+dir_[n]
                n = n + 1
                if os.path.isdir(folders) == True:
                    m = dir_.index(dir_[n])
                    while True:
                        m = m + 1
                        folders = folders+'\\'+dir_[m]
                        if dir_[m] == dir_[-1]:
                            #os.chdir(folders)
                            return folders
                        else:continue
                if n == len(dir_):break    








##def drivePrint():
##    driveList = ['A:','B:','C:','D:','E:','F:','G:',\
##                 'H:','I:','J:','K:','L:','M:','N:',\
##                 'O:','P:','Q:','R:','S:','T:','U:',\
##                 'V:','W:','X:','Y:','Z:']
##    dir_ = ['PavementAnalysis','Pavemgmt','DATA_COLLECTION',\
##            'AUTOMATED_VANS','02_COLLECTION_VEHICLES','01_CALIBRATION']
##    for drives in driveList:
##        n = 0
##        letter = drives[n]+':/'
##        if os.path.isdir(letter) == True:
##            for strings in dir_:
##                folders = letter+'\\\\'+strings
##                if os.path.isdir(folders) == True:
##                    print folders
##                    m = dir_.index(strings)
##                    while True:
##                        m = m + 1
##                        folders = folders+'\\\\'+dir_[m]
##                        print folders
##                        if dir_[m] == dir_[-1]:
##                            print folders
##                            break
##                        else:continue
##                else:break
##drivePrint()

##        while os.path.isdir(folders) == True:
##            m = 0
##            print folders
##            while True:
##                m = m + 1
##                folders = folders+'\\\\'+dir_[m]
##                print folders
##                if dir_[m] == dir_[-1]:
##                    os.chdir(folders)
##                    print''
##                    print'Directory is:',folders
##                    print''
##                    p.pprint(os.listdir(folders))
##                    break
##                else:
##                    continue

##        else:
##            if n == len(driveList):
##                break
##            n = n + 1
##            continue




##m = 0
##print folders
##while True:
##    m = m + 1
##    folders = folders+'\\\\'+dir_[m]
##    print folders
##    if dir_[m] == dir_[-1]:
##        os.chdir(folders)
##        print''
##        print'Directory is:',folders
##        print''
##        p.pprint(os.listdir(folders))
##        break
##    else:
##        continue


##def drivePrint():
##    driveList = ['A:','B:','C:','D:','E:','F:','G:',\
##                 'H:','I:','J:','K:','L:','M:','N:',\
##                 'O:','P:','Q:','R:','S:','T:','U:',\
##                 'V:','W:','X:','Y:','Z:']
##    dir_ = '\\\\Pavemgmt\\\\DATA_COLLECTION\\\\AUTOMATED_VANS\\\\02_COLLECTION_VEHICLES\\\\01_CALIBRATION'
##    while True:
##        for drives in driveList:
##            n = 0
##            dir_year = drives[n]+':'+dir_
##            if os.path.isdir(dir_year) == True:
##                return dir_year
##            else:
##                n = n + 1
##                if n == len(driveList):
##                    break
##        for drives in driveList:
##            n = 0
##            dir_year = drives[n]+':'+'\\\\PavementAnalysis'+dir_
##            if os.path.isdir(dir_year) == True:
##                return dir_year
##            else:
##                n = n + 1
##                if n == len(driveList):
##                    break
