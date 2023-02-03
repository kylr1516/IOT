import csv

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
# print(opener('hourly_88101_2022.csv','49')[-15:]) 

def firstvalue(data):
    i=0
    while i<len(data):
        if data[i][-1] != '':
            return data[i][-1] 
        i+=1

#returns all the times for the given state where the diff was reached and how many stations recorded that diff
def gapfinder(file,state='49',diff=30):#may run errors when reaching the end of 1 year and starting a year on a different station 
    data = opener(file,state)
    dates={}
    missing=[]
    previousday=firstvalue(data)
    print("first day check:",previousday)
    for line in data:
        try:
            if abs(eval(previousday)-eval(line[-1])) >=diff:
                if line[-2] not in dates:
                    dates[line[-2]]=1
                else:
                    dates[line[-2]]+=1
            previousday=line[-1]
        except SyntaxError:
            missing.append(line[-2])
    # print("# of dates missing",len(missing))
    return dates
print(gapfinder('hourly_88101_2021.csv'))