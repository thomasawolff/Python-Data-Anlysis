import os
import csv

os.chdir(os.getcwd())

with open('carrie_puzzle_data.csv') as f:
    data = csv.reader(f,delimiter=',')
    try:
        row1 = next(data)
        row2 = next(data)
        row3 = next(data)
        row4 = next(data)
        row5 = next(data)
        row6 = next(data)
        row7 = next(data)
        row8 = next(data)
        row9 = next(data)
        row10 = next(data)
        row11 = next(data)
        row12 = next(data)
        row13 = next(data)
        row14 = next(data)
        row15 = next(data)
        row16 = next(data)
        row17 = next(data)
        row18 = next(data)
        row19 = next(data)
        row20 = next(data)
    except: pass

    rowNum = row4
            

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
    with open('carrieJoeOutfile.csv','wb') as data:
        filename = csv.writer(data)
        filename.writerows(classesOut())
        filename.writerow(final)
        for line in dataJoined:
            filename.writerow(line)

    with open('Error report.csv','wb') as info:
        filename2 = csv.writer(info)
        filename2.writerow([studentsOut()[1]])
        filename2.writerow([attendOut()[2]])
        filename2.writerow([lessonLogOut()[1]])
    
rowsWriter()


  

