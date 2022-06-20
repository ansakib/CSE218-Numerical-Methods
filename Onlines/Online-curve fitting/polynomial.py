# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:42:27 2021

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


inFile=open("data2.txt")
count=len(inFile.readlines())
inFile.close()

xi=np.zeros(count)
yi=np.zeros(count)
inFile=open("data2.txt")


for i in range(count):
    line=inFile.readline().split()
    xi[i]=float(line[0])
    yi[i]=float(line[1])
    
plt.figure(figsize=(15,9))
plt.scatter(xi,yi,s=10)

ti = np.sum(xi)
ti2 = np.sum(xi**2)
ti3 = np.sum(xi**3)
ti4 = np.sum(xi**4)


mat_A = np.ndarray(shape=(3,3))
mat_B = np.ndarray(shape=(3,1))

mat_A[0][0] = count
mat_A[0][1] = ti
mat_A[0][2] = ti2
mat_B[0][0] = np.sum(yi)

mat_A[1][0] = ti
mat_A[1][1] = ti2
mat_A[1][2] = ti3
mat_B[1][0] = np.sum(yi*xi)

mat_A[2][0] = ti2
mat_A[2][1] = ti3
mat_A[2][2] = ti4
mat_B[2][0] = np.sum(yi*(xi*xi))

print(mat_A)
print(mat_B)

soln = GaussianElimination(mat_A,mat_B)
a = soln[0][0]
b = soln[1][0]
c = soln[2][0]

print("a=",a,"; b=",b, "; c=",c)

#function = lambda x: (a*x) + (b*math.exp(x))
minimum_x = np.amin(xi)
maximum_x = np.amax(xi)
x_array = np.arange(minimum_x, maximum_x, 0.0001)

y_array = (c*(x_array*x_array))+(b*x_array)+a
plt.plot(x_array, y_array)
plt.ylim(-0.00001,0.00001)
plt.grid()
plt.xlabel("x")
plt.ylabel("y")

    