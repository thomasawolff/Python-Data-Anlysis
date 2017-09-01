
import os
import csv
import math
import sys
import random as r

def readerIn():
    os.chdir('/home/user/Desktop')

def nCounter():
    readerIn()
    last = None
    for col in csv.DictReader(open('NORTH_7_6_2017_SEC.csv')):
        corridor = str(col['CORRIDOR'])
        begMi = float(col['BEGIN_MI'])
        begMiA = float(col['BEGIN_MI'])
        begMiB = float(col['BEGIN_MI'])
        endMi = float(col['END_MI'])
        lane = int(col['LANE'])
        dir_ = str(col['DIR'])
        if dir_ == 'I' and abs(endMi-begMi) > 12 and lane == 1:
            n = 0
            print corridor,begMi,endMi,'####################################################'
            print corridor,round(begMi,3),round(begMi+10,3),'...',\
                  round(r.uniform(begMi,begMi+10),3)
            while begMi < endMi and begMiA+10 < endMi:
                n = n + 1
                begMiA = (begMiA + 1)
                if n % 10 == 0:
                    if r.uniform(begMiA,begMiA+10) < endMi and begMiA+10 < endMi:
                        print corridor,round(begMiA,3),round(begMiA+10,3),'...',\
                              round(r.uniform(begMiA,begMiA+10),3)
                        if abs(begMiA+10 - endMi) < 10 and abs(begMiA+10 - endMi) > 2:
                            print corridor,round(begMiA+10,3),round(endMi,3),'...',\
                                  round(r.uniform(begMiA+10,endMi),3)
                        elif abs(begMiA+10 - endMi) < 2:
                            print corridor,endMi
                        else: continue
                    else: print corridor,round(begMiA,3),round(endMi,3),'...',\
                          round(r.uniform(begMiA,endMi),3)
                          break
                else: pass
            else:
                print corridor,round(begMi+10,3),round(endMi,3),'...',\
                      round(r.uniform(begMi+10,endMi),3)
        elif (endMi - begMi) <= 12 and (endMi - begMi) > 2 \
             and r.uniform(begMi,endMi) < endMi and lane == 1:
            print corridor,round(begMi,3),round(endMi,3),'...',\
                  round(r.uniform(begMi,endMi),3),'--------'
        else: pass 
nCounter()

