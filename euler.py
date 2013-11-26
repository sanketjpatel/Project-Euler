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
