# To fit the straight line y = a + bx 
# We have 2 equations ∑y = na + b∑x and ∑xy = a∑x + b∑x²
# Solving these 2 equations will give values for a and b (intercept and slope of best fit)

# Error Analysis 
# Our expected model is y = mx + c
# m and c parameters are extracted with or without some error in them as
#  m +- ∆m and c +- ∆c


# sig_y = sqrt(1/(N-2) ∑(yi - a - bx)^2)
# Delta = N ∑x^2 - (∑x)^2
# Standard deviation in slope = sig_y * sqrt(N/Delta)
# Standard deviation in intercept = sig_y * sqrt(∑x^2/Delta)

import numpy as np
from tabulate import tabulate 
from matplotlib import pyplot as plt

x_data = [3.80,8.26,15.31,19.31,21.39,26.52,36.27,40.79,43.01,62.79]
y_data = [0.109,0.231,0.409,0.472,0.566,0.700,0.941,1.315,1.441,2.073]

x = np.array(x_data)
y = np.array(y_data)
n = len(x)

if n != len(y):
    print("Data not complete!!")

x2 = np.square(x)
xy = np.array(x*y)

sigma_x = np.sum(x)
sigma_x2 = np.sum(x2)
sigma_y = np.sum(y)
sigma_xy = np.sum(xy)

# Solving the 2 linear equations as discussed 
# 1) ∑y = na + b∑x 
# 2) ∑xy = a∑x + b∑x²

# Using basic linear algebra 
# A . X = B 
# X = A^-1 . B 

A = np.array([[sigma_x,n],[sigma_x2,sigma_x]])
B = np.array([[sigma_y],[sigma_xy]])
X = np.linalg.inv(A).dot(B)

slope , intercept = X[0][0] , X[1][0]

delta = n*sigma_x2 - (sigma_x)**2
sig_y = (np.sum(np.square(y-x*slope-intercept))/(n-2))**0.5
# SD in slope and intercept 
sig_slope = sig_y * (n/delta)**0.5
sig_intercept = sig_y * (sigma_x2/delta)**0.5

table = np.array([x,y,x2,xy]).transpose()
print(tabulate(table,headers= ["Xi","Yi","Xi*Yi","Xi²"],tablefmt = "outline"))

print(f"\nThe Equation of the best fit is y = {slope}*x + {intercept}")

print(f'\n∑(x)  = {sigma_x}\n∑(y)  = {sigma_y}\n∑(xy) = {sigma_xy}\n∑(x²) = {sigma_x2}\n')
print(f'Slope = {slope}\nIntercept = {intercept}\n')
print(f'Error in Slope = {sig_slope}\nError in Intercept = {sig_intercept}\n')
print(f'σy = {sig_y}\n∆ = {delta}')
# Data plotting 
plt.title("Least Square Fit")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x ,y ,"o" , color = "red")
x = np.linspace(min(x),max(x),len(x))
y = slope*x + intercept
plt.plot(x,y,linestyle = "-",color = "green")
plt.grid()
plt.plot()
plt.show()