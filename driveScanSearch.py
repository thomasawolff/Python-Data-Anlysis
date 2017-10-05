import os
import sys
import csv
import time

'''This code scans through any number of system
drives internal and external and searches for
prft and PRFT files (or any other kind of file)'''

##driveSet = ['A:','B:','D:','E:','F:','G:',\
##            'H:','I:','J:','K:','L:','M:',\
##            'N:','O:','P:','Q:','R:','S:',\
##            'T:','U:','V:','W:','X:','Y:','Z:']


driveSet = ['A:','B:','D:','F:','I:','J:','K:','L:','M:',\
            'N:','O:','P:','S:','U:','V:']


def driveFind():
    for drives in driveSet:
        if os.path.isdir(drives)==True: # letters from driveSet
            yield drives                # that are drives are yielded
        #else: print 'No drives'
driveFind()
            
def setFinder():
    for driveList in driveFind():
        try:os.chdir(driveList) # change directory to driveList drives
        except WindowsError:pass # pass by the drive if error
        print 'Drive being scanned:',driveList
        for setFolder in os.listdir(os.getcwd()): # for folder in list of folders
            if os.path.isdir(setFolder)==True and \
               len(setFolder)==3 and \
               setFolder.endswith('.sec')==False: # if it ends with '.sec'
                try: type(int(setFolder[-3:])) # if the folder name ends with 3 numbers
                except ValueError:continue # code above will raise error if false: continue
                yield driveList+'\\'+setFolder # yield the drive and setFolder 
        if driveList == driveList[-1]: # when it gets to end of driveList stop
            sys.exit(0) # exit from the code

def missingFileSearchPRFT(): # searches for prft files
    for line in setFinder():
        data = os.listdir(line)
        if('prft0002.'+line[-3:] in data) or ('PRFT0002.'+line[-3:] in data):
            print'Fine here:',line
        else:
            print 'PRFT Data is missing here:',line # tells you where data is missing
#missingFileSearchPRFT()

def missingFileSearchBoxes(): # searches for area crack and boxes files
    setList = []
    for line in setFinder():
        os.chdir(line)
        folder = os.listdir(line)
        for minFolder in folder:
            if os.path.isdir(minFolder)==True:
                for data in os.listdir(minFolder):
                    if data == str(data[0:12])+'_area_boxes_cr.txt' or \
                       data == str(data[0:12])+'_area_pixels_cr.txt' or \
                       data == str(data[0:12])+'_crack_pixels_cr.txt' or \
                       data == str(data[0:12])+'_boxes_cr.txt' or \
                       data == str(data[0:12])+'.jpg' or \
                       data == str(data[0:12])+'.3dc' or \
                       data == str(data[0:12])+'.jpg.thmb' or \
                       data == str(data[0:12])+'_intensity.jpg' or \
                       data == str(data[0:12])+'_intensity.jpg.thmb' or \
                       data == str(data[0:12])+'_depth.jpg' or \
                       data == str(data[0:12])+'_depth.jpg.thmb' or \
                       data == 'Errors.txt' or \
                       data == 'Thumbs.db': pass
                    else: print line,minFolder,data


def dataYield(): # writes output to a csv file
    os.chdir('C:\\\\Users\\\\U2970\\\\Desktop')
    with open('missingDataPrft.csv','w') as fp:
        for line in missingFileSearchPRFT():
            print line
            filename = csv.writer(fp)
            filename.writerow(line)
            
start_time = time.time()
missingFileSearchBoxes()
print("--- %s seconds ---" % (time.time() - start_time))

