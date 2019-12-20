
import csv
import os

os.chdir('\\\\hhs-hlnshare\\\\shared\\\\phs\\\\MTmechv Data\\\\Reports\\\\Report Codesets')

def fileFinder():
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
          yield(dict(zip([os.getcwd()+root],[name])))
        for name in dirs:
          yield(dict(zip([os.getcwd()+root],[name])))

def rowFinder():
    files = []
    for lines in fileFinder():
        files.append(lines)

    for i in range(0,len(files)):
        os.chdir(files[i].keys()[0])
        try:
            with open(files[i].values()[0],'r') as inData:
                n = 0
                lines = csv.reader(inData)
                for row in lines:
                    if 'FORM_NAME' in row:
                        print (files[i].keys()[0]+'\\'\
                              +files[i].values()[0]+',','Line:',str(n)+':')
                        print (row)
                        print('\n')
                    n = n + 1
        except IOError: pass

rowFinder()

input("Press enter to exit ;)")
