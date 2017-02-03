
import csv,sqlite3,os

'''This code is used to create a SQLite database within the Python environment from a csv file'''

os.chdir('C:\\\\Users\\\\U2970\\\\Desktop')

dataBase = sqlite3.connect('csvTest.sqlite') # creates the database connection
cur = dataBase.cursor()  # sets the cursor 
cur.execute("CREATE TABLE if not exists projects6 (ROW_ID integer primary key,\
            CONT integer,\
            CORR varchar(100),\
            PROJ_NUM varchar(100),\
            ROUTE varchar(100),\
            BEGMi float,\
            ENDMi float,\
            CONTRACTid integer,\
            CONTROL_NUMBER integer,\
            PROJ_NAME varchar(1000),\
            QMI_NAME varchar(100),\
            ITEM_NUMBER integer,\
            NUMBER_LIFTS integer,\
            DESIGN_MIX_TYPE varchar(100),\
            DESIGN_ADDITIVE_PERCENT float,\
            DESIGN_VFA float,\
            DESIGN_ADDITIVE varchar(100),\
            DESIGN_ASPHALT_PERCENT float,\
            DESIGN_DENSITY float,\
            DESIGN_HAMBURG float,\
            DESIGN_RICE float)") # creates table and sets columns

with open('PROJECT_DATA_02_03_17.csv','rb') as files: # opens and reads the csv file
    dataFile = csv.DictReader(files)
    
    ''' The code below grabs columns by their names and takes in data from each row
        then assigns all the data to the variable to_db'''
    
    to_db = [(i['OBJECTID__'],i['CONT_ID'],i['CORRIDOR_RB'],i['PROJECT_NUM'],i['ROUTE_NBR'],\
              i['PROJECT_START'],i['PROJECT_END'],i['CONTRACT_ID'],\
              i['CONTROL_NUMBER'],i['PROJECT'],i['QMI_NAME'],i['QMI_ITEMNUMBER'],\
              i['QDP_NUMBERLIFTS'],i['DESIGN_MIX_TYPE'],i['DESIGN_%_ADDITIVE'],\
              i['DESIGN_VFA'],i['DESIGN ADDITIVE'],i['DESIGN_%_ASPHALT_CONTENT'],\
              i['DESIGN_DENSITY'],i['DESIGN_HAMBURG_VOIDS'],i['DESIGN_RICE']) for i in dataFile]

    '''The code below inserts the data from to_db and assigns each column of data
       to the column names created above. The question marks are place holders for
       for the data from to_db'''
    
cur.executemany("INSERT INTO projects6 (ROW_ID,CONT,CORR,PROJ_NUM,ROUTE,BEGMi,ENDMi,CONTRACTid,\
                CONTROL_NUMBER,PROJ_NAME,QMI_NAME,ITEM_NUMBER,NUMBER_LIFTS,DESIGN_MIX_TYPE,\
                DESIGN_ADDITIVE_PERCENT,DESIGN_VFA,DESIGN_ADDITIVE,DESIGN_ASPHALT_PERCENT,\
                DESIGN_DENSITY,DESIGN_HAMBURG,DESIGN_RICE)\
                values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", to_db)

''' For rows in the variables below selected from projects6 table, print the variables'''

for rowID,cont,corr,project_num,route,begmi,endmi,contractID,\
    controlNumber,project,qmiName,itemNumber,numberLifts,\
    designMixType,designAdditivePer,designVFA,designAdditive,designAsphaltPer,\
    designDensity,designHamburgVoids,designRice in cur.execute("select * from projects6"):
    
    print   rowID,cont,corr,project,route,begmi,endmi,contractID,controlNumber,\
            project,qmiName,itemNumber,numberLifts,designMixType,designAdditivePer,\
            designVFA,designAdditive,designAsphaltPer,designDensity,\
            designHamburgVoids,designRice

dataBase.close()


