# -*- coding: utf-8 -*-
"""
Created on Sat May 29 20:44:33 2021

@author: ASUS
"""

import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 1, 0.0001)
y = (x**3)-9*x*x+3.8197


plt.figure(figsize=(16,8))
plt.plot(x,y)
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")


