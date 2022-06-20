# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 10:18:12 2021

@author: ASUS
"""

import numpy as np
import matplotlib.pyplot as plt
import math


def GaussianElimination(a,b):
    n = np.shape(a)[0]
    mat_Solution = np.ndarray(shape=(n,1))
    for target_RC in range(n-1):
        
        max_idx = target_RC
        for idx in range(target_RC, n):
            if abs(a[idx][target_RC])>abs(a[target_RC][target_RC]):
                max_idx = idx
            
        if max_idx!=target_RC:
            a[[max_idx,target_RC]]=a[[target_RC,max_idx]]
            b[[max_idx,target_RC]]=b[[target_RC,max_idx]]
            
        
        for changing_row in range(target_RC+1, n):
            multi_fact = a[changing_row][target_RC]/a[target_RC][target_RC]
            for changing_col in range(target_RC, n):
                a[changing_row][changing_col] = a[changing_row][changing_col]-(multi_fact*a[target_RC][changing_col])
            
            b[changing_row][0] = b[changing_row][0] - multi_fact*b[target_RC][0]
            
                
    mat_Solution[n-1][0] = b[n-1][0]/a[n-1][n-1]
    for row in range(n-2, -1, -1):
        for col in range(row+1, n):
            b[row][0] = b[row][0]-a[row][col]*mat_Solution[col][0]
        
        mat_Solution[row][0] = b[row][0]/a[row][row]
        
    return mat_Solution


inFile=open("data.txt")
count=len(inFile.readlines())
inFile.close()

ci=np.zeros(count)
ki=np.zeros(count)
inFile=open("data.txt")


for i in range(count):
    line=inFile.readline().split()
    ci[i]=float(line[0])
    ki[i]=float(line[1])
    
plt.figure(figsize=(15,9))
plt.scatter(ci,ki,s=25, color='red')

yi = 1/ki
xi = 1/(ci*ci)


mat_A = np.ndarray(shape=(2,2))
mat_B = np.ndarray(shape=(2,1))

mat_A[0][0] = count
mat_A[0][1] = np.sum(xi)
mat_B[0][0] = np.sum(yi)

mat_A[1][0] = np.sum(xi)
mat_A[1][1] = np.sum(xi*xi)
mat_B[1][0] = np.sum(xi*yi)


soln = GaussianElimination(mat_A,mat_B)
a = soln[0][0]
b = soln[1][0]

kmax = 1/a
cs = kmax*b

print("kmax=",kmax,"; cs=",cs)

minimum_x = np.amin(ci)
maximum_x = np.amax(ci)
x_array = np.arange(minimum_x, maximum_x, 0.0001)
y_array = (kmax*x_array*x_array)/(cs+(x_array*x_array))
plt.plot(x_array, y_array)
plt.grid()
plt.xlabel("c")
plt.ylabel("k")