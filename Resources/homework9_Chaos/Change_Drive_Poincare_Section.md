```python
# -*- coding: utf-8 -*-
"""
@author: YUE Shaosheng
Last modified on Thu Apr 24 2016
观测运动轨迹与此截面的截点( Poincare点)，设它们依次为P1,P2,P3…。原来相空间的连续轨迹在
Poincare截面上便表现为一些离散点之间的映射Pn。由它们可得到关于运动特性的信息。如不考虑
初始阶段的暂态过渡过程，只考虑Poincare截面的稳态图像，当Poincare截面上只有一个不动点和
少数离散点时，可判定运动是周期的;当Poincare截面上是一封闭曲线时，可判定运动是准周期的;
当Poincare截面上是成片的密集点，且有层次结构时，可判定运动处于混沌状态。
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
THETA = []
OMG = []
FD = .0

# class Euler
# use Euler METHOD to solve the pendulum
# para. & var.  :    
#             theta0, omg0, t0 - initial angel & angular velocity & time
#             l, g, dt, time - length of string, gravity acceleration, time step size & total time 
#             the time period of this pendulum - 1(s)


class Nonlinear_Cromer(object):
    """docstring for Nonlinear_Cromer"""
    global g, l, q, OmgD, FD
    def __init__(self, _theta0 = 0.2, _omg0 = .0, _t0 = .0, _dt = 0.04, _time = 8000.):
        self.FD = FD
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
    def pick_phase_space(self):
        t = np.array([i * OmgD / np.pi / 2 for i in self.t])
        tempt = np.array([round(i) for i in t])
        tempt2 = t - tempt
        a = []
        for i, j in enumerate(tempt2):
            if abs(j) < 0.0001:
                a.append(i)
        self.THETA = [self.theta[i] for i in a]
        self.OMG = [self.omg[i] for i in a]
        THETA.append(self.THETA)
        OMG.append(self.OMG)
        # print t, tempt, tempt2,a
        # print a


        # _ax.plot(self.THETA, self.OMG, 'o',markersize = 3.3, color = _color,label = r'$F_D = %.1f,\phi = 0$' % self.FD)


# PREPARE x.axis&y.axis data
s = np.arange(1., 1.4, 0.02)
for i in s:
    FD = i
    comp = Nonlinear_Cromer()
    comp.calculate()
    comp.pick_phase_space()


# plot:
#       ax1: theta vs time

fig = plt.figure(figsize = (16., 5))
ax1 = fig.add_subplot(111, xlim = (-4, 4), ylim = (-3, 3))

ax1.set_xlabel(r'$\theta (radians)$',fontsize=14)
ax1.set_ylabel(r'$\omega (radians/s)$',fontsize=14)
ax1.set_title(r'$Poincare Section$'+r'$(q=\frac{1}{2}, l=g=9.8,\Omega_D=2/3)$'+'\n     ' +r'$\Omega_Dt=2n\pi +\phi$',fontsize=18)
FD_text = ax1.text(3,0.6, '' )
line, = ax1.plot([], [], 'o',markersize = 3.3, color = 'r',label = r'$\Omega_D=2/3,\phi = 0$')
ax1.legend(fontsize=12,loc='upper right')
def init():
    """initialize animation"""
    line.set_data([], [])
    FD_text.set_text('')
    return line, FD_text

def animate(i):
    """perform animation step"""
    global FD
    FD = s[i]
    # comp = Nonlinear_Cromer()
    # comp.calculate()
    # comp.pick_phase_space()
    line.set_data(THETA[i], OMG[i])
    FD_text.set_text(r'$F_D=%.2f$' % FD)
    return line, FD_text

ani = animation.FuncAnimation(fig, animate, frames=len(s),
                              interval=400, blit=True, init_func=init)

# ani.save('改变驱动力看奇异吸引子', fps=3, extra_args=['-vcodec', 'libx264'])
plt.show(fig)
        


```