import csv

def opener(file,col):#opens the csv file
    path = file
    lines=[]
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            lines.append([row[0],row[col]])
    return lines

#cols=BV-MC,CV-MC,ED-MC,EN-MC,H3-MC,H3-MC-CO,HA-MC,HC-MC,HV-MC,HW-MC,IP-MC,LN-MC,NR-MC,RP-MC,RS-MC,RS-MC-CO,SF-MC,!!!SM-MC-CO,SM-MC-CO2,UT-MC,UT-MC-CO,V4-MC (starting at 1)
#for some reason some end in -MC-CO or -MC-CO2 rather than just -MC while having the same site abreviation
#to acces these use the site ID then .1 for -MC and .2 for -MC-CO and .3 for -MC-CO2
#also I have no idea what UT would stand for except average of Utah and it doesn't work to the average with the provided stations
#also HA,IP appears to not exist
#there are also sites listed on the web with valid sensors that are not included in this list
coldict={490110004:1,
    490352005:2,
    490450004:3,
    490210005:4,
    490353013.1:5,
    490353013.2:6,
    0.1:7,
    490530007:8,
    490571003:9,
    490353006:10,
    0.2:11,
    490494001:12,
    490354002:13,
    490353010:14,
    490130002.1:15,
    490130002.2:16,
    490495010:17,
    490050007.2:18,
    490050007.3:19,
    0.3:20,
    0.4:21,
    490471004:22,
    }


#print(opener("2021-PM2.5.csv",11)[:10]) #look at the file to determine which column you need. I'm not coding that mess?

def firstvalue(data):
    i=0
    while i<len(data):
        if data[i][1] != '':
            return data[i][1] 
        i+=1

def gapfinder(file,diff=30,col=2):#returns all the times for the given column where the diff was reached
    data = opener(file,col)
    data=data[1:]
    dates=[]
    missing=[]
    previousday=firstvalue(data)
    # print("first day check:",previousday)
    for line in data:
        try:
            if abs(eval(previousday)-eval(line[1])) >=diff:
                if line[0] not in dates:
                    dates.append(line[0])
            previousday=line[1]
        except SyntaxError:
            missing.append(line[0])
    # print("# of dates missing",len(missing))
    return dates
#print(gapfinder('2021-PM2.5.csv'))

def time_dictionary(file,cols=22,diff=30):#returns dict of all the time and dates at which the diff was surpassed and how many stations also recorded that diff
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
# print(time_dictionary('2021-PM2.5.csv'))
time_dic=time_dictionary('2021-PM2.5.csv')
for date in (time_dic):
    print(date)
    print(len(time_dic[date]))