import os
import re
import csv
import sys
import arcpy as ap
import glob as g
import pprint as p
from itertools import groupby
from math import radians, cos, sin, asin, sqrt, atan2

os.chdir('C:\Users\U2970\Desktop\Desktop Excel Files')

'''This code is intended to input a csv file and utilize the latitude
and longitude. It calculates the distance between the latitude and
longitude in miles and appends the resulting data along with the data from
the csv into a Python list. That list, which is a list of lists, is sorted
using the first two columns, or the distance between the first record and
all the other records in the csv file. The sorted file includes the streets
in order of distance from the first record in the csv.'''

def dataOutGlob():
    for file in g.glob('*NORTH_OUTPUT_DATA.csv'): # This was run on Missoula Montana data
        for line in open(file):
            yield line

def headerBody():
    m = 1
    b = 0
    data1 = []
    dist = [] # initiating empty lists
    for line in dataOutGlob():
        data1.append(line.split(','))
        
    for n in range(1,len(data1)):
        
        # Calculating the distance between the starting lat,long,
        # and ending lat and long of streets in csv file.
        # m = first row in csv
        # n = row n in csv
        
        diffLatS = radians(abs(float(data1[m][20]) - float(data1[n][20]))) # lat diff for start node
        diffLongS = radians(abs(float(data1[m][21]) - float(data1[n][21]))) # long diff for start node
        diffLatE = radians(abs(float(data1[m][22]) - float(data1[n][22]))) # lat diff for end node
        diffLongE = radians(abs(float(data1[m][23]) - float(data1[n][23]))) # long diff for end node

        diffLongX = radians(abs(float(data1[n][20]) - float(data1[n][22]))) # lat diff for start node
        diffLatY = radians(abs(float(data1[n][21]) - float(data1[n][23]))) # long diff for start node
        
        xDistWGS = radians((float(data1[n][20])-float(data1[n][22])))
        yDistWGS = radians((float(data1[n][21])-float(data1[n][23])))
        try: 
            if diffLatS > 0.0 and diffLongS > 0.0:
                xSd = sin(yDistWGS/2)**2 + cos(float(data1[n][20])) * cos(float(data1[n][22]))\
                        * sin((xDistWGS /2))**2
                ySd = 2 * atan2(sqrt(xSd),sqrt(1 - xSd))
                dDist = 3958.756 * ySd # distance in miles between start and end nodes
                
                xS = sin(diffLatS/2)**2 + cos(float(data1[m][20])) * cos(float(data1[n][20]))\
                        * sin(diffLongS /2)**2
                yS = 2 * atan2(sqrt(xS),sqrt(1 - xS))
                dStart = 3958.756 * yS # distance in miles between starting nodes of different rows

                xE = sin(diffLatE/2)**2 + cos(float(data1[m][22])) * cos(float(data1[n][22]))\
                        * sin(diffLongE /2)**2
                yE = 2 * atan2(sqrt(xE),sqrt(1 - xE))
                dEnd = 3958.756 * yE # distance in miles between ending nodes of different rows
                                                                        
                dist.append([dStart,dEnd,data1[n][0],data1[n][1],int(data1[n][2]),\
                             data1[n][3],data1[n][4],data1[n][5],\
                             data1[n][6],data1[n][7],data1[n][8],\
                             data1[n][9],data1[n][10],data1[n][11],\
                             float(data1[n][12]),float(data1[n][13]),\
                             float(data1[n][14]),float(data1[n][15]),
                             data1[n][16],data1[n][17],data1[n][18],\
                             data1[n][19],float(data1[n][20]),\
                             float(data1[n][21]),float(data1[n][22]),\
                             float(data1[n][23])]) # csv data appended to list dist
                try:
                    xDiffTis = (float(data1[n][27])-float(data1[n][29]))**2 # state plane coordinates longitude
                    yDiffTis = (float(data1[n][28])-float(data1[n][30]))**2 # state plain coordinates latitude
                    print round((math.sqrt(xDiffTis+yDiffTis)*3.280)/5280.0,4),round(dDist,4),\
                          abs(float(data1[n][14])-float(data1[n][15]))
                except ValueError: pass
        except ValueError: print round(xSd,3),'   ',round(ySd,3)
        
    dist.sort(key = lambda row: row[0:2]) # sorts a list of lists by two factors
    #print str(dist[0:])[1:-1].replace("'","") # strips away characters

headerBody()
