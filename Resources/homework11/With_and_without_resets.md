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
# fun. calculate
# n=0 means reset
# n=1 means without reset   
    def calculate(self, n = 0):
        for i in range(self.n):
            domg = (-(g / l) * math.sin(self.theta[-1]) - q * self.omg[-1] + self.FD * math.sin(OmgD * self.t[-1])) * self.dt
            self.omg.append(self.omg[-1] + domg)
            dtheta = self.omg[-1] * self.dt
            temp_theta = self.theta[-1] + dtheta
            if n == 0:
                if temp_theta < - math.pi:
                    self.theta.append(temp_theta + 2 * math.pi)
                elif temp_theta > math.pi:
                    self.theta.append(temp_theta - 2 * math.pi)
                else:
                    self.theta.append(temp_theta)
            if n == 1:
                self.theta.append(temp_theta)
            self.t.append(self.t[-1] + self.dt)
    def plot_theta(self, _ax, _color, _resets):
        _ax.plot(self.t, self.theta, '-', color = _color, label = r'$F_D = %.1f$' % self.FD + _resets)


# plot:
#       ax1: theta vs time

fig = plt.figure(figsize = (9.7, 6))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

comp = Nonlinear_Cromer(_FD = 1.2)
comp.calculate(0)
comp.plot_theta(ax1,'r',' with resets')

comp = Nonlinear_Cromer(_FD = 1.2)
comp.calculate(1)
comp.plot_theta(ax2,'b', ' without resets')
for i in fig.axes:
    i.legend(fontsize=12,loc='upper right')
    # i.set_title(r'$\theta vs time$',fontsize=14)
    i.set_xlabel(r'$time(s)$',fontsize=14)
    i.set_ylabel(r'$\theta (radians)$',fontsize=14)
ax1.set_title('with and without resets'+r'$(q=\frac{1}{2}, l=g=9.8, \Omega_D=\frac{2}{3})$',fontsize=18)
plt.show()
```