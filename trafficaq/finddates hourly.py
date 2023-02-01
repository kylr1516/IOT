#look at the file to determine which column you need. I'm not coding that mess

import csv

def opener(file,col):#opens the csv file
    path = file
    lines=[]
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            lines.append([row[0],row[col]])
    lines=lines[1:]
    return lines
#print(opener("2021-PM2.5.csv",2)[:10]) 


def gapfinder(file,diff=30,col=2):#returns all the times for the given column where the diff was reached
    data = opener(file,col)
    dates=[]
    missing=[]
    previousday=data[0][1]
    #print("first day check:",previousday)
    for line in data:
        try:
            if abs(eval(previousday)-eval(line[1])) >=diff:
                if line[0] not in dates:
                    dates.append(line[0])
            previousday=line[1]
        except SyntaxError:
            missing.append(line[0])
    return dates
#print(gapfinder('2021-PM2.5.csv'))

def time_dictionary(file,cols,diff=30):#returns dict of all the time and dates at which the diff was surpassed and how many stations also recorded that diff
    all_times={}
    for i in range(1,cols+1):
        dates=(gapfinder(file,diff=diff,col=i))
        for j in range(len(dates)):
            if dates[j] not in all_times:
                all_times[dates[j]]=str(i)
            else:
                all_times[dates[j]]+=','
                all_times[dates[j]]+=(str(i))
    return all_times
print(time_dictionary('2021-PM2.5.csv',22))