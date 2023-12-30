#!/usr/bin/python
""" problem2.3-4.py

	Purpose:  This problem is about comparing the state transition matrix method of system
			  integration to integrating with a numerical procedure like RK4.

	Problem:  Compute state transition and control effect matrices, \Phi and \Gamma, for the
			  following differential equation, with \Delta t = 0.1 s:

			  F = [ -0.5, 1; 0, -0.7], G = [ 0, 1]'
			  where \dot{x} = F \vec{x} + G u.

			  Propagate the solution by 4th order Runge-Kutta and by the recursive use of
			  the state transfer function \Phi, with zero initial conditions and u = 1 for
			  t = 0 to 10 s.

"""

import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

from OCPUtil import *

def RHS( t, x, u):
	F = np.array([[-0.5, 1],[0,-0.7]])		# System dynamics
	G = np.array([0,1])						# Control effect matrix
	f = np.dot(F, x) + G * u

	# NOTE TO SELF: Avoid exlicitly shaping vectors if you don't need to.  Adding a 2x1 to a 
	# 1x2 in numpy evidently casts the result to a 2x2 array.  It's a giant pain in the ass to
	# debug if you get it wrong.  Ambiguous (2,) arrays don't have that problem.
	return f

def simulate_state_transition():
	#####  State transition method
	Phi = np.array([[0.95123, 0.0942],[0, 0.93239]])		# Approximate
	Gamma = np.array([0.0047714, 0.096586])             	# Approximate
	
	x_stm = np.zeros(( 2, nt))
	x_stm[:,0] = x_0[:,0]
	
	i=0
	for timestep in t:
		if timestep == t[-1]:
			break
		x_stm[:,i+1] = np.dot( Phi, x_stm[:,i]) + Gamma * u[i]
		i = i + 1

	return x_stm


def simulate_RK4():
	# Initial condtion
	x_RK4 = np.zeros(( 2, nt))
	x_RK4[ :, 0] = x_0[ :, 0]
	
	i = 0
	for timestep in t:
	
		# Stop before the end	
		if timestep == t[-1]:
			break
		
		x_RK4[:, i+1] = RK4( RHS, timestep, dt, x_RK4[:, i], u[i])
		i = i + 1
	return x_RK4

def generate_plots( x_RK4):
	# Plot State Transition solution
	plt.subplot(3, 2, 1)
	plt.plot( t, x_stm[0,:], label='x1')
	plt.plot( t, x_stm[1,:], label='x2')
	plt.legend()
	plt.title('Evolution by State Transition')
	plt.grid(True)
	
	# Plot RK4
	plt.subplot(3, 2, 2)
	plt.plot( t, x_RK4[0,:], label='x1')
	plt.plot( t, x_RK4[1,:], label='x2')
	plt.legend()
	plt.title('Evolution by 4th order Runge Kutta')
	plt.grid(True)
	
	# Overlay plots
	
	plt.subplot(3,2,3)
	plt.plot( t, x_stm[0,:], label='State Transition')
	plt.plot( t, x_RK4[0,:], label='4th Order Runge Kutta')
	plt.legend()
	plt.title('X1 Overlay')
	plt.grid(True)
	
	
	plt.subplot(3,2,4)
	plt.plot( t, x_stm[1,:], label='State Transition')
	plt.plot( t, x_RK4[1,:], label='4th Order Runge Kutta')
	plt.legend()
	plt.title('X2 Overlay')
	plt.grid(True)
	
	#  Error Plots
	err1 = x_RK4[0,:] - x_stm[0,:]
	err2 = x_RK4[1,:] - x_stm[1,:]
	
	plt.subplot(3,2,5)
	plt.plot( t, err1, label='x1')
	plt.plot( t, err2, label='x2')
	plt.legend()
	plt.title('Absolute Error')
	plt.grid(True)

	plt.show()



if __name__ == "__main__":

	##### Time discretization
	dt = 0.1
	t = np.arange(0,20,dt)
	nt = len(t)
	
	
	x_0 = np.zeros((2,1))					# Initial conditions
	
	##### Control history
	u = np.zeros(t.shape)
	
	i=0
	for timestep in t:
		if timestep < 10:
			u[i] = 1
		i = i + 1
	
	
	x_stm = simulate_state_transition()
	x_RK4 = simulate_RK4()

generate_plots( x_RK4)
