# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 22:02:02 2021

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
        


time = [19,22,26,28,30]
mass = [1203,1245,1378,1315,1475]
velocity = [3000,3500,4000,4500,5000]
targetX = 25

mass_result = [0]*4
for order in range(1,5):
    mass_result[order-1] = LagrangeInterpolation(time, mass, targetX, order)
print("mass at ",targetX,"sec is ",mass_result[3])
print()

vel_result = [0]*4
for order in range(1,5):
    vel_result[order-1] = LagrangeInterpolation(time, velocity, targetX, order)
print("vel at ",targetX,"sec is ",vel_result[3])
print()

print("Relative Approx Error for mass: ")
for i in range(2,5):
    err = (abs(mass_result[i-1]-mass_result[i-2])/mass_result[i-1])*100
    print("For order",i,", error:", err,"%")
print()    
    
print("Relative Approx Error for velocity: ")
for i in range(2,5):
    err = (abs(vel_result[i-1]-vel_result[i-2])/vel_result[i-1])*100
    print("For order",i,", error:", err,"%")
print()

"""Graph plot for Mass"""

x = np.arange(0,40.005,0.005)
y = np.zeros(len(x))
for i in range(len(x)):
    y[i] = LagrangeInterpolation(time, mass, x[i], 4)
matplt.figure(figsize=(16,8))
matplt.ylim(1000,1800)
matplt.xlim(19,30)
matplt.plot(x, y)
matplt.scatter(targetX, mass_result[3], color='black', s=200)
matplt.grid()
matplt.xlabel("time")
matplt.ylabel("mass")
matplt.show()

"""Graph plot for velocity"""

x = np.arange(0,40.005,0.005)
y = np.zeros(len(x))
for i in range(len(x)):
    y[i] = LagrangeInterpolation(time, velocity, x[i], 4)
matplt.figure(figsize=(16,8))
matplt.ylim(2500,5500)
matplt.xlim(19,30)
matplt.plot(x, y)
matplt.scatter(targetX, vel_result[3], color='black', s=200)
matplt.grid()
matplt.xlabel("time")
matplt.ylabel("velocity")
matplt.show()

"""Differentiation"""
t = Symbol('t')
m = LagrangeInterpolation(time, mass, t, 4)
v = LagrangeInterpolation(time, velocity, t, 4)
f = m*v
f_prime = f.diff(t)
f_prime = lambdify(t, f_prime)
print("Total applied force at t=25sec: ",f_prime(25))


'''
time = [10,15,20,22.5]
mass = [227.04, 362.78, 517.35, 602.97]

targetX = 16
order = 3
result = LagrangeInterpolation(time, mass, targetX, order)
print(result)
'''



