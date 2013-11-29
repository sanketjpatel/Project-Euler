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



#def diagonals(m, n):
#    dummy1 = max(m,n)
#    dummy2= min(m,n)
#    n = dummy1
#    m = dummy2
#    total = 0
#    
#    for k in range(m+1, 0, -2):
#        total = total + (k-1)*((2*k*(2*k-1)/3) - 3*k + 2 + (n-m)*(2*k - 3)) #pxodd    
#    
#    for k in range(m, 0, -2):
#        total = total + (k-1)*((2*k*(2*k-1)/3) - 5*k + 6 + (n-m+1)*(2*k - 3)) #pxeven
#    
#    total = 2*total
#    
#    for k in range(m-1, 0, -2):
#        total = total - 2*k*(k-1) - (n-m)*(2*k - 1)
#    
#    for k in range(m-2, 0, -2):
#        total = total - 2*(k-1)*(k-1) - (n-m+1)*(2*k - 1)
#                
#    return total


#subrects returns the total number of sub-rectangles in a given rectangle of (x,y) dimension                
def subrects(x, y):
    dummy1 = min(x,y)
    dummy2 = max(x,y)
    x = dummy1
    y = dummy2
    #Found this closed form solution
    total = ((3*(x**2) + 3*x )*(y**2) + (16*(x**3) + 3*(x**2) - x)*y - 8*(x**4) + 2*(x**2) - 6*x) / 12 
    #straight = x*y*(x+1)*(y+1)/4
    #diagonal = diagonals(x,y)
    #total = straight +diagonal
    ## 2, 4, 6, ... 2m-2, (2m-1, 2m-1, ... x(n-m)), 2m-2, ... 6, 4, 2
    ## px1 = (2m-1)*(m*(n-m+2)-2)
    return total

def problem147(x,y):
    total = 0
    for i in range(1, x+1):
        for j in range(1, y+1):
            total = total + subrects(i,j)
    return total
