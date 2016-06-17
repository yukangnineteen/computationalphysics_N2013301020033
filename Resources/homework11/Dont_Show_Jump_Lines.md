```python
# -*- coding: utf-8 -*-
"""
@author: YUE Shaosheng
Last modified on Thu Apr 23 2016
"""

# basic packages needed
#     matplotlib - for plot 2D lines
#     numpy - for math 
import matplotlib.pyplot as plt
import numpy as np
import math

# global var.
g = 9.8
l = 9.8
q = 0.5
OmgD = 2. / 3.


# class Euler
# use Euler METHOD to solve the pendulum
# para. & var.  :    
#             theta0, omg0, t0 - initial angel & angular velocity & time
#             l, g, dt, time - length of string, gravity acceleration, time step size & total time 
#             the time period of this pendulum - 1(s)


class Nonlinear_Cromer(object):
    """docstring for Nonlinear_Cromer"""
    global g, l, q, OmgD
    def __init__(self, _FD = .0, _theta0 = 0.2, _omg0 = .0, _t0 = .0, _dt = 0.04, _time = 70.):
        self.FD = _FD
        self.theta = [_theta0]
        self.omg = [_omg0]
        self.t = [_t0]
        self.dt = _dt
        self.time = _time
        self.n = int(_time / _dt)
        self.THETA = []
        self.OMG = []
        self.T =[]
# fun. calculate
# n=0 means reset
# n=1 means without reset   
    def calculate(self):
        for i in range(self.n):
            domg = (-(g / l) * math.sin(self.theta[-1]) - q * self.omg[-1] + self.FD * math.sin(OmgD * self.t[-1])) * self.dt
            self.omg.append(self.omg[-1] + domg)
            dtheta = self.omg[-1] * self.dt
            temp_theta = self.theta[-1] + dtheta
            if temp_theta < - math.pi:
                self.theta.append(temp_theta + 2 * math.pi)
            elif temp_theta > math.pi:
                self.theta.append(temp_theta - 2 * math.pi)
            else:
                self.theta.append(temp_theta)
            self.t.append(self.t[-1] + self.dt)
        # print 'theta length:',len(self.theta)

# fun. plot
#  没有去除阶跃点之间的连线
    def plot_theta(self, _ax, _color, _resets):
        _ax.plot(self.t, self.theta, '-', color = _color, label = r'$F_D = %.1f$' % self.FD + _resets)

# fun. plot
#  去除了阶跃点之间的连线
    def plot_theta_improved(self, _ax, _color, _resets):
 

        l = []
        for i, j in enumerate(self.theta):
            if abs(j - self.theta[i-1]) > 6.:
                l.append(i)
            else:
                pass
        l = [i -1 for i in l]
        l = [-1] + l + [len(self.theta)]
        # print l,len(l)

        for i, j in enumerate(l):
            if i < (len(l) - 1):
                self.THETA.append(self.theta[j+1 : l[i + 1]])
                self.OMG.append(self.omg[j+1 : l[i + 1]])
                self.T.append(self.t[j+1 : l[i + 1]])
        # print len(self.THETA), len(self.OMG), len(self.T)
        _ax.plot(self.T[0], self.THETA[0], '-', color = _color, label = r'$F_D = %.1f$' % self.FD + _resets)
        for i in range(len(self.T)-1):
            _ax.plot(self.T[i+1], self.THETA[i+1], '-', color = _color)
            


# plot:
#       ax1: theta vs time

fig = plt.figure(figsize = (9.7, 6))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

comp = Nonlinear_Cromer(_FD = 1.2)
comp.calculate()
comp.plot_theta(ax1,'r',' with resets')

comp = Nonlinear_Cromer(_FD = 1.2)
comp.calculate()
comp.plot_theta_improved(ax2,'r',' with resets')


for i in fig.axes:
    i.legend(fontsize=12,loc='upper right')
    # i.set_title(r'$\theta vs time$',fontsize=14)
    i.set_xlabel(r'$time(s)$',fontsize=14)
    i.set_ylabel(r'$\theta (radians)$',fontsize=14)
ax1.set_title('Improved Plot'+r'$(q=\frac{1}{2}, l=g=9.8, \Omega_D=\frac{2}{3})$',fontsize=18)
plt.show()
        



```