```python
# -*- coding: utf-8 -*-
"""
@author: YUE Shaosheng
Last modified on Thu Apr 24 2016
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
    def __init__(self, _FD = .0, _theta0 = 0.2, _omg0 = .0, _t0 = .0, _dt = 0.04, _time = 10000.):
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


# fun. plotplot_phase_space
#  去除了阶跃点之间的连线的相空间图
    def plot_phase_space(self, _ax, _color, _accur):
        t = np.array([i * OmgD / np.pi / 2 for i in self.t])
        tempt = np.array([round(i) for i in t])
        tempt2 = t - tempt
        a = []
        for i, j in enumerate(tempt2):
            if abs(j) < _accur:
                a.append(i)
        self.THETA = [self.theta[i] for i in a]
        self.OMG = [self.omg[i] for i in a]
        print t, tempt, tempt2,a
        # print a


        _ax.plot(self.THETA, self.OMG, 'o',markersize = 3.2, color = _color,label = r'$F_D = %.1f,\phi = 0$' % self.FD)
        # for i in range(len(self.T)-1):
        #     _ax.plot(self.THETA[i+1], self.OMG[i+1], '-', color = _color)
            


# plot:
#       ax1: theta vs time

fig = plt.figure(figsize = (16., 5))
ax2 = fig.add_subplot(122, xlim = (2.0,4.), ylim = (-1.5, 0.))
ax1 = fig.add_subplot(121, xlim = (-4, 4), ylim = (-2, 1))


comp = Nonlinear_Cromer(_FD = 1.2)
comp.calculate()
comp.plot_phase_space(ax1,'r', 1e-3)

comp = Nonlinear_Cromer(_FD = 1.2)
comp.calculate()
comp.plot_phase_space(ax2,'r', 1e-3)

for i in fig.axes:
    i.legend(fontsize=12,loc='upper right')
    # i.set_title(r'$\theta vs time$',fontsize=14)
    i.set_xlabel(r'$\theta (radians)$',fontsize=14)
    i.set_ylabel(r'$\omega (radians/s)$',fontsize=14)
    i.set_title(r'$Poincare Section$'+r'$(q=\frac{1}{2}, l=g=9.8, \Omega_D=\frac{2}{3})$',fontsize=18)
# ax1.text(0.5,0.85,r'$Poincare Section$'+r'$(q=\frac{1}{2}, l=g=9.8, \Omega_D=\frac{2}{3})$',fontsize=18)
plt.show()
```