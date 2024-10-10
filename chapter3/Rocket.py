"""	Contains the RocketTrajectory class used for problems 2,3, and 4
		from section 3.2 of 'Optimal Control and Estimation' by Stengel.

"""

import numpy as np
from OCPUtil import *
import math
import matplotlib.pyplot as plt


# TODO LIST
# Write some bloody tests for this module!  It makes things easier!
#
# Make the RHS function more readable.  Breaking the assignments into functions might work.
# Make the Cost Function specification user-defined.  (Problem 4)
# Rewrite the equations of motion to handle a variable mass.  (Later)
# Rewrite the Thrust, Lift, and Drag equations so they're parametrized in a physical way.
#
#
# 

# CONSTANTS
g = 32				# ft/sec^2


# Sub-expression evaluators
def massFunc():
 return  20			# slugs

def thrustFunc():
	return 10**5			# lbf

def dragFunc():
	return 0				# lbf


def liftFunc():
	return 0				# lbf


def RHS(t, x, u):		
	""" Computes the right hand side of the differential equation.
		
		At the moment, the mass is remaining constant.

		Therefore:
			x is a state vector at a single instant
			t is the time at that instant
			u is the control scalar alpha at the present instant
	"""
	alpha = u
	
	f = np.zeros(len(x))
	# Wind-frame x direction
	f[0] = (1/(massFunc())) * (thrustFunc()*math.cos(alpha) - dragFunc() - g*math.sin(x[1]))
	# Wind-frame y direction
	f[1] = 1/(massFunc()*x[0]) * (thrustFunc()*math.sin(alpha)+liftFunc()-g*math.cos(x[1]))
	# ...? Can't remember.
	f[2] = x[0] * math.sin(x[1])
	return f

def getIC():
	"""  Set the initial conditions """
	v_0 = 100			# ft/s
	gamma_0 = np.pi/2	# rad
	h_0 = 0			# ft
	return np.array( [v_0, gamma_0, h_0])


# Note: This is becoming a god class.
# Get some tests in place.  Then break some stuff apart into separate classes.

class RocketTrajectory:
	""" Defines a model for a rocket's flight dynamics.
		
		Given a control history, the flight trajectory is then computed. 
		The objective function can then be computed for the trajectory.
	"""
	def __init__(self, t):
		self.time = t
		self.mdot = 0			# Slugs/sec
		nt = len(t)
		self.x = np.zeros((3,nt)) 
		self.x[:,0] = getIC()
		self.set_FinalConditions()

	def set_FinalConditions(self):
		v_d = 0					# ft/s  NOTE: Should be ignored based on Q
		gamma_d = np.pi/2			# rad
		h_d = 0					# ft	NOTE: Should be ignored based on Q
		
		self.x_d = np.array( [ v_d, gamma_d, h_d])

	def setAlpha(self, alpha):
		""" Input: a time history of the control variable alpha in degrees.		"""
		
		assert(len(alpha) == len(self.time)) 
		
		self.alpha = np.radians(alpha)


	def shoot(self):
		"""	Updates the values of the state vector for each instant in time.  Using an RK4
			integration scheme. 
		"""

		dt = self.time[1]-self.time[0]
		for i, timestep in enumerate(self.time):
			if self.x[0,i] == self.x[0,-1]:
				break
			self.x[:,i+1] = RK4( RHS, timestep, dt, self.x[:,i], self.alpha[i])
			# print(self.x[:,i])

	def getCost(self):
		"""  Computes and returns the cost of the trajectory.	"""
		
		Q = np.diag([0,1,0])
		r = 1
		diff = self.x_d - self.x[:,-0]

		J = np.dot( diff, np.dot( Q, diff))  + r * Quad( self.alpha**2, self.time)
		# print(J)
		return J

			
def plot( time, x):
    fig, ax = plt.subplots(3)
    
    ax[0].plot( time, x[0])
    ax[0].set_ylabel( 'velocity')
    ax[1].plot( time, x[1])
    ax[1].set_ylabel( 'flight path angle')
    ax[2].plot( time, x[2])
    ax[2].set_ylabel( 'Altitude')
    plt.tight_layout() 
    plt.show()
