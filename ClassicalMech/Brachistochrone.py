import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
xb=1.; yb=-1.; r=xb/yb

def trig(theta1):
    if (np.abs(theta1)<0.0001):
        trig=0.
    else:
        trig=(theta1-np.sin(theta1))/(1-np.cos(theta1))-r
    return trig

def fillarray():
    theta1=fsolve(trig,1.1)
    biga=2*yb/(1-np.cos(theta1))
    th=np.arange(0,theta1,theta1/1000,dtype='float')
    xout=(biga/2)*(th-np.sin(th))
    yout=(biga/2)*(1-np.cos(th))
    return xout,yout
    
xb=1.; yb=-1.; r=xb/yb
x,y=fillarray()
xb=0.5; yb=-0.5; r=xb/yb
x2,y2=fillarray()
xb=0.3; yb=-0.9; r=xb/yb
x3,y3=fillarray()
xb=0.9; yb=-0.3; r=xb/yb
x4,y4=fillarray()
xb=0.9; yb=-0.1; r=xb/yb
x5,y5=fillarray()
plt.plot(x,y)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.plot(x4,y4)
plt.plot(x5,y5)
plt.show()
