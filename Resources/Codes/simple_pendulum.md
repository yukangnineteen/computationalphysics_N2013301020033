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

theta0 = 0.2
omg0 = 0
g = 9.8
length = g / (4 * (np.pi) ** 2)

# class Euler
# use Euler METHOD to solve the pendulum
# para. & var.  :    
#             theta0, omg0, t0 - initial angel & angular velocity & time
#             l, g, dt, time - length of string, gravity acceleration, time step size & total time 
#             the time period of this pendulum - 1(s)


class Euler(object):
    global theta0, omg0, g, length
    def __init__(self, _dt = 0.01, _time = 5.):
        self.theta, self.omg, self.t = [theta0], [omg0], [0.]
        self.l, self.g, self.dt, self.time, self.n= length, g, _dt, _time, int(_time/_dt)
        self.E = [0.5*((self.l*omg0)**2+self.g*self.l*(theta0)**2)]
    def calculate(self):
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)
            self.omg.append(self.omg[-1]-self.g/self.l*self.theta[-1]*self.dt)
            self.theta.append(self.theta[-1]+self.omg[-2]*self.dt)
            self.E.append(0.5*((self.l*self.omg[-1])**2+self.g*self.l*(self.theta[-1])**2))
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


    def plot_theta(self,_ax):
        _ax.plot(self.t, self.theta, '-',label='Euler Method')
    def plot_E(self,_ax):
        _ax.plot(self.t,self.E,'-',label='Euler Method')

# class Cromer
# use Euler-Cromer METHOD to solve the pendulum
# para. & var.  :    
#             theta0, omg0, t0 - initial angel & angular velocity & time
#             l, g, dt, time - length of string, gravity acceleration, time step size & total time 
#             the time period of this pendulum - 1(s)        
class Cromer(Euler):
    def calculate(self):
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)
            self.omg.append(self.omg[-1]-self.g/self.l*self.theta[-1]*self.dt)
            self.theta.append(self.theta[-1]+self.omg[-1]*self.dt)
            self.E.append(0.5*((self.l*self.omg[-1])**2+self.g*self.l*(self.theta[-1])**2))
    def plot_theta(self,_ax):
        _ax.plot(self.t, self.theta, '-',label='Euler-Cromer Method')
    def plot_E(self,_ax):
        _ax.plot(self.t,self.E,'-',label='Euler-Cromer Method')
        

# class RK2
# use Second-order Runge-Kutta METHOD to solve the pendulum
# para. & var.  :    
#             theta0, omg0, t0 - initial angel & angular velocity & time
#             l, g, dt, time - length of string, gravity acceleration, time step size & total time 
#             the time period of this pendulum - 1(s)        


class RK2(Euler):
    def calculate(self):
        for i in range(self.n):
            midtheta = self.theta[-1] + 0.5 * self.omg[-1] * self.dt
            midomg = self.omg[-1] - 0.5 * self.g / self.l * self.theta[-1] * self.dt
            self.theta.append(self.theta[-1] + midomg * self.dt)
            self.omg.append(self.omg[-1]-self.g/self.l* midtheta*self.dt)
            self.t.append(self.t[-1] + self.dt)
            self.E.append(0.5*((self.l*self.omg[-1])**2+self.g*self.l*(self.theta[-1])**2))
    def plot_theta(self,_ax):
        _ax.plot(self.t, self.theta, '-',label='2th Runge-Kutta')
    def plot_E(self,_ax):
        _ax.plot(self.t,self.E,'-',label='2th Runge-Kutta')
        
# class Kutta4
# use Second-order Runge-Kutta METHOD to solve the pendulum
# para. & var.  :    
#             theta0, omg0, t0 - initial angel & angular velocity & time
#             l, g, dt, time - length of string, gravity acceleration, time step size & total time 
#             the time period of this pendulum - 1(s)        


