
import glob
import csv
import os

os.chdir('C:\Users\U2970\Desktop\Rut and Ride Data2') ## Changes directory to this path

def data_parser():
    for file in glob.glob('*.TXT'): ## Looks for any file in directory that ends with .TXT
        for row in csv.DictReader(open(file,'rb')): ## Opens all files given by glob row by row
            try:
            except:
                beg = float(row['Beginning'])  ## Some beg data was in float some was in integer
            except ValueError:
                beg = int(row['Beginning'])  ## Beginning mile of each corridor
            corridor = str(row['Corridor'])  ## Corridor number
            try:
                end = float(row['Ending'])  ## End mile of each corridor
            except ValueError:
                end = int(row['Ending'])
            ll1Date = str(row['LL1_Date'])
            try:
                ll1Ride = int(row['LL1_Ride'])
            except ValueError:
                ll1Ride = str(row['LL1_Ride']) ## Some Lane 1 ride data was in string some in float
            try:
                ll1Rut = float(row['LL1_Rut']) ## Left side of Lane 1 rut data
                ll1Rut = str(row['LL1_Rut'])
            rl1Date = str(row['RL1_Date'])
            try:
                rl1Ride = int(row['RL1_Ride']) ## Right side of lane 1 ride data
            except ValueError:
                rl1Ride = str(row['RL1_Ride'])
            try:
                rl1Rut = float(row['RL1_Rut']) ## Right side of lane 1 rut data
            except ValueError:
                rl1Rut = str(row['RL1_Rut'])
            year = int(row['Year'])
            yield beg,corridor,end,ll1Date,ll1Ride,\
                  ll1Rut,rl1Ride,rl1Rut,year

os.chdir('C:\Users\U2970\Desktop')
outfile = csv.writer(open('project_outfile_christian_new.csv','wb')) ## Creates csv file for output
for row in data_parser():
    outfile.writerow(row) ## Writes data from data_parser to a csv file
print'creation is done of the .CSV'
    print row

