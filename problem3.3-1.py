""" Problem 1, sections 3.3
	
	We're tasked with solving the parametric optimization problem from example 3.3-1c
	with a different final desired value of '10' rather than '0'.

	The problem consists of a cart on a track moving from x=0 to x=100 using a parametric
	control history.  We want to minimize both the errors in the final state (location and
	velocity), while also minimizing the time required to complete the task.

	The intent of the exercise is to demonstrate parametric trajectory optimization AND to 
	show how one would trade penalties among different objectives.


"""

import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt


def A( q):
	a = np.zeros((2,2))
	a[0,0] = 5*10**3 * q[0] + 2*10**2 * q[1] + 20 * q[2]
	a[1,0] = (5*10**4)/3 * q[0] + 5*10**3 * q[1] + (10**3)/6 * q[2]

	a[0,1] = (5*10**4)/3 * q[0] + 10**3 * q[1] + 50 * q[2]
	a[1,1] = (5*10**4)/3 * q[0] + 5*10**3 * q[1] + (10**3)/6 * q[2]
	return a

B = np.array([ [ 10**3, 2*10**2, 0], [ (10**5)/3, 10**3, 0]])
t = np.arange(0,10,0.1)
nt = len(t)

def x1( k, t):
	"""Position function"""
	return k[0] *(t**2)/2 + k[1] * (t**3)/6

def x2( k, t):
	"""Velocity function"""
	return k[0] * t + k[1] * (t**2)/2



q_list = [ (1, 1, 0) ]
  
for q in q_list:
	a = A(q)
	k = np.dot( linalg.inv( a), np.dot( B, q))
	print('q: ' + str(q))
	print('k: ' + str(k))
	print 
	plt.plot( t, x1( k, t))

plt.show()

##  Plots don't look right.  Something's been calculated wrong.
