#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 4:
Created on Fri Jun  5 08:44:57 2020

@author: krishnendu
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

"""In theis question there is not mentioned about the frequency of the sampling of the data .I am taking
 dx=1 for this problem """
"""  a  """
n=1024
random=np.random.rand(n)
dx=1
x=np.arange(1,n+1,dx)

plt.scatter(x,random)
plt.xlabel("x")
plt.ylabel("random numbers ")
plt.title("plot of 1024 random numbers",size=18)
plt.show()

""" b """
dft=np.fft.fft(random,norm="ortho")
freq=np.fft.fftfreq(n,dx)
dft=np.fft.fftshift(dft)
freq=np.fft.fftshift(freq)
freq=2*np.pi*freq
ps=(abs(dft))**2

plt.plot(freq,ps)
plt.xlabel("frequency(k)")
plt.ylabel("spectral density")
plt.title("plot of the power spectrum ",size=16)
plt.show()

""" c """
print("The minimum value of the wavevector k= ",min(freq))

print("The maximum value of the wavevector k= ",max(freq))

""" d """

plt.hist(ps,bins=n//5,density="True")
plt.title("Histogram of the power spectrum",size=16)
plt.show()

#Bartlet method 
#In the following code we have splitted the data in 204 segements where each segments contain 5 data points 
y0=random[0:1020].reshape(204,5)

k0=np.fft.fftfreq(5,dx)
k0=np.fft.fftshift(k0)
k0=2*np.pi*k0

pdg2=np.zeros(1020).reshape(204,5)


for i in range(204):
    z=np.fft.fft(y0[i],norm="ortho")
    z=np.fft.fftshift(z)
    pdg2[i]=(abs(z)**2)
    
pdg2=sum(pdg2[:,])/204

plt.scatter(k0,pdg2) 
plt.title("power spectrum using Bartlet method" ,size=18)   
plt.xlabel("frequencies(k)") 
plt.ylabel("spectral density")
plt.show()



