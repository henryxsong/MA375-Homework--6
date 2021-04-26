# Henry Song  |  MA375  |  Spring 2021
# Homework #6: Topic 6 - Differential Equations
# File: Problem1.py
# Requirements: numpy, scipy, matplotlib
# Description: Calculates solutions to a differential equation using the 
#              Runge-Kutta method.
#==========================================================================

import numpy as np
import scipy as sp
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def dydt(t, y): return t**2 + y**2

diff_eq = lambda y, t : t**2 + y**2
solution = solve_ivp(diff_eq, t_span=[0, 2], y0=[1], max_step=0.01)
print("Solution @ t = %0.2f" % solution.t[80], ":", solution.y[0][81])
print("Solution @ t = %0.2f" % solution.t[90], ":", solution.y[0][91])
print("Solution @ t = %0.2f" % solution.t[95], ":", solution.y[0][96])
print("Solution @ t = %0.2f" % solution.t[101], ":", solution.y[0][101])

plt.title("Homework #6")
plt.plot(solution.t, solution.y[0], 'ro-')
plt.grid()
plt.show()