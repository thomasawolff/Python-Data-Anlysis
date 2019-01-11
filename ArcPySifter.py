import arcpy
import csv
from math import radians, cos, sin, asin, sqrt, atan2

m = 1

data1 = []
output = [] 

outfile = csv.writer(open('program_NORTH_data.csv','wb'))

fields = ['START_LAT','START_LON','END_LAT','END_LON',\
          'CORRIDOR_C','ROAD_VAN','FROM_DESCR','TO_DESCR',\
          'BEGIN_MI','END_MI','SECFILE_NA']

path = r'Y:\\\\PavementAnalysis\\\\Pavemgmt\\\\DATA_COLLECTION\\\\AUTOMATED_VANS\\\\07_GIS_LAYERS\\\\GIS_MAPPING_PROJECTS\\\\COLLECTION VAN DATA\\\\2019 North Data'

arcpy.env.workspace = path

with arcpy.da.SearchCursor('North_2018_Last_Year_Data.dbf',fields) as cursor:
    for row in cursor:
        data1.append([row])
del cursor


for n in range(1,len(data1)):
##      START_LAT = n[0]
##      START LONG = n[1]
##      END_LAT = n[2]
##      END_LONG = n[3]
    diffLatS = radians(abs(float(data1[m][0][0]) - float(data1[n][0][0]))) # lat diff for start node
    diffLongS = radians(abs(float(data1[m][0][1]) - float(data1[n][0][1]))) # long diff for start node
    diffLatE = radians(abs(float(data1[m][0][2]) - float(data1[n][0][2]))) # lat diff for end node
    diffLongE = radians(abs(float(data1[m][0][3]) - float(data1[n][0][3]))) # long diff for end node
    xDistWGS = radians((float(data1[n][0][0]) - float(data1[n][0][2])))
    yDistWGS = radians((float(data1[n][0][1]) - float(data1[n][0][3])))

    try:
        xSd = sin(yDistWGS/2)**2 + cos(float(data1[n][0][0]))*cos(float(data1[n][0][2]))*sin((xDistWGS/2))**2
        ySd = 2*atan2(sqrt(xSd),sqrt(1 - xSd))
        dDist = 3958.756 * ySd # distance in miles between start and end nodes

        if diffLatS > 0.0 and diffLongS > 0.0:
            xS = sin(diffLatS/2)**2 + cos(float(data1[m][0][0]))*cos(float(data1[n][0][0]))*sin(diffLongS/2)**2
            yS = 2*atan2(sqrt(xS),sqrt(1 - xS))
            dStart = 3958.756 * yS # distance in miles between starting nodes of different rows

            xE = sin(diffLatE/2)**2 + cos(float(data1[m][0][2]))*cos(float(data1[n][0][2]))*sin(diffLongE/2)**2
            yE = 2*atan2(sqrt(xE),sqrt(1 - xE))
            dEnd = 3958.756 * yE # distance in miles between ending nodes of different rows


            output.append([round(dStart,3),float(data1[n][0][0]),float(data1[n][0][1]),\
                           data1[n][0][4],data1[n][0][5],data1[n][0][6],\
                           data1[n][0][7],float(data1[n][0][8]),\
                           float(data1[n][0][9]),data1[n][0][10]])
    except ValueError: pass

columns = ['DISTANCE','START_LAT','START_LONG',\
           'CORRIDOR_C','ROAD_VAN',\
           'FROM_DESCR','TO_DESCR',\
           'BEG_MI','END_MI','SECFILE']

outfile.writerow(columns)
for line in output:
    outfile.writerows([line])

        
