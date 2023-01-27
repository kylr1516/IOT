#tester.py////////////////////////////////////////////////////////////////////////////////////////////////////
"""with open('66.219.235.215.txt', 'r') as myfile:
    data=myfile.read()
    print([i.strip().split() for i in data.split(' \\n') if len(i.strip())>0])"""

"""logFile = "IP_Fix.txt"

with open(logFile) as f:
    content = f.readlines()      
# you may also want to remove empty lines
content = [l.strip() for l in content if l.strip()]   


for line in content:     
    line = line.replace(" ", ",")
    print(line[-4:])  # for each line, replace the space with ,
"""

'''
fin = open("50.243.6.69.txt", "r") 
fout = open("output.txt", "w")
for line in fin:
   new_line = line.replace('\t', ' ')
   fout.write(new_line) 

fin.close()
fout.close()
'''

#bargraph.py////////////////////////////////////////////////////////////////////////////////////////////////////////
import numpy as np
import matplotlib.pyplot as plt

def correct_finder(file,param=['False ne','True pos','False po','True Neg']):
    logFile = file

    with open(logFile) as f:
        content = f.readlines()      
    content = [l.strip() for l in content if l.strip()]   
    line_val=0
    ping_list = list()
    for line in content:   
        if param.count(line[:8]):
            line = line.replace(" ", "")
            line = line.replace("/0", "/1")
            for i in range(len(line)):
                if line[i]==':':
                    ping_list += [line[:i]]
                    if eval(line[i+1:]) <= 1:
                        ping_list += [eval(line[i+1:])]
                    else:
                        ping_list += [1-((ping_list[-2]))]#need to diff between flase neg(one above) and false pos(one below)
                        print(ping_list[-1])
                        print(ping_list[-3])
    return (ping_list)
#end copy///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

with open('utah_SLC_2021_all.csv', 'r') as myfile:
    data=myfile.read()
    data = data[60:]
    data=[i.strip().split() for i in data.split(' \\n') if len(i.strip())>0]
    data=data[0]
#print(data[0][0:15]) ##this goes [which line][how many characters]--want last to be comma seperated

def gapfindersite(data,siteID,diff=30):#site ID needs to be a string
    dates=[]
    data=[line.split(",") for line in data]
    data=[line for line in data if line[1]==siteID]
    previousday=data[0][2]
    print("first day check:",previousday)
    for line in data:
        if abs(eval(previousday)-eval(line[2])) >=diff:
            if line[0] not in dates:
                dates.append(line[0])
        previousday=line[2]

    return dates
#print(gapfindersite(data,"490352005"))

def gapfinder(data,diff=30):
    dates=[]
    data=[line.split(",") for line in data]
    previousday=data[0][2]
    print("first day check:",previousday)
    for line in data:
        if abs(eval(previousday)-eval(line[2])) >=diff:
            if line[0] not in dates:
                dates.append(line[0])
        previousday=line[2]
    return dates
print(gapfinder(data,))