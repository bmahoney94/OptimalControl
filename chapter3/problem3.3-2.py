#!/usr/bin/python3
""" Section 3.3: Problem 2
	
	This is a parametric trajectory optimization problem for a 
	rocket with given dynamics:

		v_dot = 1/m * (T cos(alpha) - D - g sin(gamma)
		gamma_dot = 1/(mv) * (T sin(alpha) + L - g cos(gamma))
		h_dot = v * sin(gamma)
		m_dot = f(T)

	The cost function is:
		J = 1/2 ( (x_d - x_f)' Q (x_d - x_f) + r \integ_0^{tf} alpha(t)^2 dt

	Initially, a control history of 
		
		alpha = alpha_vec0 + alpha_vec1 * t 
	
	is assumed.

"""

import numpy as np
import matplotlib.pyplot as plt
from OCPUtil import *
from Rocket import *

def alphaFunc( alpha0, alpha1):
	return alpha0 + alpha1 * t

def objFunc( alpha_vec):
	rocketTrajectory.setAlpha( alphaFunc( alpha_vec[0], alpha_vec[1]) )
	rocketTrajectory.shoot()
	cost = rocketTrajectory.getCost()
	return cost



if __name__ == "__main__":

	tf = 10				# seconds
	dt = 0.1			# seconds
	t = np.arange(0, tf, dt)
	
	# Trajectory Optimization using Gradient Descent 
	alpha0, alpha1 = 0.5, -0.5
	alpha_vec = alpha0, alpha1
	
	rocketTrajectory = RocketTrajectory( t)
	cost = objFunc( alpha_vec)
	
	cost, location = gradient_descent( objFunc, alpha_vec)
	
	print('Final Cost: ', cost)
	print('Parameters: ', location)
	
	plot( t, rocketTrajectory.x)




