# -*- coding: utf-8 -*-
"""
Created on Sat May 29 20:25:19 2021

@author: ASUS
"""

function = lambda x: (x**3)-0.165*x*x+3.993e-4

def SecantMethod(x_low, x_up, re_approx_err, max_iter):
    count_iter = 1
    error = 100
    xm = 0
    xm_old = 0
    
    while re_approx_err<error and count_iter<=max_iter:
        xm = x_up - ((function(x_up)*(x_low-x_up))/(function(x_low)-function(x_up)))
        
        if function(xm)==0:
            error = 0
        else:
            x_low = x_up
            x_up = xm
            count_iter = count_iter + 1
            if xm!=0:
                error = abs((xm-xm_old)/xm) * 100
            xm_old = xm
        
    return xm


result = SecantMethod(0.01, 0.1, 0, 50)
print(result)