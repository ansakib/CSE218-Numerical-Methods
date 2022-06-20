# -*- coding: utf-8 -*-
"""
Created on Sat May 29 20:25:19 2021

@author: ASUS
"""

function = lambda x: (x**3)-9*x*x+3.8197

def FalsePositionMethod(x_low, x_up, re_approx_err, max_iter):
    count_iter = 1
    error = 100
    xm = 0
    xm_old = 0
    
    while re_approx_err<error and count_iter<=max_iter:
        xm = x_up - ((function(x_up)*(x_low-x_up))/(function(x_low)-function(x_up)))
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


result = FalsePositionMethod(0.5, 0.8, 0, 50)
print(result)