# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 20:20:50 2021

@author: ASUS
"""

import numpy as np

def fourDec(item):
    return "%.4f" %item

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
        
        mat_Solution[row][0] = fourDec(b[row][0]/a[row][row])
        
    return mat_Solution
        
        
        
        
        
var_no = int(input("Enter No of unknown variables: "))
mat_A = np.ndarray(shape=(var_no,var_no))
mat_B = np.ndarray(shape=(var_no,1))

for i in range(var_no):
    mat_A[i] = np.array(input().split())
    
for i in range(var_no):
    mat_B[i][0] = float(input())
    
print()
solution_matrix = GaussianElimination(mat_A, mat_B)
print()
print("Solution Matrix:")
print(solution_matrix)