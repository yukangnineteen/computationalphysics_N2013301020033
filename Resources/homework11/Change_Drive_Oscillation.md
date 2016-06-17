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
from matplotlib import animation


# global var.
g = 9.8
l = 9.8
q = 0.5
OmgD = 2. / 3.
FD = .0
THETA = []
T = []

# class Euler
# use Euler METHOD to solve the pendulum
# para. & var.  :    
#             theta0, omg0, t0 - initial angel & angular velocity & time
#             l, g, dt, time - length of string, gravity acceleration, time step size & total time 
#             the time period of this pendulum - 1(s)


class Nonlinear_Cromer(object):
    """docstring for Nonlinear_Cromer"""
    global g, l, q, OmgD, FD,T
    def __init__(self,  _theta0 = 0.2, _omg0 = .0, _t0 = .0, _dt = 0.04, _time = 3000.):
        self.FD = FD
        self.theta = [_theta0]
        self.omg = [_omg0]
        self.t = [_t0]
        self.dt = _dt
        self.time = _time
        self.n = int(_time / _dt)
    
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
            # self.theta.append(temp_theta)
            self.t.append(self.t[-1] + self.dt)
    def plot_theta(self ):
        THETA.append(self.theta)
        T.append(self.t)
        # _ax.plot(self.t, self.theta, '-', color = _color, label = r'$F_D = %.1f$' % self.FD)

# PREPARE x.axis&y.axis data
s = np.arange(1.2, 1.45, 0.005)
for i in s:
    FD = i
    comp = Nonlinear_Cromer()
    comp.calculate()
    comp.plot_theta()
print len(s),len(T), len(THETA)

# plot:
#       ax1: theta vs time

fig = plt.figure(figsize = (14,5))
ax1 = fig.add_subplot(111,xlim=(2800,3000),ylim=(-4,4))
ax1.set_xlabel(r'$time(s)$',fontsize=14)
ax1.set_ylabel(r'$\theta (radians)$',fontsize=14)
ax1.set_title(r'$Nonlinear_Pendulum$'+r'$(q=\frac{1}{2}, l=g=9.8,\Omega_D=2/3)$'+'\n     ' +r'$\Omega_Dt=2n\pi +\phi$',fontsize=14)
FD_text = ax1.text(2900, 2.3 , '',fontsize = 16)

line, = ax1.plot([], [], '-',markersize = 3.3, color = 'r',label = r'$\Omega_D=2/3,\phi = 0$')#
ax1.legend(fontsize=12,loc='upper right')


def init():
    """initialize animation"""
    line.set_data([], [])
    FD_text.set_text('')
    # line.set_label('')
    return line, FD_text

def animate(i):
    """perform animation step"""
    global FD
    FD = s[i]
    # comp = Nonlinear_Cromer()
    # comp.calculate()
    # comp.pick_phase_space()
    line.set_data(T[i], THETA[i])
    FD_text.set_text(r'$F_D=%.3f$' % FD)
    # line.set_label(r'$\Omega_D=2/3,\phi = 0$'+r'$F_D=%.2f$' % FD)
    # ax1.legend(fontsize=12,loc='best')
    return line, FD_text

ani = animation.FuncAnimation(fig, animate, frames=len(s),
                              interval=150, blit=True, init_func=init)

# ani.save('ChangeDriveSeeOscillation.mp4', fps=3, extra_args=['-vcodec', 'libx264'])
plt.show(fig)
```