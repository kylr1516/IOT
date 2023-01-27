with open('66.219.235.215.txt', 'r') as myfile:
    data=myfile.read()
    print([i.strip().split() for i in data.split(' \\n') if len(i.strip())>0])

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