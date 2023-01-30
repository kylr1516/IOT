with open('utah_SLC_2021_all.csv', 'r') as myfile:
    data=myfile.read()
    data = data[60:]
    data=[i.strip().split() for i in data.split(' \\n') if len(i.strip())>0]
    data=data[0]
#print(data[0][0:15]) ##this goes [which line][how many characters]--want last to be comma seperated sometimes --error when try to do this with the dates as it tries to eval a date and does want to divide 0X

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