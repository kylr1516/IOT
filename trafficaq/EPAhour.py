import csv
import sys

def opener(file,state): #Utah is state code 49
    path = file
    lines=[]
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        rownum=0
        for row in reader:
            if rownum==0:
                lines=[]
                rownum+=1
            elif row[0]==state:
                lines.append([state+row[1]+row[2],row[5],row[6],row[9]+' '+row[10],row[13]])
    return lines #output is [epa station code,lat,long,date+time,pm2.5 val]
def opener2(file,state): #Utah is state code 49
    path = file
    lines=[]
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        rownum=0
        for row in reader:
            if rownum==0:
                lines=[]
                rownum+=1
            elif row[0]==state:
                lines.append([state+row[1]+row[2],row[5],row[6],row[9],row[10],row[13]])
    return lines #output is [epa station code,lat,long,date,time,pm2.5 val]
# print(opener('hourly_88101_2022.csv','49')[-15:]) 

def firstvalue(data):
    i=0
    while i<len(data):
        if data[i][-1] != '':
            return data[i][-1] 
        i+=1

#returns all the times for the given state where the diff was reached and how many stations recorded that diff as a dictionary
def gapfinder(file,state='49',diff=30,stationcode=0):#may run errors when reaching the end of 1 year and starting a year on a different station 
    rawdata = opener(file,state)
    if stationcode:
        data=[]
        for line in rawdata:
            if line[0]==stationcode:
                data.append(line)

    else:
        data=rawdata
    dates={}
    missing=[]
    previousday=firstvalue(data)
    print("first day check:",previousday)
    for line in data:
        try:
            if abs(eval(previousday)-eval(line[-1])) >=diff:
                if line[-2] not in dates:
                    print(line[-1])
                    dates[line[-2]]=1
                else:
                    dates[line[-2]]+=1
            previousday=line[-1]
        except SyntaxError:
            missing.append(line[-2])
    print("# of dates missing",len(missing))
    return dates
# print(gapfinder('hourly_88101_2021.csv',stationcode='490353013'))


def site_csv_maker(file,stationcode,writefile,state='49'):
    rawdata = opener(file,state)
    data=[]
    for line in rawdata:
        if line[0]==stationcode:
            data.append(line)
    orig_std_out= sys.stdout
    with open(writefile,'w') as f:
        sys.stdout=f
        for lines in data:
            print(lines)
        sys.stdout=orig_std_out
# site_csv_maker('hourly_88101_2021.csv','490353013','490353013.csv')

def site_csv_hour_maker(file,stationcode,writefile,hours,state='49'):
    rawdata = opener2(file,state)
    data=[]
    for line in rawdata:
        if line[0]==stationcode:
            for hour in hours:
                if line[-2]==hour:
                    data.append(line)
    orig_std_out= sys.stdout
    with open(writefile,'w') as f:
        sys.stdout=f
        for lines in data:
            print(lines)
        sys.stdout=orig_std_out

site_csv_hour_maker('hourly_88101_2021.csv','490354002','490354002.csv',['12:00','09:00'])

# stations of note= 490353013, 490450004, 490494001, 490353016, 490495010, 490353013, 490352005, 490353015, 490494002
#most of these spikes occured in august and on the 6th and 18th