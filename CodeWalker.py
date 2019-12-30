''' This code was intended to search through text files of SQL code searching for lines which had the string 'FORM_NAME'
The code will begin at the folder Report Codesets and search every file and directory recursively using the os.walk modele'''

import csv
import os

# Changing the directory to Report Codesets
os.chdir('\\\\hhs-hlnshare\\\\shared\\\\phs\\\\MTmechv Data\\\\Reports\\\\Report Codesets')

def fileFinder():
    # Recursive directory search using os.walk()
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            # Outputting a dictionary with the directory path as the key and filename as value
          yield(dict(zip([os.getcwd()+root],[name])))
        for name in dirs:
          yield(dict(zip([os.getcwd()+root],[name])))

def rowFinder():
    files = []
    # Appending the output from FileFider into the list files
    for lines in fileFinder():
        files.append(lines)

    for i in range(0,len(files)):
        # For each file, change the directory to the path of each file
        # Note that I am accessing the dictonary key using an iterator
        # within the list files and keys() for the dictionary key.
        os.chdir(files[i].keys()[0])
        try:
            # Open each csv file and assign it to the variable inData
            with open(files[i].values()[0],'r') as inData:
                n = 0
                # Read each csv file
                lines = csv.reader(inData)
                for row in lines:
                    # Iterate through each line of code and search for the string 'FORM_NAME'
                    if 'FORM_NAME' in row:
                        # If string is in line, print the key, value, and the line number of code n
                        print (files[i].keys()[0]+'\\'\
                              +files[i].values()[0]+',','Line:',str(n)+':')
                        print (row)
                        print('\n')
                    n = n + 1
                    # Notice n = 0 for each file. This resets the iterator n = 0 for each file. 
                    # This is how I get the line of code for each file.
        except IOError: pass

rowFinder()

input("Press enter to exit ;)")
