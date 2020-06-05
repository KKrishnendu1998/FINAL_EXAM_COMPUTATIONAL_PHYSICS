#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 9:
Created on Fri Jun  5 08:30:41 2020

@author: krishnendu
"""

#
#In this method  A real matrix of dimention(m,n) is decomposed through A=U*S*V^T , where the S is a real Diaginal matrix of dimention(m,n) and U, V are real othogonal matrics of dimention (m,m) and (n,n) respectivly
import numpy as np

A=np.array([[2,1],[1,0],[0,1]])# the given matrix

U1,S1,V1=np.linalg.svd(A)       # U1,V1,S1 are the singular value decomposed  matrics using function numpy.linalg.svd


print('Singular valuesof the first matrix using the function numpy.linalg.svd is : \n',S1)


A2=np.array([[1,1,0],[1,0,1],[0,1,1]])

U2,S2,V2=np.linalg.svd(A2)       # U1,V1,S1 are the singular value decomposed  matrics using function numpy.linalg.svd


print('Singular values of the second matrix using the function numpy.linalg.svd is : \n',S2)

A3=np.array([[4,1,2],[2,4,-1],[1,1,-3]])

