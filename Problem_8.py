#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 8:
Created on Fri Jun  5 07:47:39 2020

@author: krishnendu
"""

import numpy as np
from scipy.integrate import *
import matplotlib.pyplot as plt
a=0     #starting value
b=1    #end value
def fun(x,y):         #function that returns the derivative 
    return np.vstack((y[1],4*(y[0]-x)))
def bc(ya,yb):        #function for boundary conditions
    return np.array([ya[0],yb[0]-2])
x=np.linspace(a,b,50)       #creating mesh points
y=np.zeros((2,x.size),dtype="double")
y[0]=1              #initial guess of the solution
sol=solve_bvp(fun,bc,x,y)         #solving the problem using solve_bvp

y=sol.sol(x)[0]
y1=(np.exp(1)**2/(np.exp(1)**4-1))*(np.exp(2*x)-np.exp(-2*x))+x
plt.plot(x,y,"go-",ms=4,label="solve_bvp")      #plotting the solution using solve_bvp
plt.plot(x,y1,"r-",label="analytical")                #plotting the analytical solution
plt.legend()
plt.xlabel("x",size=18)
plt.ylabel("y",size=18)
plt.title("Problem 8",size=18)
plt.grid()
plt.show()

print("the relative in my computed solution in percentage error is :",abs((y-y1)/y1)*100 )