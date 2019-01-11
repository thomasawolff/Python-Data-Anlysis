
import arcpy
from arcpy import env


fields = ['CORRIDOR_C','ROAD_VAN','FROM_DESCR','TO_DESCR','FRFPOST','TRFPOST','BEGIN_MI','END_MI','DIR','LANE']
path = 'Y:\\\\PavementAnalysis\\\\Pavemgmt\\\\DATA_COLLECTION\\\\AUTOMATED_VANS\\\\07_GIS_LAYERS\\\\GIS_MAPPING_PROJECTS\\\\COLLECTION VAN DATA\\\\2019 North Data'
env.workspace = path

d = []
i = []

def dataMiner():
    
    with arcpy.da.SearchCursor("North_2018_Last_Year_Data.dbf",fields) as cursor:
        for row in cursor:
            corridor = row[0]
            road_van = row[1]
            from_descr = row[2]
            to_descr = row[3]
            frfpost = float(row[4])
            trfpost = float(row[5])
            begin = float(row[6])
            end_ = float(row[7])
            dir_ = row[8]
            lane = int(row[9])
            
            if dir_ == 'I' and lane == 1 and 'Concret' not in from_descr:
                i.append([corridor,road_van,from_descr,to_descr,\
                         frfpost,trfpost,begin,end_,dir_,lane])

            elif dir_ == 'D' and lane == 1 and 'Concret' not in from_descr:
                d.append([corridor,road_van,from_descr,to_descr,\
                         frfpost,trfpost,begin,end_,dir_,lane])

    for n in range(0,len(d)):
        for m in range(0,len(i)):
            if (d[n][0] == i[m][0]) and (d[n][1] in i[m][1])\
               and (d[n][3] in i[m][2]) and (i[m][3] in d[n][2])\
               and ((d[n][5] != i[m][4]) or (i[m][4] != d[n][5])):
                
                print d[n][0],',',d[n][1],',',d[n][2],',',d[n][3],',',d[n][8],',',\
                      d[n][4],',',d[n][5],',',i[m][4],',',i[m][5]

    del cursor

dataMiner()

