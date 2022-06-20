# -*- coding: utf-8 -*-
"""
Created on Sat May 29 21:29:48 2021

@author: ASUS
"""



def newtonRaphsonMethod(f, df, x_init, re_approx_err, max_iteration):
    counted_iter = 1
    error = 100
    x_old = x_init
    x_new = x_init
    
    while re_approx_err<error and counted_iter<=max_iteration :
        print("iter=",counted_iter,",x=",x_new,",error=", error)
        if f(x_old)==0:
            error = 0
        else:
            x_new = x_old - (f(x_old)/df(x_old))
            error = abs((x_new-x_old)/x_new)*100
            counted_iter = counted_iter + 1
            x_old = x_new
            
    return x_new

        
        
        
        
func = lambda x: (x**3)-0.165*x*x+3.993e-4
dfunc = lambda x: (3*x*x)-2*.165*x

root = newtonRaphsonMethod(func, dfunc, 0.05, 0, 50)
print("root =",root)