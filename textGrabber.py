import os
import re
import sys

'''This program acquires the text files from the sharedrive path shown below and yields them out.
this program is used by the baseline plotting programs for both Rut and IRI. Each function below
grabs a different text file'''

# changes directory to the sharedrive path
os.chdir('Y:\\\\PavementAnalysis\\\\Pavemgmt\\\\DATA_COLLECTION\\\\AUTOMATED_VANS\\\\02_COLLECTION_VEHICLES\\\\01_CALIBRATION\\\\2015\\\\H12_174_NORTH\\\\NORTH BASELINE\\\\BaseLineData')

def textGrab1(): # gets the first text file
    try:
        with open('BASELINE1.TXT', 'rU') as file: # opens the text file and assigns it to file
            yield file # yields the file to where the function is called
    except IOError:
        print'Error: Did you name the file correctly as BASELINE1.TXT?' # was the text file misnamed?
        sys.exit(0)
        
def textGrab2():
    try:
        with open('BASELINE2.TXT', 'rU') as file:
            yield file
    except IOError:
        print'Error: Did you name the file correctly as BASELINE2.TXT?'
        sys.exit(0)
        
def textGrab3():
    try:
        with open('BASELINE3.TXT', 'rU') as file:
            yield file
    except IOError:
        print'Error: Did you name the file correctly as BASELINE3.TXT?'
        sys.exit(0)

def textGrab4():
    try:
        with open('BASELINE5.TXT', 'rU') as file:
            yield file
    except IOError:
        print'Error: Did you name the file correctly as BASELINE4.TXT?'
        sys.exit(0)

def textGrab5():
    try:
        with open('BASELINE5.TXT', 'rU') as file:
            yield file
    except IOError:
        print'Error: Did you name the file correctly as BASELINE5.TXT?'
        sys.exit(0)
    
def textGrab6():
    try: 
        with open('BASELINE6.TXT', 'rU') as file:
            yield file
    except IOError:
        print'Error: Did you name the file correctly as BASELINE6.TXT?'
        sys.exit(0)
        
def textGrab7():
    try:
        with open('BASELINE7.TXT', 'rU') as file:
            yield file
    except IOError:
        print'Error: Did you name the file correctly as BASELINE7.TXT?'
        sys.exit(0)

def textGrab8():
    try: 
        with open('BASELINE8.TXT', 'rU') as file:
            yield file
    except IOError:
        print'Error: Did you name the file correctly as BASELINE8.TXT?'
        sys.exit(0)

def textGrab9():
    try:
        with open('BASELINE9.TXT', 'rU') as file:
            yield file
    except IOError:
        print'Error: Did you name the file correctly as BASELINE9.TXT?'
        sys.exit(0)

def textGrab10():
    try:
        with open('BASELINE10.TXT', 'rU') as file:
            yield file
    except IOError:
        print'Error: Did you name the file correctly as BASELINE10.TXT?'
        sys.exit(0)
