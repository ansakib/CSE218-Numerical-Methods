# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 11:00:41 2021

@author: ASUS
"""

import numpy as np
import matplotlib.pyplot as matplt
from sympy import *

def LagrangeInterpolation(x,y,targetX,order):
    result = 0
    for i in range(order+1):
        L_term = y[i]
        for j in range(order+1):
            if i!=j:
                L_term = L_term * ((targetX-x[j])/(x[i]-x[j]))
        result = result + L_term
    
    return result

v_28 = [25,27,30,31]
p_28 = [43,42,40,35]
targetVolume = 28
p_result_28 = [0]*3
for order in range(1,4):
    p_result_28[order-1] = LagrangeInterpolation(v_28, p_28, targetVolume, order)
print("Pressure at volume=",targetVolume,"is ",p_result_28[2])
print()

v_32 = [30,31,35,37]
p_32 = [40,35,30,25]
targetVolume = 32
p_result_32 = [0]*3
for order in range(1,4):
    p_result_32[order-1] = LagrangeInterpolation(v_32, p_32, targetVolume, order)
print("Pressure at volume=",targetVolume,"is ",p_result_32[2])
print()

print("Relative Approx Error for Volume = 28")
for i in range(2,4):
    err = (abs(p_result_28[i-1]-p_result_28[i-2])/p_result_28[i-1])*100
    print("For order",i,", error:", err,"%")
print()

print("Relative Approx Error for Volume = 32")
for i in range(2,4):
    err = (abs(p_result_32[i-1]-p_result_32[i-2])/p_result_32[i-1])*100
    print("For order",i,", error:", err,"%")
print()

"""Graph plot for Volume = 28"""

x = np.arange(10,40.005,0.005)
y = np.zeros(len(x))
for i in range(len(x)):
    y[i] = LagrangeInterpolation(v_28, p_28, x[i], 3)
matplt.figure(figsize=(16,8))
matplt.ylim(32,45)
matplt.xlim(25,31)
matplt.plot(x, y)
matplt.scatter(28, p_result_28[2], color='black', s=200)
matplt.grid()
matplt.xlabel("Volume")
matplt.ylabel("Pressure")
matplt.show()

"""Graph plot for Volume = 32"""

x = np.arange(10,40.005,0.005)
y = np.zeros(len(x))
for i in range(len(x)):
    y[i] = LagrangeInterpolation(v_32, p_32, x[i], 3)
matplt.figure(figsize=(16,8))
matplt.ylim(22,45)
matplt.xlim(30,37)
matplt.plot(x, y)
matplt.scatter(32, p_result_32[2], color='black', s=200)
matplt.grid()
matplt.xlabel("Volume")
matplt.ylabel("Pressure")
matplt.show()

"""Differentiation"""

v = [25,27,30,31,35]
p = [43,42,40,35,30]
x = Symbol('x')
p = LagrangeInterpolation(v, p, x, 4)
p_prime = integrate(p)
p_prime = lambdify(x, p_prime)
work = p_prime(35)-p_prime(25)
print("Work done: ",work)


