import haversine as hs
from haversine import Unit
import csv
import sys
# loc1=(28.426846,77.088834)
# loc2=(28.394231,77.050308)
# print(hs.haversine(loc1,loc2,unit=Unit.MILES))


# print("Enter camera ID:")
# cameraID=str(input())

# cameraID='94'
# def opener(file,cameraID=f"'{cameraID}'"): #Utah is state code 49
#     path = file
#     lines=[]
#     with open(path, newline='\n') as csvfile:
#         reader = csv.reader(csvfile, delimiter=',')
#         spacer =0
#         extIDholder=""
#         stringspace=''
#         for row in reader:
#             if spacer>0:
#                 stringspace+=(row[0][5:])
#                 spacer-=1
#                 if spacer==0:
#                     lines.append(stringspace)
#                     stringspace=""
#                     extIDholder=""
#                 continue
#             if row[0][4:10]=='ExtId:':
#                 if row[0][11:]==cameraID:
#                     extIDholder=cameraID
#             if row[0][2:8]=='ExtId:':
#                 if row[0][9:]==cameraID:
#                     extIDholder=cameraID
#             elif extIDholder!="":
#                 if row==['    GPS:']:
#                     stringspace+=row[0][4:]
#                     spacer=2
#                 if row[0][2]=='G':
#                     temp=row[0][2:]+" "+row[1]
#                     lines.append(temp)
#                     extIDholder=""
#     return lines [0] #this returns long,lat and we need lat long for dist formula
# camerageo=(opener('combined_cams.txt'))[5:]
# camera=(float(camerageo[11:]),float(camerageo[:10]))


# print("Enter station ID:")
# stationID=str(input())
stationID='490354002'
def opener2(file,stationcode=stationID): #Utah is state code 49
    path = file
    lines=[]
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        i=0
        for row in reader:
            if row[0]+row[1]+row[2]==stationcode:
                return[row[0]+row[1]+row[2],row[5],row[6]] #output is [epa station code,lat,long]
stationgeo=(opener2('hourly_88101_2022.csv'))
station=(float(stationgeo[1]),float(stationgeo[2]))

def allopener(file): #Utah is state code 49
    path = file
    lines=[]
    with open(path, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        spacer =0
        extIDholder=""
        stringspace=[]
        for row in reader:
            if spacer>0:
                stringspace.append(row[0][5:])
                spacer-=1
                if spacer==0:
                    lines.append([extIDholder[1:-1],stringspace])
                    stringspace=[]
                    extIDholder=""
                continue
            if row[0][4:10]=='ExtId:':
                    extIDholder=row[0][11:]
            if row[0][2:8]=='ExtId:':
                    extIDholder=row[0][9:]
            elif extIDholder!="":
                if row==['    GPS:']:
                    stringspace+=row[0][4:]
                    spacer=2
                if row[0][2]=='G':
                    temp=[row[1],row[0][7:]]
                    lines.append([extIDholder[1:-1],temp])
                    extIDholder=""
    return lines  
# print(allopener('combined_cams.txt'))


# print("Enter difference:")
# difference=float(input())
difference=0.75
def dist_dif(dif=difference,file='combined_cams.txt'):
    allgeos=(allopener(file))
    camlist=[]
    for cam in allgeos:
        print(cam)
        camera=(float(cam[1][-2]),float(cam[1][-1]))
        if hs.haversine(station,camera,unit=Unit.MILES)<=dif:
            camlist.append(cam[0])
    return camlist
print(dist_dif())