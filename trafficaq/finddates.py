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
"""iteration=iter(correct_finder('/home/kyle2004/IOT/manualanalisys-v4.0 copy.txt'))
dic=dict(zip(iteration,iteration))
print(dic)"""#failure do to overwriting dictionary entries with the same name
"""my_list=correct_finder('/home/kyle2004/IOT/manualanalisys-v4.0 copy.txt')
new=[my_list[i] for i in range(len(my_list)) if i%2!=0]
#print(new)
import numpy as np
from matplotlib import pyplot as plt"""
def bargraph(list):
    x=[i for i in range(len(list))]
    plt.bar(x,list)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("TITLE")
    return plt.show()

def bars(list):
    x=[i for i in range(len(list))]
    plt.bar(x,list)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("TITLE")

"""for i in range(len(new)):
    if i%4==0:
        bars(new[i:i+4])#maybe try adding them all together?
plt.show()"""

def march(val=0):
    if val<3 :
        val+=1
    else:
        val=0
    return val


"""tot_list=[0,0,0,0]
val=0
for i in range(len(new)):
    tot_list[val]+=new[i]
    val=march(val)

print(sum(new))#currently only worth 16 data vals,should be 26
print(len(my_list))
bargraph(tot_list)"""
#print(correct_finder('/home/kyle2004/IOT/manualanalisys-v4.0 copy.txt')[:10])

#d = dict(zip(*[iter(some_list)] * 2))


#bargraph(correct_finder('/home/kyle2004/IOT/manualanalisys-v4.0 copy.txt')[:10])
#end copy///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

with open('utah_SLC_2021_all.csv', 'r') as myfile:
    data=myfile.read()
    data = data[60:]
    data=[i.strip().split() for i in data.split(' \\n') if len(i.strip())>0]
print(data[0][0][0:15]) ##this goes [all][which line][how many characters]--want last to be comma seperated