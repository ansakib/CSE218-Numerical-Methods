# -*- coding: utf-8 -*-
"""
Created on Sun May 30 09:58:18 2021

@author: ASUS
"""

import numpy as np

def detMatrix(a):
    n = np.shape(a)[0]
    rowswaps = 0
    
    for target_RC in range(n-1):
        
        max_idx = target_RC
        for idx in range(target_RC, n):
            if abs(a[idx][target_RC])>abs(a[target_RC][target_RC]):
                max_idx = idx
            
        if max_idx!=target_RC:
            rowswaps = rowswaps + 1
            a[[max_idx,target_RC]]=a[[target_RC,max_idx]]
            
            
        for changing_row in range(target_RC+1, n):
            multi_fact = a[changing_row][target_RC]/a[target_RC][target_RC]
            for changing_col in range(target_RC, n):
                a[changing_row][changing_col] = a[changing_row][changing_col]-(multi_fact*a[target_RC][changing_col])
            
    det = 1
    for i in range(n):
        det = det * a[i][i]
        
    det = det* (-1)**rowswaps
    return det
    
    
    
var_no = int(input("Enter No of unknown variables: "))
mat_A = np.ndarray(shape=(var_no,var_no))

for i in range(var_no):
    mat_A[i] = np.array(input().split())
    
detValue = detMatrix(mat_A)
print(detValue)