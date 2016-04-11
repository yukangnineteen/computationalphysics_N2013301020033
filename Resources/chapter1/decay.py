#beifen
from pylab import *
from matplotlib import animation   
import time
from math import *

N_A = []
N_B = []
N_B.append(0.0)
NN_A = []
NN_B = []
t = []
tau_A = 1.0
tau_B = 0
dt = 0
n = 0

def initialize(N_A, N_B, t, _tau_A, _tau_B, _dt, _n):
    global tau_A, tau_B, dt, n, time
    print 'initial number of nuclei A -> ',
    N_A.append(float(raw_input()))
#                                       print 'initial number of nuclei B -> ',
#                                       N_B.append(float(raw_input()))
#    print 'time constant of A -> ',
#    tau_A = float(raw_input())
    print 'time constant of B -> ',
    tau_B = float(raw_input())
    print "time step -> ",
    dt = float(raw_input())
    print "total time -> ",
    time = float(raw_input())
    t.append(0)
    n = int(time / dt)
    for i in range(n):
        t.append(dt*(i+1))
    return 0

initialize(N_A, N_B, t, tau_A, tau_B, dt, n)


for ratio in range(1,51):
    tau_B = tau_A/ratio
#    print tau_A,tau_B
    for i in range(n):
        tmp_A = N_A[i]-N_A[i]/tau_A*dt
        tmp_B = N_B[i]+dt*(N_A[i]/tau_A-N_B[i]/tau_B)
        N_A.append(tmp_A)
        N_B.append(tmp_B)
    NN_A.append(N_A)
    NN_B.append(N_B)
#    print len(NN_A[ratio-1])
#    print len(t)
    N_A=[100,]
    N_B=[0,]
#for i in range(10):
#    print len(NN_A[i])



fig = figure() 
ax1 = fig.add_subplot(1,1,1,xlim=(0, time), ylim=(-3, 100))
# ax1 = fig.add_subplot(2,1,1,xlim=(0, 2), ylim=(-4, 4))
# ax2 = fig.add_subplot(2,1,2,xlim=(0, 2), ylim=(-4, 4))
line, = ax1.plot([], [], color='red', linewidth=2.5, linestyle="-",label="A")  
#lineTh, = ax1.plot([], [], '-b')  
line2, = ax1.plot([], [], color='blue', linewidth=2.5, linestyle="-",label="B")  
xlabel('Time')
ylabel('N/N_0')
text(time*0.5, 80, r'$\tau A=1,\ \tau B=from\quad 1\quad to\quad 0.02$')
#line2Th, = ax1.plot([], [], '-r')  
def init():  
    line.set_data([], [])  
    line2.set_data([], [])  
    return line,line2

# animation function.  this is called sequentially   
def animate(i):
    x = t   
    y = NN_A[i]  
    line.set_data(x, y)     

    x2 = t   
    y2 = NN_B[i]
    line2.set_data(x2, y2)   
    return line,line2



anim1=animation.FuncAnimation(fig, animate, init_func=init,  frames=10, interval=100, blit=True)  
#savefig("chapter.png")
show()