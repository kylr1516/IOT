#look at the file to determine which column you need. I'm not coding that mess

import csv

def opener(file,col):
    path = file
    lines=[]
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            lines.append([row[0],row[col]])
    lines=lines[1:]
    return lines
#print(data[0][0:15]) ##this goes [which line][how many characters]--want last to be comma seperated sometimes 


def gapfinder(file,diff=30,mod=True,col=2):
    data = opener(file,col)
    dates=[]
    #data=[line.split(",") for line in data]
    previousday=data[1][1]
    print("first day check:",previousday)
    for line in data:
        if abs(eval(previousday)-eval(line[1])) >=diff:
            if line[0] not in dates:
                dates.append(line[0])
        previousday=line[1]
    return dates
(gapfinder('2021-PM2.5.csv'))