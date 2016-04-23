```python
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 11:32:49 2016

@author: sheng

Last modified on Thu Apr 21 2016
"""
# basic packages needed
#     matplotlib - for plot 2D lines
#     numpy - for math 
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib import animation

theta0 = 0.1
omg0 = 0
g = 9.8
length = g / (4 * (np.pi) ** 2)
T = []
THETA = []
# class Cromer
# use Euler-Cromer METHOD to solve the pendulum
# para. & var.  :    
#             theta0, omg0, t0 - initial angel & angular velocity & time
#             l, g, dt, time - length of string, gravity acceleration, time step size & total time 
#             the time period of this pendulum - 1(s)        
 
class Cromer(object):
    global theta0, omg0, g, length
    def __init__(self, _dt = 0.01, _time = 5.):
        self.theta, self.omg, self.t = [theta0], [omg0], [0.]
        self.l, self.g, self.dt, self.time, self.n= length, g, _dt, _time, int(_time/_dt)
        self.E = [0.5*((self.l*omg0)**2+self.g*self.l*(theta0)**2)]
    def calculate(self):
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)
            self.omg.append(self.omg[-1]-self.g/self.l*self.theta[-1]*self.dt)
            self.theta.append(self.theta[-1]+self.omg[-1]*self.dt)
            self.E.append(0.5*((self.l*self.omg[-1])**2+self.g*self.l*(self.theta[-1])**2))
        T.append(self.t)
        THETA.append(self.theta)
    def plot_theta(self,_ax):
        _ax.plot(self.t, self.theta, '-',label='Euler-Cromer Method')

    # def animate_theta(self):
    #     for i in range(len(np.arange(0, 0.2, 0.02))):
    #         theta0 = np.arange(0, 0.2, 0.02)[i]
    #         calculate()
    #         T.append(self.t)
    #         THETA.append(self.theta)

    def find_period(self):
        tperiod = []
        for i in range(self.n):
            if abs(self.theta[i] - theta0) < 0.0000001 and self.t[i] > 10 * self.dt:
                tperiod.append(self.t[i])
            else:
                pass
        s = 0
        print tperiod
        # for i in range(3):
        #     s = s + tperiod[i]
        #     print "period: %f" % (s / 3)
        # return s / 3


    

# plot :
#        ax1 - time dependence of angel
#        ax2 - time dependence of energy
# both Euler & Euler Cromer METHOD & Second-order Runge-Kutta METHOD are used
fig= plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(121,xlim=(0, 5),ylim=(-0.6, 0.6))
ax1.set_xlabel('time'+r'$ /\tau $',fontsize=14)
ax1.set_ylabel('Angel (radian)',fontsize=14)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.text(6,0.2,r'For simple pendulum, the period is independent'+ '\n'+'of amplitude.' + '\n' +'Period:'+ r'$ \tau = 1s$'+ '\n')

ax1.set_title('Amplitude Animation of Simple Pendulum')
ax1.grid()
line, = ax1.plot([], [], '-', label='Euler-Cromer Method')
angle_text = ax1.text(0.3,0.43, '' )
ax1.legend(fontsize=12,loc='upper left', frameon=True)
def init():
    """initialize animation"""
    line.set_data([], [])
    angle_text.set_text('')
    return line, angle_text

def animate(i):
    """perform animation step"""
    global theta0
    theta0 = np.arange(0.02, 0.2, 0.02)[i]
    comp = Cromer()
    comp.calculate()
    line.set_data(T[i], THETA[i])
    angle_text.set_text('Amplitude is %.2f' % theta0 + r'$rad$')
    return line, angle_text
ani = animation.FuncAnimation(fig, animate, frames=len(np.arange(0.02, 0.2, 0.02)),
                              interval=300, blit=True, init_func=init)

ani.save('basic_animation.mp4', fps=3, extra_args=['-vcodec', 'libx264'])
plt.show(fig)
```