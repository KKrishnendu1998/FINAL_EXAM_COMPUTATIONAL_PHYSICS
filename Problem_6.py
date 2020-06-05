#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 6:
Created on Fri Jun  5 08:04:11 2020

@author: krishnendu
"""

import numpy as np
from scipy.integrate import *
import matplotlib.pyplot as plt
def fun1(x,y):                   ##defining the function for derivative 
    return [32*y[0]+66*y[1]+(2/3)*x+(2/3),-66*y[0]-133*y[1]-(1/3)*x-1/3]
x=np.linspace(0,0.5,1000)           #creating mesh points
s=solve_ivp(fun1,[0,0.5],[1/3,1/3],dense_output="True")     #solving the probelm using solve_ivp 
plt.plot(x,s.sol(x).T[:,0],label='y1')  
plt.plot(x,s.sol(x).T[:,1],label='y2')        
plt.legend()
plt.xlabel("x",size=18)
plt.ylabel("y",size=18)
plt.title("Problem 6",size=18)
plt.grid()
plt.show()


