import os
import csv
import time
import arcpy
import numpy
from arcpy import env
from numpy import array
timestr = time.strftime('%Y%m%d%H%M')

path = r'Y:\\\\PavementAnalysis\\\\Pavemgmt\\\\DATA_COLLECTION\\\\AUTOMATED_VANS\\\\07_GIS_LAYERS\\\\GIS_MAPPING_PROJECTS\\\\Map_DBF'
gdb = 'Y:\\\\PavementAnalysis\\\\Pavemgmt\\\\DATA_COLLECTION\\\\AUTOMATED_VANS\\\\07_GIS_LAYERS\\\\GIS_MAPPING_PROJECTS\\\\SEC_FILE_GDB.gdb'

def headerBody():
    output = []
    os.chdir(path)
    outfile = csv.writer(open('program_NORTH_data.csv','wb'))
    with open('NORTH_V2017.SEC') as line:
        for data in line:
            col = data.split('!')
            corrRB = col[4]+col[32]
            begMi = float(col[12])
            endMi = float(col[13])
            dir_ = col[16]
            lane = int(col[31])
            set_ = int(col[41])
            if set_ > 0:
                output.append([corrRB,begMi,endMi,dir_,lane,set_])

    columns = 'corrRB','begMi','endMi','dir_','lane','set_'
    outfile.writerow(columns)
    for line in output:
        print line
        outfile.writerows([line])
    
#headerBody()


def shapeBuilder():
    n = 0
    d = 0
    env.workspace = path
    inTable = 'program_NORTH_data.csv'
    outLocation = path+'\\\\DBF_Files'
    while True:
        try:
            outTable = 'secfileDBF'+str(n)
            arcpy.TableToTable_conversion(inTable, outLocation, outTable)
            break
        except:
            if d == 25:
                print'Too many .dbf files delete some or error'
                sys.exit(0)
            else:
                n = n + 1
                d = d + 1
                outTable = 'secfileDBF '+str(n)
                continue

    rt = 'g:\\\\LAYERS\\\\ROUTES\\\\MEASURED_ROUTES\\\\Corridor Routes - Miles.lyr'
    rid = 'CORRIDOR'
    tbl = outTable+'.dbf'
    props = 'corrRB LINE begMi endMi'
    lyr = 'secfileEvent'+timestr
    outpath = path+'\\\\DBF_Files'
    template = lyr
    geometry_type = 'POLYLINE'
    offset_field = 'lane'
    offset_direction = 'LEFT'
    os.chdir(outpath)
    arcpy.MakeRouteEventLayer_lr (rt,rid,tbl,props,lyr,'#','ERROR_FIELD')
    arcpy.TableToGeodatabase_conversion(tbl,env.workspace+'\\\\Geodatabases')
    print 'Geodatabase created'
    arcpy.FeatureClassToShapefile_conversion(lyr,env.workspace+'\\\\Shapefiles')
    print 'Shapefile created'

#shapeBuilder()


def arcStarter():
    
    os.chdir('C:\\\\Program Files (x86)\\\\ArcGIS\\\\Desktop10.4\\\\bin')
    os.system('start ArcMap.exe')

#arcStarter()


