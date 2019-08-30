import os
import re
import csv


directory = '\\\\hhs-hlnshare\\shared\\phs\\MTmechv Data\\NFP Exports'
os.chdir(directory)
print os.getcwd()

fileName = 'Home_Visit_Encounter.txt'

column1 = 'CL_EN_GEN_ID'
value1 = '622699'

column2 = 'SurveyDate'
#value2 = '2016-05-19'

def dataParser():
    t = 1
    files = []
    fullSet = []
    position = []
    final = []
    columnList = []
    changeDirList = []
    dirCheck = []
    headers = []
    
    for root, dirs, files in os.walk("."):
        path = root.split('/')
        folders = os.getcwd()+'\\'+root[2:]
        data = os.listdir(folders)
        filesList = [[] for i in xrange(0)]
        filesList.append([folders,data])
        position.append(folders)
        fullSet.append(filesList)

    for lines in position:
        if position[0] == fullSet[0][0][0]:
            dirCheck.append('All Good')
        else:
            dirCheck.append(['Do not Match',position[0],fullSet[0][0][0]])
    #print dirCheck
            
    dataDict = dict(zip(position,fullSet))
    for i in range(0,len(dataDict.keys())):
        if any(fileName in val for val in dataDict.values()[i][0]) == True:
            changeDir = str(dataDict.keys()[i])+'\\'+fileName
            changeDirList.append(changeDir)

    for row in changeDirList:
        with open(row) as f:
            files = csv.reader(f,delimiter=',')
            columns = files.next()
            columnList.append(columns)
            cleanCol = map(lambda l: [x.split('\t') for x in l],columnList)
            filesData = [[] for i in xrange(0)]
            for line in files:
                filesData.append(line)
            for e in range(0,len(filesData)):
                no_tabs = map(lambda x: x.split('\t'),filesData[e])
                newDict = dict(zip(cleanCol[0][0],no_tabs[0]))
                headers.append(newDict.keys())
                try:
                    if newDict[column1] == value1 and newDict[column2] == value2:
                        final.append(newDict.values())
                except NameError:
                    if newDict[column1] == value1:
                        final.append(newDict.values())

    with open('NFPdata.csv','wb') as data:
        filename = csv.writer(data)
        filename.writerow(headers[-1])
        for lines in final:
            filename.writerow(lines)

dataParser()



