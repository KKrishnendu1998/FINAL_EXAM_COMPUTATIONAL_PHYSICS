#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 10:
Created on Fri Jun  5 08:17:22 2020

@author: krishnendu
"""

import numpy as np
import matplotlib.pyplot as plt

def fun(x):
        if abs(x)<1:
         return 1
        else :
         return 0
     
        
xmin=-50    #xmin value
xmax=50     #xmax value

    
def fourier(n):
   
   
   numpoints=n         #number of sample points

   dx=(xmax-xmin)/(numpoints-1)      

   sampled_data=np.zeros(numpoints)

   xarr=np.zeros(numpoints)

   for i in range(numpoints):
    sampled_data[i]=fun(xmin+i*dx)          #sampling the data
    xarr[i]=xmin+i*dx

   nft=np.fft.fft(sampled_data,norm='ortho')       #computing dft of the data using numpy.fft.fft

   karr=np.fft.fftfreq(numpoints,d=dx)          #computing the frequencies 

   karr=2*np.pi*karr
   factor=np.exp(-1j*karr*xmin)
   aft=dx*np.sqrt(numpoints/(2.0*np.pi))*factor*nft
   karr=np.fft.fftshift(karr)         #shifting the frequencies

   aft=np.fft.fftshift(aft)           #shifting the fourier transform

   plt.plot(karr,abs(aft))       #plotting the fourier transform computed by numpy.fft.fft
    
   plt.title("numpoints="+str(n))
   plt.suptitle("Fourier transform of the function")
   plt.xlabel("frequency(k)",size=14)
   plt.grid()
   plt.show()
 
x=np.linspace(-5,5,100)          
plt.plot(x,[fun(x[i]) for i in range(len(x))])  
plt.xlabel("x",size=14)
plt.ylabel("f(x)",size=14)
plt.title("plot of the function",size=18)
plt.grid()
plt.show()

fourier(512)
fourier(1024)
fourier(2048)

    

