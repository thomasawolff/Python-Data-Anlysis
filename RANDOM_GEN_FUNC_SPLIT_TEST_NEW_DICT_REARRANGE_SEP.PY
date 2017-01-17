
import os
import csv
import math
import sys
import random as r

def readerIn(): # changes the directory to the desktop to begin program
    os.chdir('C:\\\\Users\\\\U2970\\\\Desktop')
    
    
def readerOut():
    os.chdir('C:\\\\Users\\\\U2970\\\\Desktop')


class nCounter(object):
    
    def __init__(self):
        self.length = 10
        self.rounder = 3

    def yielderOut(self):
        n = 0
        readerIn()
        while True:
            corr = raw_input('Enter the corridor you want or type "done" to leave: ').upper()
            if corr == 'done'.upper():
                sys.exit(0) # If user enters 'done' the program will exit
            else:
                for i in range(0,abs(len(corr)-6)): # Corridor designations are six characters long 
                    corr = '0' + corr # Adds zeros in front of the corridor number entered
                corr = 'C' + corr # Adds C to the beginning of corridor to create correct corridor designation
            for col in csv.DictReader(open('NORTH_DATA_EXPORT_10_12_16.csv')): # file to bring into program
                corridorRB = str(col['CORRIDOR_CODE_RB'])
                corridor = str(col['CORRIDOR_CODE'])
                begMi = float(col['BEGIN_MI']) # 
                begHi = float(col['BEGIN_MI'])
                begLi = float(col['BEGIN_MI'])
                endMi = float(col['END_MI'])
                lane = int(col['LANE'])
                dir_ = str(col['DIR'])
                group = corridor,begMi,endMi,lane,dir_
                n = n + 1
                try:
                    if corridor == corr and dir_ == 'I': # Corridor in the increasing direction
                        if abs(endMi - begMi) < self.length: # if the corridor in question is less than 10 miles in length
                            varsL = round(r.uniform(math.ceil(begMi),\ # take random sample from between the begin mile rounded
                                (math.floor(endMi))),self.rounder) # the end mile rounded down
                            if (varsL > begMi and varsL < endMi): # if the sampled point is between the begin and end mile
                                yield group,varsL
                            else:continue                
                        if abs(endMi - begMi) <= (2*self.length)\
                             and abs(endMi - begMi) > self.length:
                            varsM = round(r.uniform(math.ceil(begMi),\
                                (math.floor(begMi+self.length))),self.rounder)
                            yield group,varsM                    
                        elif abs(endMi - begMi) > (2*self.length):
                            for i in range(0,n):
                                begHi = math.floor(begHi)+(self.length)
                                varsN = round(r.uniform(math.ceil(begHi),\
                                (math.floor(begHi+self.length))),self.rounder)
                                if varsN < endMi and varsN > begMi:
                                    yield group,varsN
                                else:continue
                        else:continue
                    if corridor == corr and dir_ == 'D':
                        if abs(endMi - begMi) < self.length:
                            varsL = round(r.uniform(math.ceil(begMi),\
                                (math.floor(endMi))),self.rounder)
                            if (varsL < begMi and varsL > endMi):
                                yield group,varsL
                            else:continue
                        elif abs(endMi - begMi) <= (2*self.length)\
                             and abs(endMi - begMi) > self.length:
                            varsO = round(r.uniform(math.ceil(begMi),\
                                (math.floor(begMi-self.length))),self.rounder)
                            yield group,varsO
                        elif abs(endMi - begMi) > (2*self.length):
                            for i in range(0,n):
                                begLi = math.floor(begLi)-(self.length)
                                varsP = round(r.uniform(math.ceil(begLi),\
                                    (math.floor(begLi-self.length))),self.rounder)
                                if varsP > endMi and varsP < begMi:
                                    yield group,varsP
                                else:continue
                        else:continue
                except:break

def nCounterGo():
    readerOut()
    gen = nCounter()
    outfile = csv.writer(open('random_gen_writer.csv','wb'))
    for i in range(0,10):
        for line in gen.yielderOut():
            print line
            outfile.writerow(line)
    print'Have a nice day!'
nCounterGo()

