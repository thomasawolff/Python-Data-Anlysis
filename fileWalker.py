import os
import csv
import timeit


def fileOut():
    n = 0
    m = 0
    d = 0
    os.chdir('Y:\\\\PavementAnalysis\\\\Pavemgmt') ## This is where I tell the code where to go
    ## traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk("."):
        path = root.split('/')
        for file in files:
            if file.endswith('.XLS' or '.xls'):
                n = n + 1 # Counts Excel files
                yield file,root
            if file.endswith('.DOC' or '.doc'):
                m = m + 1 # Counts Word files
                yield file,root
            if file.endswith('.PPT' or '.ppt'):
                d = d + 1 # Counts Powerpoint files
                yield file,root
    yield 'Excel Files:',n,'Word Files:',m,'Powerpoint Files:',d ## Totals for each type of file

def fileYield(): ## Creates a .csv file of files to be converted
    os.chdir('C:\\\\Users\\\\U2970\\\\Desktop')
    with open('Converts.csv','w') as fp:
        for line in fileOut():
            filename = csv.writer(fp)
            filename.writerow(line)
            
fileYield()
