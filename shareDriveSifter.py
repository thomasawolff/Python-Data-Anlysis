import sys
import os
import pprint as p

'''This code is designed to sift around through a sharedrive'''

def readerFunc():
    n = 0
    print''
    userIn = raw_input('Do you want to continue? yes or no: ')
    while True:
        if userIn.lower() != 'yes':break
        elif userIn.lower() == 'yes':
            print ''
            print os.getcwd() # prints present directory
            print ''
            enter1 = raw_input('Enter folder you want to access: ').upper()
            if len(enter1) == 1:
                enter1 = enter1 + ':\\'
            print ''
            if enter1.lower() == 'done':
                print ''
                print os.getcwd()
                print 'Have a nice day'
                break
            else:
                try:
                    os.chdir(enter1) # changes directory to enter1
                    print os.getcwd()
                    p.pprint(os.listdir(os.getcwd())) # prints out contents of present directory
                    n = n + 1
                    if n > 0:
                        for i in range(0,n):continue
                except:
                    print 'That was not a valid folder'
                    continue
        else:
            print ''
            print'Have a nice day'
            
readerFunc()
