import os
import csv
import re
import matplotlib.pyplot as plt
from matplotlib import pylab
from matplotlib import style

#style.use('dark_background')
#style.use('bmh')

figure1 = plt.figure()

def graphWriterIRI():
    # Set up the plots
    plt.subplot(2, 1, 1)
    plt.grid(True)
    plt.ylabel('IRI value', fontsize=12)
    #pylab.ylim([0,150])
    plt.title('Right IRI data per mile for verification runs')
    plt.tick_params(axis='both', which='major', labelsize=8)
    plt.hold(True)
    plt.subplot(2, 1, 2)
    plt.grid(True)
    plt.ylabel('IRI value', fontsize=12)
    #pylab.ylim([0,150])
    plt.title('Left IRI data per mile for verification runs:')
    plt.tick_params(axis='both', which='major', labelsize=8)
    plt.hold(True)
    # Iterate over the files in the current directory
    for filename in os.listdir(os.getcwd()):
        # Initialize a new set of lists for each file
        startList = []
        endList = []
        iriRList = []
        iriLList = []
        # Load the file
        with open(filename, 'rU') as file:
            for row in csv.DictReader(file):
                try:
                    startList.append(float(row['Start-Mi']))
                    endList.append(float(row['  End-Mi']))
                except:
                    startList.append(float(row['Start-MP']))
                    endList.append(float(row['  End-MP']))
                try:
                    iriRList.append(float(row[' IRI R e']))
                    iriLList.append(float(row['IRI LWP ']))
                except:
                    iriRList.append(float(row[' IRI RWP']))
                    iriLList.append(float(row['IRI LWP ']))
            
        # Add new data to the plots
        try:
            plt.subplot(2, 1, 1)
            plt.plot(startList, iriRList)
            plt.subplot(2, 1, 2)
            plt.plot(startList, iriLList)
        except ValueError:pass
        
    plt.show()
    plt.close('all')


def graphWriterRut():
    # Set up the plots
    plt.subplot(2, 1, 1)
    plt.grid(True)
    plt.ylabel('Rut value', fontsize=12)
    pylab.ylim([0,.4])
    plt.title('Right Rut data per mile for verification runs:')
    plt.tick_params(axis='both', which='major', labelsize=8)
    plt.hold(True)
    plt.subplot(2, 1, 2)
    plt.grid(True)
    plt.ylabel('Rut value', fontsize=12)
    pylab.ylim([0,.4])
    plt.title('Left Rut data per mile for verification runs:')
    plt.tick_params(axis='both', which='major', labelsize=8)
    plt.hold(True)
    # Iterate over the files in the current directory
    for filename in os.listdir(os.getcwd()):
        # Initialize a new set of lists for each file
        startList = []
        endList = []
        RutRList = []
        RutLList = []
        # Load the file
        with open(filename, 'rU') as file:
            for row in csv.DictReader(file):
                try:
                    startList.append(float(row['Start-Mi']))
                except:
                    startList.append(float(row['Start-MP']))
                try:
                    endList.append(float(row['  End-Mi']))
                except:
                    endList.append(float(row['  End-MP']))
                try:    
                    RutRList.append(float(row[' RUT R e']))
                except:pass
                try:
                    RutRList.append(float(row[' RUT RWP']))
                except:pass
                try:
                    RutLList.append(float(row[' RUT L e']))
                except:pass
                try:
                    RutLList.append(float(row[' RUT LWP']))
                except:pass
        #print startList,RutRList,RutLList
        #print len(RutRList),len(RutLList)
        # Add new data to the plots
        try:
            plt.subplot(2, 1, 1)
            plt.plot(startList, RutRList)
            plt.subplot(2, 1, 2)
            plt.plot(startList, RutLList)
        except ValueError:pass
    plt.show()
    plt.close('all')

