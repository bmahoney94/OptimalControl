"""  This is my own personal collection of utilities and functions.  Hopefully I'll get better
	 at reusing code if I commit to maintaining this at least.  As the collection grows, 
	 bits of code with similar functionality will be broken out into separate modules.

	 Tests are located in util_tests.py.

"""

import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
from pprint import pprint


# THIS FUNCTION HAS TOO MANY ARGUMENTS!
def RK4(RHS, t, delta_t, x, u):
	""" RK4( RHS, time, delta_t, x1, u)
		
		RHS(t, x, u): Function that returns a column vector
		t: scalar time input
		delta_t: Scalar time step length
		x: Column vector of present state
		u: column vector of present control state
		
		Implements a 4th order Runge-Kutta integration scheme to propagate the state from
		time = t1 to time = t2.
		
		The control state is held constant throughout the interval(zoh).
	"""	
	k1 = delta_t * RHS( t, x, u)
	k2 = delta_t * RHS( t + delta_t/2, x + k1/2, u)
	k3 = delta_t * RHS( t + delta_t/2, x + k2/2, u)
	k4 = delta_t * RHS( t + delta_t, x + k3, u)
	
	result = x + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
	return result


	
def Quad( f, t):
	"""  Computes the definite integral of 'f' over 't' using a trapezoid rule.
		
		 'f' and 't' are precomputed numpy arrays.
	"""
	A = 0
	for i in range(1, len(f)):
		A = A + (f[i] + f[i-1])/2 * (t[i] - t[i-1])
	
	return A



def gradient_descent( F, x):
	""" Computes the minimum of the function 'F' and returns its value and location
		given an initial guess at the location of the min.

	"""
	
	epsilon = 0.5		# Arbitrary atm. Try to compute it somehow! 
	x_list = [x]

	
	for index in range(0,100):
		grad = gradient( F, x)
		
	
		# Function of epsilon.  To be passed to newton1D.	
		G =	lambda eps: F( x - eps * gradient( F, x) )

		print('blah:' + str( G( 0)) )
	

		x = x - epsilon * grad   
		x_list.append(x)
		
		if isConverged( x_list[-2], x_list[-1]):
			break

		elif index == 99:
			#TODO: Find a way to make this raise an exception.  Need an abort on failure.
			print('Gradient descent failed to converge in 100 steps')

	return F( x), x	

#TODO:  Consider breaking this function out on its own.
def get_dxx( F, x):
		
	h_list = [ (0.5)**n for n in range(0,10) ] 

	result_list = []
	for h in h_list:
		result = (deriv1D( F, x + h) - deriv1D( F, x)) / h
		
		result_list.append(result)

		if h < 0.5 and isConverged( result_list[-2], result_list[-1]):
			break

	return result		

def newton1D( F, x):
	"""  Given a function F and an initial guess x, this function will find the
			local optima of the function.

		 This is a Newton-Raphson optimization procedure, not a root finder!
	"""
	
		
	
	x_list = [x]
	for iteration in range( 0, 10):	
		x = x - deriv1D( F, x) / get_dxx( F, x)	
		
		x_list.append(x)

		if isConverged( x_list[-2], x_list[-1]):
			break

	return x, F(x)

def deriv1D( F, x):
	#	h = 0.01
	
	h_list = [ (0.5)**n for n in range(1,10)]
	
	deriv_list = []
	
	for h in h_list:
		deriv = ( F( x + h) - F(x))  
		deriv = deriv/ h
		
		deriv_list.append(deriv)
	
		if h < 0.5:	
			if isConverged( deriv_list[-2], deriv_list[-1]):
				break
	
	return deriv



#TODO:  Try to make this function 'do one thing'.  
def gradient( F, x):
	""" Computes the gradient of a scalar function F at a point x. 
	
		The function computes the slope of secant lines and successively refines the stepsize
		until the gradient values converage to within some tolerance.
	"""
	x = np.array(x)
	
	grad_estimate_list = []
	stepsize = 1
	
	# Refine the gradient to force it to converge
	for index in range(1,1000):
		stepsize = 0.1**index
		# print('Increment: ', stepsize)

		grad = np.zeros(x.shape)
		
		# Computes the gradient for a given resolution
		for i, element in enumerate(grad):
			delta = np.zeros(x.shape)
			delta[i] = stepsize
			
			grad[i] = (F( x + delta) - F(x)) / stepsize
	
		
		if len(grad_estimate_list) > 1:
			if isConverged( grad_estimate_list[-1], grad):
				break

					
		grad_estimate_list.append(grad)	
	
	return grad





def isConverged( current, previous):
	""" Returns a boolean value to determine if two vectors(successive estimates, typically)
		are within a specified tolerance of one another.  This helps clarify the logic in 
		calling functions a bit.
	"""
	tolerance = 0.001
	
	deviation = current - previous
	
	return np.linalg.norm( deviation) < tolerance
	

##  IF: main ##

if  __name__ == '__main__':
	print('This is a library.  Run tests from the util_test.py file.')

