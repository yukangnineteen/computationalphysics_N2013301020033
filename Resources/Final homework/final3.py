# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 22:57:57 2016

@author: Guoguo
"""

# Simulating the TDGL equation
# This example uses the 5-point Laplacian discretization from 
# [here](https://github.com/ketch/finite-difference-course)
#
from __future__ import division
import numpy as np

from scipy.sparse import spdiags,linalg,eye
import matplotlib.pyplot as plt


a, b, k  = 0, 1.0, 100.0
dh, dt = 1.0, 1e-3
N, T  = 256, 10001

class TDGL():
    '''
    Class to solve a PDE 
    '''
    def mu(self, u):
        return a*u + b*u*u*u 

    def laplacian(self, N):
        '''Construct a sparse matrix that applies the 5-point laplacian discretization'''
        e=np.ones(N**2)
        e2=([1]*(N-1)+[0])*N
        e3=([0]+[1]*(N-1))*N
        h=dh
        A=spdiags([-4*e,e2,e3,e,e],[0,-1,1,-N,N],N**2,N**2)
        A/=h**2
        return A

    def integrate(self, L, x, y, u):
        '''  solves the equation and plots it at differnt instants '''
        
        f = plt.figure(figsize=(15, 15), dpi=80);    

        for i in range(T):          
            u = u - dt*(self.mu(u) - k*L.dot(u))
            
            if (i==0):      self.configPlot(x, y, u, f, 1, i);
            if (i==1):      self.configPlot(x, y, u, f, 2, i);
            if (i==10):     self.configPlot(x, y, u, f, 3, i);
            if (i==100):    self.configPlot(x, y, u, f, 4, i);
            if (i==1000):   self.configPlot(x, y, u, f, 5, i);
            if (i==10000):  self.configPlot(x, y, u, f, 6, i);
     
    def configPlot(self, x, y, u,f, n_, i):
        U= u.reshape((N,N))
        sp =  f.add_subplot(3, 3, n_ )  
        plt.setp(sp.get_yticklabels(), visible=False)
        plt.setp(sp.get_xticklabels(), visible=False)
        plt.pcolormesh(x,y,U);
        plt.title('Time=%d'%i)
        
        
        
        
rm = TDGL()   # instantiate the class

# generate the grid and initialise the field
x = np.linspace(-1,1,N)
y = np.linspace(-1,1,N)
X, Y = np.meshgrid(x, y)

u=np.random.randn(N*N, 1);  # Initial data
L = rm.laplacian(N)         # construct the laplacian
rm.integrate(L, x, y, u)    # simulate
