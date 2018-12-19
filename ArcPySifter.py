import os
import arcpy
import glob as g
from math import radians, cos, sin, asin, sqrt, atan2

m = 1

data1 = []

fields = ['START_LAT','START_LONG','END_LAT','END_LONG']
path = 'Y:\\\\PavementAnalysis\\\\Pavemgmt\\\\DATA_COLLECTION\\\\AUTOMATED_VANS\\\\07_GIS_LAYERS\\\\GIS_MAPPING_PROJECTS\\\\Geodatabase_10_12_16.gdb'

with arcpy.da.SearchCursor("northDataSorted",fields) as cursor:
    for row in cursor:
        data1.append(row)

for n in range(1,len(data1)):
    ##      START_LAT = n[0]
    ##      START LONG = n[1]
    ##      END_LAT = n[2]
    ##      END_LONG = n[3]
    diffLatS = radians(abs(float(data1[m][0]) - float(data1[n][0]))) # lat diff for start node
    diffLongS = radians(abs(float(data1[m][1]) - float(data1[n][1]))) # long diff for start node
    diffLatE = radians(abs(float(data1[m][2]) - float(data1[n][2]))) # lat diff for end node
    diffLongE = radians(abs(float(data1[m][3]) - float(data1[n][3]))) # long diff for end node
    xDistWGS = radians((float(data1[n][0])-float(data1[n][2])))
    yDistWGS = radians((float(data1[n][1])-float(data1[n][3])))

    xSd = sin(yDistWGS/2)**2 + cos(float(data1[n][0]))*cos(float(data1[n][2]))*sin((xDistWGS/2))**2
    ySd = 2*atan2(sqrt(xSd),sqrt(1 - xSd))
    dDist = 3958.756 * ySd # distance in miles between start and end nodes

    if diffLatS > 0.0 and diffLongS > 0.0:
        xS = sin(diffLatS/2)**2 + cos(float(data1[m][0]))*cos(float(data1[n][0]))*sin(diffLongS/2)**2
        yS = 2*atan2(sqrt(xS),sqrt(1 - xS))
        dStart = 3958.756 * yS # distance in miles between starting nodes of different rows

        xE = sin(diffLatE/2)**2 + cos(float(data1[m][2]))*cos(float(data1[n][2]))*sin(diffLongE/2)**2
        yE = 2*atan2(sqrt(xE),sqrt(1 - xE))
        dEnd = 3958.756 * yE # distance in miles between ending nodes of different rows

        print dStart
        m = m + 1