class RK2(Euler):
    def calculate(self):
        for i in range(self.n):
            midtheta = self.theta[-1] + 0.5 * self.omg[-1] * self.dt
            midomg = self.omg[-1] - 0.5 * self.g / self.l * self.theta[-1] * self.dt
            self.theta.append(self.theta[-1] + midomg * self.dt)
            self.omg.append(self.omg[-1]-self.g/self.l* midtheta*self.dt)
            self.t.append(self.t[-1] + self.dt)
            self.E.append(0.5*((self.l*self.omg[-1])**2+self.g*self.l*(self.theta[-1])**2))
    def plot_theta(self,_ax):
        _ax.plot(self.t, self.theta, '-',label='2th Runge-Kutta')
    def plot_E(self,_ax):
        _ax.plot(self.t,self.E,'-',label='2th Runge-Kutta')
        
# class Kutta4
# use Second-order Runge-Kutta METHOD to solve the pendulum
# para. & var.  :    
#             theta0, omg0, t0 - initial angel & angular velocity & time
#             l, g, dt, time - length of string, gravity acceleration, time step size & total time 
#             the time period of this pendulum - 1(s)        


class RK4(Euler):
    def calculate(self):
        for i in range(self.n):
            dx1 = self.omg[-1] * self.dt
            dv1 = - self.g / self.l * self.theta[-1] * self.dt

            dx2 = (self.omg[-1] + dv1 / 2.) * self.dt
            dv2 = - self.g / self.l * (self.theta[-1] + dx1 / 2.) * self.dt

            dx3 = (self.omg[-1] + dv2 / 2.) * self.dt
            dv3 = - self.g / self.l * (self.theta[-1] + dx2 / 2.) * self.dt

            dx4 = (self.omg[-1] + dv3 ) * self.dt
            dv4 = - self.g / self.l * (self.theta[-1] + dx3) * self.dt

            dx = (dx1 + 2. * dx2 + 2. * dx3 + dx4) / 6.
            dv = (dv1 + 2. * dv2 + 2. * dv3 + dv4) / 6.

            self.theta.append(self.theta[-1] + dx)
            self.omg.append(self.omg[-1] + dv)
            self.t.append(self.t[-1] + self.dt)
            self.E.append(0.5*((self.l*self.omg[-1])**2+self.g*self.l*(self.theta[-1])**2))
    def plot_theta(self,_ax):
        _ax.plot(self.t, self.theta, '-',label='4th Runge-Kutta')
    def plot_E(self,_ax):
        _ax.plot(self.t,self.E,'-',label='4th Runge-Kutta')
        

# plot :
#        ax1 - time dependence of angel
#        ax2 - time dependence of energy
# both Euler & Euler Cromer METHOD & Second-order Runge-Kutta METHOD are used
fig= plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

def showtraj():
    for i in [Euler(), Cromer()]:
        comp = i
        comp.calculate()
        comp.find_period()
        comp.plot_theta(ax1)
        comp.plot_E(ax2)

showtraj()

t=np.linspace(0, 5, 200)
theta = theta0 * np.cos(2. * np.pi * t)
E = 0.5 * g * g / (4 * (np.pi) ** 2) * (theta0 ** 2)
ax1.plot(t,theta,'-',label='Analytical solution')
ax2.plot(t,len(t)*[E],label='Analytical solution')
ax1.plot(t,len(t)*[theta0],'k--',t,len(t)*[-theta0],'k--')

ax1.text(0.7,-0.5,r'$Period:   \tau = 1s$'+ '\n'+r'$\theta_0=0.2rad$',fontsize=16,color='red')

ax1.set_title('Simple Pendulum - angle vs time',fontsize=14)
ax2.set_title('Simple Pendulum - energy vs time',fontsize=14)
ax1.set_xlabel('time'+r'$ /\tau $',fontsize=14)
ax1.set_ylabel('Angel (radian)',fontsize=14)
ax2.set_xlabel('time'+r'$ /\tau $',fontsize=14)
ax2.set_ylabel('Energy (J)',fontsize=14)
# ax1.legend(fontsize=12,loc='best')
# ax2.legend(fontsize=12,loc='best')
for ax in fig.axes:
        # ax.spines['right'].set_color('none')
        # ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.legend(fontsize=12,loc='upper left', frameon=True)
plt.show(fig)
```