import numpy as np

def problem1():
    x1 = np.arange(0, 1000, 3)
    x2 = np.arange(0, 1000, 5)
    x3 = np.arange(0, 1000, 15)
    return sum(x1) + sum(x2) - sum(x3)
    
def problem2():
    ans = 0
    f = [1, 1]
    fnew = f[len(f)-1] + f[len(f)-2]
    while (fnew < 4000000):
        fnew = f[len(f)-1] + f[len(f)-2]
        f.append(fnew)
        if (fnew%2 == 0):
            ans = ans + fnew
    return ans
    
def problem44():
#I am solving this in order n^2 for now. If it doesn't work out, will change the algorithm
#Giving a limit to the pentagonal chain, because I don't want the program to run forever.
#Should remove it and use a while loop once you have a working solution.
    p = []
    counter = 1
    i = 1
    #print "Start"
    while (counter):
        p.append(i*(3*i - 1)/2)
        for j in range(i-1):                        
            y = p[i-1] - p[j]                        
            if (((24*y + 1)**0.5)%6 == 5):
                #print i-1, j
                x = p[i-1]+p[j]
                if (((24*x + 1)**0.5)%6 == 5):
                    print "Solution has been found!"
                    counter = 0
                    print i-1, j, p[i-1], p[j], x, y
                    print "Answer is ", y
                    return y
        i = i+1

def problem147(x, y):
    #straight = x*y*(x+1)*(y+1)/4
    #diagonal = 
    # 2, 4, 6, ... 2m-2, (2m-1, 2m-1, ... x(n-m)), 2m-2, ... 6, 4, 2
    # px1 = (2m-1)*(m*(n-m+2)-2)
