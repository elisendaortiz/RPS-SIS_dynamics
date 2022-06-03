import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np
from numpy import pi, sin
import sympy as sympy
from sympy import *
import sys, traceback
import operator


#----Mathematica colors ----
m_blue='#5E81B5'
m_green='#8FB131'
m_mustard='#E19C24'
m_tile='#EC6235'
l_grey='#CCCCC6'
# --------------------------


def system_equations(delta, lamb):
	k=10 #Degree of k-regular network
	U = -k*X**2 -2*k*X*Y +X*(-delta+k) # dx/dt
	V = +k*lamb*Y**2 -k*lamb*Y +k*X*Y*(lamb+1) # dy/dt
    	return U,V

fig = plt.figure()
ax = fig.add_subplot(111)

# Adjust the subplots region to leave some space for the sliders and buttons
fig.subplots_adjust(left=0.25, bottom=0.25)

#Parameters to draw initial plot
w = 1.0
Y, X = np.mgrid[0:w:100j, 0:w:100j]
delta_0=0
lamb_0=0

# Draw the initial plot
stream = ax.streamplot(X, Y, system_equations(delta_0,lamb_0)[0],system_equations(delta_0,lamb_0)[1], color=m_blue, density=[1., 1.])
ax.set_xlabel('rho_1')#Papers
ax.set_ylabel('rho_2')#Scissors
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])

# Define an axes area and draw a slider in it
delta_slider_ax  = fig.add_axes([0.25, 0.1, 0.65, 0.03])
delta_slider = Slider(delta_slider_ax, 'delta', 0., 10.0, valinit=delta_0)

# Draw another slider
lamb_slider_ax = fig.add_axes([0.25, 0.05, 0.65, 0.03])#
lamb_slider = Slider(lamb_slider_ax, 'lambda', 0., 10.0, valinit=lamb_0)

# Add a button for resetting the parameters
reset_button_ax = fig.add_axes([0.8, 0.9, 0.1, 0.04])
reset_button = Button(reset_button_ax, 'Reset', color='white', hovercolor=l_grey)
def reset_button_on_clicked(mouse_event):
    delta_slider.reset()
    lamb_slider.reset()
reset_button.on_clicked(reset_button_on_clicked)

# Define an action for modifying the streamplot (actually redrawing) when any slider's value changes
def sliders_on_changed(val):#val es el valor de l'slider (el de delta es= delta_slider.val, el de lambda es lamb_slider.val
	#system_equations(delta_slider.val,lamb_slider.val) #Em retorna U,V evaluats als valors dels sliders
	global stream
	stream.lines.remove()
	ax.patches = []
	stream= ax.streamplot(X, Y, system_equations(delta_slider.val,lamb_slider.val)[0],system_equations(delta_slider.val,lamb_slider.val)[1], color=m_blue, density=[1., 1.])
	ax.set_xlabel('rho_1')
	ax.set_ylabel('rho_2')
	ax.set_xlim([0, 1])
	ax.set_ylim([0, 1])
	return

delta_slider.on_changed(sliders_on_changed)#AQUI DINS HAS DE CRIDAR LA FUNCIO Q VULGUIS Q S'IMPLEMENTI (=redraw streamplot) QUAN VARIES UN SLIDER
lamb_slider.on_changed(sliders_on_changed)

plt.show()



