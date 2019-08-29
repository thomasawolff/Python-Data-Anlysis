import os
import re
import csv

os.chdir(os.getcwd())

fileName = 'Home_Visit_Encounter.txt'
value1 = '622699'
value2 = '2016-05-19'

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
        fullSet.append([filesList])

    for lines in position:
        if position[0] == fullSet[0][0][0][0]:
            dirCheck.append('All Good')
        else:
            dirCheck.append(['Do not Match',position[0],fullSet[0][0][0][0]])
    #print dirCheck
            
    dataDict = dict(zip(position,fullSet))
    for i in range(0,len(dataDict.keys())):
        if any(fileName in val for val in dataDict.values()[i][0][0]) == True:
            changeDir = str(dataDict.keys()[i])+'\\'+fileName
            changeDirList.append(changeDir)

    for row in changeDirList:
        with open(row) as f:
            files = csv.reader(f,delimiter=',')
            filesData = [[] for i in xrange(0)]
            while t < 2:
                columns = files.next()
                columnList.append(columns)
                cleanCol = map(lambda l: [x.split('\t') for x in l],columnList)
                t = t + 1
            for line in files:
                filesData.append(line)
            for e in range(0,len(filesData)):
                no_tabs = map(lambda x: x.split("\t"),filesData[e])
                newDict = dict(zip(cleanCol[0][0],no_tabs[0]))
                if value1 in newDict.values() and value2 in newDict.values():
                    headers.append(newDict.keys())
                    final.append(newDict.values())

    with open('NFPdata.csv','wb') as data:
        filename = csv.writer(data)
        #filename.writerow(headers)
        for lines in final:
            filename.writerow(lines)

dataParser()



