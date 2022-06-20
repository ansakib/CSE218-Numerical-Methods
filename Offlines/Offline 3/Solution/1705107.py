# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 20:33:49 2021

@author: ASUS
"""
import math

def trapezoidalRule(a,b,int_f,n):
    h = (b-a)/n
    area = int_f(a)
    for i in range (1, n):
        area = area + 2*(int_f(a+(i*h)))
    area = area + int_f(b)
    area = (h/2)*area
    return area
def simpson13Rule(a, b, fx0, fx1, fx2):
    area = (b-a)*(fx0+(4*fx1)+fx2)/6
    return area
    
    

u = 2000
q = 2100
m = 140000
g = 9.8
distance = lambda t: u*math.log((m/(m-q*t)))-g*t

t1 = 8
t2 = 30
sub_intvl = int(input("Enter the number of sub-intervals: "))
result_trap = trapezoidalRule(t1,t2,distance,sub_intvl)
print("Using Trapezoidal rule: ", result_trap)
re_approx_err = []
calculated = []
for i in range(1,6):
    calculated.append(trapezoidalRule(t1,t2,distance,i))
    re_approx_err.append(((abs(calculated[i-1]-calculated[i-2]))/calculated[i-1])*100)
for i in range(1,6):
    print("For n=",i,": Integrated Values=",calculated[i-1],",Relative Approx. Error=",re_approx_err[i-1],"%")
    

"""2nd Part"""

point_gap = (t2-t1)/(2*sub_intvl)
result_simpson = 0
current_time = t1
for i in range(sub_intvl):
    x0 = current_time
    x1 = x0+point_gap
    x2 = x1+point_gap
    fx0 = distance(x0)
    fx1 = distance(x1)
    fx2 = distance(x2)
    current_time = x2
    result_simpson = result_simpson + simpson13Rule(x0,x2,fx0, fx1, fx2)
    
print()
print("----------------------")
print()
print("Using Simposon 1/3 rule: ", result_simpson)

re_approx_err_simp = []
calculated_simp = []
for i in range(1,6):
    intvl = i;
    point_gap = (t2-t1)/(2*intvl)
    result_simpson = 0
    current_time = t1
    for j in range(intvl):
        x0 = current_time
        x1 = x0+point_gap
        x2 = x1+point_gap
        fx0 = distance(x0)
        fx1 = distance(x1)
        fx2 = distance(x2)
        current_time = x2
        result_simpson = result_simpson + simpson13Rule(x0,x2,fx0, fx1, fx2)
    calculated_simp.append(result_simpson)
    re_approx_err_simp.append(((abs(calculated_simp[i-1]-calculated_simp[i-2]))/calculated_simp[i-1])*100)
    
for i in range(1,6):
    print("For n=",i,": Integrated Values=",calculated_simp[i-1],",Relative Approx. Error=",re_approx_err_simp[i-1],"%")
    