import os
import csv
import sys

os.chdir(os.getcwd())

input_ = raw_input('Enter the .csv file you want used or Enter "done" to leave: ')
if input_ == 'done':
    sys.exit(0)
row = raw_input('Enter a row number between 2 and 10: ')

def fileOpen():
    try:
        with open(input_) as f:
            data = csv.reader(f,delimiter=',')
            try:
                row1 = next(data)
            except Exception as e: pass
            try:
                row2 = next(data)
            except Exception as e: pass
            try:
                row3 = next(data)
            except Exception as e: pass
            try:
                row4 = next(data)
            except Exception as e: pass
            try:
                row5 = next(data)
            except Exception as e: pass
            try:
                row6 = next(data)
            except Exception as e: pass
            try:
                row7 = next(data)
            except Exception as e: pass
            try:
                row8 = next(data)
            except Exception as e: pass
            try:
                row9 = next(data)
            except Exception as e: pass
            try:
                row10 = next(data)
            except Exception as e: pass
                
            if row == str(2):
                return row1,row2,e
            if row == str(3):
                return row1,row3,e
            if row == str(4):
                return row1,row4,e
            if row == str(5):
                return row1,row5,e
            if row == str(6):
                return row1,row6,e
            if row == str(7):
                return row1,row7,e
            if row == str(8):
                return row1,row8,e
            if row == str(9):
                return row1,row9,e
            if row == str(10):
                return row1,row10,e
            
    except IOError: print 'You entered an invalid file name'

try:
    row1 = fileOpen()[0]
    rowNum = fileOpen()[1]
except TypeError:
    raw_input('Failed. Press ENTER to exit')
    sys.exit(0)


def classesOut():
    final = []
    f = row1.index('proj_id')
    classes = [[] for i in xrange(0)]
    classes.append(rowNum[f:row1.index('class_type_other')])
    final.append(classes[0])
    print ''

    return final


def studentsOut():
    h = 1
    i = 2
    e = 5
    final = []
    try:
        while e < row1.index('students_complete'):
            students = [[] for i in xrange(0)]
            students.append(rowNum[row1.index('a_first_'+str(h)):\
                                 row1.index('a_first_'+str(i))])
            final.append(students[0])
            i = i + 1
            h = h + 1
            e = e + (row1.index('a_first_'+str(i))-row1.index('a_first_'+str(h)))
    except Exception as e: pass

    return final,e
            

def attendOut():
    f = 1
    h = 5
    final = []
    attendSmall = []
    attendSmall.append(row1[row1.index('attendance_sheet_complete')-1])
    small = str(attendSmall[0])
    s = int(small[-1])
    b = int(small[-6]+small[-5])
    r = row1.index('attend_1___1')
    try:
        while r < row1.index('attendance_sheet_complete'):
            attend = [[] for i in xrange(0)]
            attend.append(rowNum[row1.index('attend_'+str(f)+'___1'):\
                               (row1.index('attend_'+str(f)+'___'+str(s))+1)])
            final.append(attend[0])
            f = f + 1
            r = r + 1
    except Exception as e: pass

    return final,s,e


def lessonLogOut():
    i = 1
    final = []
    LL1S = row1.index('f_teacher_1')
    try:
        while LL1S < row1.index('f_complete_post'):
            lesson = [[] for i in xrange(0)]
            lesson.append(rowNum[row1.index('f_teacher_'+str(i)):\
                               (row1.index('lesson_'+str(i)+'_log_complete'))])
            final.append(lesson[0])
            i = i + 1
            LL1S = LL1S + 1
    except Exception as e: pass

    return final,e


def rowsWriter():
    attend = []
    labels = []
    final = []
    dataJoined = [(e1 + e2 + e3) for (e1, e2, e3)\
                      in zip(studentsOut()[0],attendOut()[0],lessonLogOut()[0])]
    
    for i in range(1,attendOut()[1]+1):
        attend.append('attend'+'_'+str(i))
                               
    labels.append(['a_first','a_last','a_dob','a_grade','a_gradeother',\
                           'a_sex','a_race_1','a_race_2','a_race_3',\
                           'a_race_4', 'a_race_5','a_race_6','a_race_7'])

    final = labels[0] + attend
    with open(input_+'_Row'+row+'_Output.csv','wb') as data:
        filename = csv.writer(data)
        filename.writerows(classesOut())
        filename.writerow(final)
        for line in dataJoined:
            filename.writerow(line)

    with open(input_+'_Row'+row+'_Err_Rep.csv','wb') as info:
        filename2 = csv.writer(info)
        filename2.writerow([studentsOut()[1]])
        filename2.writerow([attendOut()[2]])
        filename2.writerow([lessonLogOut()[1]])
        filename2.writerow([fileOpen()[2]])

    raw_input('File was created. Press ENTER to exit')
    sys.exit(0)

rowsWriter()

