#for mod to be True:
#
#the only columns that need to be deleted are source and POC however,
#the way I changed the csv was by deleting the columns titled source, POC, units, site name, and everything right of site name

import csv

def opener(file,mod):
    path = file
    lines=[]
    if mod:
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                lines.append([row[0],row[1],row[2]])
    else:
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                lines.append([row[0],row[2],row[4]])
    lines=lines[1:]
    return lines
#print(data[0][0:15]) ##this goes [which line][how many characters]--want last to be comma seperated sometimes --error when try to do this with the dates as it tries to eval a date and does want to divide 0X

def gapfindersite(file,siteID,diff=30,mod=True):#site ID needs to be a string
    data = opener(file,mod)
    dates=[]
    data=[line for line in data if line[1]==siteID]
    previousday=data[0][2]
    print("first day check:",previousday)
    for line in data:
        if abs(eval(previousday)-eval(line[2])) >=diff:
            if line[0] not in dates:
                dates.append(line[0])
        previousday=line[2]

    return dates
print(gapfindersite('utah_SLC_2021_all.csv',"490352005"))

def gapfinder(file,diff=30,mod=True):
    data = opener(file,mod)
    dates=[]
    #data=[line.split(",") for line in data]
    previousday=data[0][2]
    print("first day check:",previousday)
    for line in data:
        if abs(eval(previousday)-eval(line[2])) >=diff:
            if line[0] not in dates:
                dates.append(line[0])
        previousday=line[2]
    return dates
print(gapfinder('utah_SLC_2021_all.csv'))