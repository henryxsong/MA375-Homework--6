# Henry Song  |  MA375  |  Spring 2021
# Homework #6: Topic 6 - Differential Equations
# File: Problem1.py
# Requirements: scipy, matplotlib
# Description: Calculates solutions to a differential equation using the 
#              Runge-Kutta method.
#==========================================================================

import scipy as sp
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# calculation functions
diff_eq = lambda y, t : t**2 + y**2 #differential equation
solution = solve_ivp(diff_eq, t_span=[0, 1.5], y0=[1], max_step=0.01) #calculates the solution for all t values from 0 to 1.5 in intervals of 0.01
specific_solution = solve_ivp(diff_eq, t_span=[0, 1.5], y0=[1], max_step=0.01, t_eval=[0.8, 0.9, 0.95, 1]) #calculates the solution for specified t values

# print functions for solutions
print("Solution @ t = %0.2f" % specific_solution.t[0], ":", specific_solution.y[0][0])
print("Solution @ t = %0.2f" % specific_solution.t[1], ":", specific_solution.y[0][1])
print("Solution @ t = %0.2f" % specific_solution.t[2], ":", specific_solution.y[0][2])
print("Solution @ t = %0.2f" % solution.t[154], ":", solution.y[0][154]) #closest value t value to 1 is located at largest index value 154

# plot functions
plt.title("Homework #6")
plt.plot(solution.t, solution.y[0], 'ro-')
plt.grid()
plt.show()