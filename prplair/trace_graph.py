import numpy as np
from matplotlib import pyplot as plt
import scipy.stats

def create_plot(x,y):
    plt.plot(x,y)
    plt.show()
    return None

def create_scatter(x,y):
    ##x     ##time since start
    ##y     ##traceroute signitaure/ping time
    plt.plot(x,y,".",markersize=1,alpha=0.25)
    return None

def line(theta_num=1,iteration=-1,theta=np.array([1,2,3,4,5]),X=np.array([1,2,3,4,5])):
    #attempt at helper to allow bestfit_scatter to accept any degree
    string=[]
    while theta_num>=0:
        iteration+=1
        string += (theta[theta_num] * pow(X,iteration))
        theta_num -=1
    return string

def bestfit_scatter(array,degree):
    #does may not work completely yet
    #array is an array of 2 col; left is x, right is y
    '''may give up on, spike line works but only if array is in order'''
    dt = array
    # Preparing X and y from the given data
    X = dt[:, 0]
    y = dt[:, 1]

    # Calculating parameters;intercept=theta[1] and slope=theta[0])
    theta = np.polyfit(X, y, degree)

    #calculating the y-axis values using the x-values and theta values
    
    y_line = line(degree,-1,theta,X)

    # Plotting the data points and the best fit line
    plt.scatter(X, y)
    plt.plot(X, y_line, 'r')
    plt.title('Traceroute time over time')
    plt.xlabel('time')
    plt.ylabel('traceroute')

    plt.show()



def bestfit_histogram(array, title, bin_count=25, xlab = 'X', ylab = 'Y'):
    ##1 col array with only points of data
    ##useful for showing common values for ping,traceroute, etc and show how often outliers occur
    ##can be used in 2 graphs to represent the change in ping ditributions between a moving and non moving device

    dt=array
    _, bins, _ = plt.hist(dt, bin_count, density=1, alpha=0.5)
    mn, std = scipy.stats.norm.fit(dt)
    y_curve = scipy.stats.norm.pdf(bins, mn, std)
    plt.plot(bins, y_curve, 'k')
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.show()

def spike_line_array(array, title, fill = 0 , xlab = 'X', ylab = 'Y', draw_to = 0, min_trace = 1):
    #takes 2 col array with x on left and y on right
    #x vals need to be in order to look nice
    dt=array
    x = dt[:, 0]
    ys = dt[:, 1]
    plt.plot(x, ys, '-')
    if fill:
        plt.fill_between(x, ys, draw_to , ys>min_trace , facecolor='tomato', alpha=1)
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    return plt.show()

def spike_line2(x,ys, title, fill = 0 , xlab = 'X', ylab = 'Y'):
    ## needs one array for both x and y compnents
    plt.plot(x, ys, '-')
    if fill:
        plt.fill_between(x, ys, facecolor='g', alpha=0.6)
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    return plt.show()

def spike_line1(x,y, title, xlab = 'X', ylab = 'Y'):
    ## needs one array for both x and y compnents
    plt.locator_params(axis=y, tight = True, nbins=10)
    plt.fill_between(x, y, facecolor='g', alpha=0.6)
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.yticks(color='w')
    return plt.show()

####testers
dt=np.array([[0.5, 0.28],[0.5, 0.29],[0.5, 0.33],[0.7, 0.21],[0.7, 0.23],[0.7, 0.26],[0.8, 0.24],[0.8, 0.25],[0.8, 0.29],[0.9, 0.28],[0.9, 0.30],[0.9, 0.31],[1.0, 0.30],[1.0, 0.33],[1.0, 0.35]])
#^quadratic
dt2 = np.array([[0.05, 0.11],[0.13, 0.14],[0.19, 0.17],[0.24, 0.21],[0.27, 0.24],[0.29, 0.32],[0.32, 0.30],[0.36, 0.39],[0.37, 0.42],[0.40, 0.40],[0.07, 0.09],[0.02, 0.04],[0.15, 0.19],[0.39, 0.32],[0.43, 0.48],[0.44, 0.41],[0.47, 0.49],[0.50, 0.57],[0.53, 0.59],[0.57, 0.51],[0.58, 0.60]])
dt3 = np.array([[0.05, 0.11],[0.13, 0.14],[0.19, 0.17],[0.24, 0.21],[0.27, 0.24],[0.29, 0.32],[0.32, 0.30],[0.36, 0.39],[0.37, 0.42],[0.40, 0.40],[0.43, 0.48],[0.44, 0.41],[0.47, 0.49],[0.50, 0.57],[0.53, 0.59],[0.57, 0.51],[0.58, 0.60]])
#^linear
h=[i for i in range(100)]
g=(200 + np.random.randn(100))
s=[i for i in range(1100,1200)]
dt4= (np.column_stack((h,s)))
l=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
dt5= (np.column_stack((h,l)))
s=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
dt6= (np.column_stack((h,s)))
p=(1+np.random.randn(100))
dt7= (np.column_stack((h,p)))
'''
spike_line_array(dt7,"hello",1,'x','y',-1,1)

'''
#spike_line_array(array, title, fill = 0 , xlab = 'X', ylab = 'Y', draw_to = 0, min_trace = 1):


def ping_finder(file):
    logFile = file

    with open(logFile) as f:
        content = f.readlines()      
    content = [l.strip() for l in content if l.strip()]   

    ping_list = list()
    for line in content:   
        line = line.replace(" ", ",")
        line = (line[-4:]) 
        ping_list += [line]

    return (ping_list)
ping = ping_finder("IP_Fix_50.txt")
length = len(ping)
long=[i for i in range(length)]
"""spike_line1(long,ping,"Ping over time for 50.243.6.69",'Time since start (Unix)','Ping')
ping2 = ping_finder("66.219.235.215.txt")
length2=len(ping2)
long2=[i for i in range(length2)]
spike_line1(long2,ping2,"Ping over time for 66.219.235.215",'Time since start (Unix)','Ping')

"""

#    for i in range(len(ping_list)):
#        ping_list[i] = float(ping_list[i])

#difference in traceroutes. return 2 arrays:one with difference and one with line number
def diff_trace(file):
    logFile = file

    with open(logFile) as f:
        content = f.readlines()      
    content = [l.strip() for l in content if l.strip()]   

    trace_list = list()
    for line in content:   
        line = line.replace(" ", ",")
        line = (line[19:-5]) 
        trace_list += [line]

    x=[i for i in range(len(trace_list))]
    count=0
    for j in range(len(trace_list)):
        high=[100000,1000000]
        high.append(10000)
    for j in range(len(trace_list)):
        high.append(100000)
        count=10000
        for i in range(10):
            """if len(set(trace_list[i]).difference(set(trace_list[j])))<high[j]:
                high[j]=len(set(trace_list[i]).difference(set(trace_list[j])))"""
            count = sum(1 for a, b in zip(trace_list[i], trace_list[j]) if a != b) + abs(len(trace_list[i]) - len(trace_list[j]))
            if count<high[j]:
                high[j]=count
    return x,high[:-3]


x,y=diff_trace("IP_Fix_50.txt")
spike_line1(x,y,"Diff over time for 50.243.6.69",'Time since start','diff')
x,y=diff_trace("66.219.235.215.txt")
spike_line1(x,y,"Diff over time for 66.219.235.215",'Time since start ','diff')