# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 12:10:46 2021

@author: ASUS
"""

import numpy as np
import matplotlib.pyplot as matplt
from tabulate import tabulate
import math

def bisection_table(x_low, x_up, re_approx_err):
    table_data = np.zeros(shape = (20, 5))
    k = 0.05
    Pt = 3
    #function = lambda x : ((x/(1-x))*np.sqrt((2*Pt)/(2+x))) - k
    function = lambda x : x**3-0.165*x*x+3.993e-4
    count_iter = 1
    error = 100
    xm = 0
    xm_old = 0
    
    while re_approx_err<error and count_iter<=20:
        xm = (x_low + x_up)/2
        table_data[count_iter-1][0] = count_iter
        table_data[count_iter-1][1] = x_low
        table_data[count_iter-1][2] = x_up
        table_data[count_iter-1][3] = xm
        root_checker = function(x_low)*function(xm)  
        if root_checker<0:
            x_up = xm
        elif root_checker>0:
            x_low = xm
        else:
            error = 0
        
        if xm!=0:
            error = abs((xm-xm_old)/xm) * 100
        xm_old = xm
        table_data[count_iter-1][4] = error
        count_iter = count_iter + 1
    
    table_data[0][4] = math.nan
    table_data = np.delete(table_data, slice(count_iter-1, 21, 1), 0)
    table_header = ["Iteration", "x_low", "x_up", "Root", "Relative Approx. Error(%)"]
    print(tabulate(table_data, headers=table_header, tablefmt="fancy_grid", numalign="left"))
        
    


def bisection_method(x_low, x_up, re_approx_err, max_iter):
    k = 0.05
    Pt = 3
    #function = lambda x : ((x/(1-x))*np.sqrt((2*Pt)/(2+x))) - k
    function = lambda x : x**3-0.165*x*x+3.993e-4
    count_iter = 1
    error = 100
    xm = 0
    xm_old = 0
    
    while re_approx_err<error and count_iter<=max_iter:
        xm = (x_low + x_up)/2
        root_checker = function(x_low)*function(xm)  
        if root_checker<0:
            x_up = xm
        elif root_checker>0:
            x_low = xm
        else:
            error = 0
        
        count_iter = count_iter + 1
        if xm!=0:
            error = abs((xm-xm_old)/xm) * 100
        xm_old = xm
        
    return xm



k = 0.05
Pt = 3

x = np.arange(-0.6, 0.5, 0.0001)
y = ((x/(1-x))*np.sqrt((2*Pt)/(2+x))) - k
matplt.figure(figsize=(16,8))
matplt.plot(x, y)
matplt.grid()
matplt.xlabel("x")
matplt.ylabel("f(x)")

#drawing x axis
y2 = np.zeros(len(x))
matplt.plot(x, y2)
matplt.show()



print()
lower_bound = float(input("Enter lower bound of the bracket: "))
upper_bound = float(input("Enter upper bound of the bracket: "))
max_iteration = int(input("Enter the number of maximum iteration: "))
expected_relative_approx_error = 0.1

result = bisection_method(lower_bound, upper_bound, expected_relative_approx_error, max_iteration)
print()
print("The estimated value of x: ", result)

print()
print()
bisection_table(lower_bound, upper_bound, expected_relative_approx_error)

