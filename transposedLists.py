"""This code is designed to place data from .TXT files and place each file
into a seperate automatically-generated data structure. Each data structure is then
transposed and the average of the list of lists is calulated"""

def listNew():
    listRiri = []
    listLiri = []
    listRrut = []
    listLrut = []
    avgIRIleft = []
    avgIRIright = []
    avgRUTleft = []
    avgRUTright = []
    startList = []
    fileList = []
    baseFiles = []
    for data in os.listdir(os.getcwd()):
        fileList.append(data)
        if data.endswith('.TXT') and 'baseline' in data: ## looks for files
            with open(data,'rU') as file:
                R_iri = [[] for i in xrange(0)]  ## Automatically generates lists for each text file
                L_iri = [[] for i in xrange(0)]
                R_rut = [[] for i in xrange(0)]
                L_rut = [[] for i in xrange(0)]
                for row in csv.DictReader(file):
                    R_iri.append(float(row[' IRI RWP']))  ## Each generated list is appended to
                    L_iri.append(float(row['IRI LWP ']))  ## from each file
                    R_rut.append(float(row[' RUT RWP']))
                    L_rut.append(float(row[' RUT LWP']))
            listRiri.append(R_iri) ## creates a list of generated lists
            listLiri.append(L_iri)
            listRrut.append(R_rut)
            listLrut.append(L_rut) 
    transRiri = zip(*listRiri) ## zip command transposes each list of lists
    transLiri = zip(*listLiri)
    transRrut = zip(*listRrut) 
    transLrut = zip(*listLrut)  
    for a in range(0,len(transRiri)):
        rAvgIRI = np.average(transRiri[a])
        avgIRIright.append(round(float(rAvgIRI),4)) ## takes the average of the transposed list of lists
    for b in range(0,len(transLiri)):
        lAvgIRI = np.average(transLiri[b])
        avgIRIleft.append(round(float(lAvgIRI),4))
    for c in range(0,len(transRrut)):
        rAvgRUT = np.average(transRrut[c])
        avgRUTright.append(round(float(rAvgRUT),4))
    for d in range(0,len(transLrut)):
        lAvgRUT = np.average(transLrut[d])
        avgRUTleft.append(round(float(lAvgRUT),4))
        
    for files in fileList:
        if 'baseline' in files:
            baseFiles.append(files)
    with open(baseFiles[0],'rU') as file:
        for row in csv.DictReader(file):
            startList.append(float(row['Start-Mi']))

    return startList,avgIRIright,avgIRIleft,avgRUTright,avgRUTleft
