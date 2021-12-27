
from matplotlib import lines, pyplot as plt
from matplotlib.animation import FuncAnimation

import numpy as np

data = np.load('../../data/Orbits.npy')
Positions = data[:,:,(0,2)]

figure, ax = plt.subplots()

# Setting limits for x and y axis
r = 32
ax.set_xlim(-r, r)
ax.set_ylim(-r, r)

ax2 = ax.twinx()
ax2.set_xlim(-r, r)
ax2.set_ylim(-r, r)

ax3 = ax.twinx()
ax3.set_xlim(-r, r)
ax3.set_ylim(-r, r)

ax4 = ax.twinx()
ax4.set_xlim(-r, r)
ax4.set_ylim(-r, r)

ax5 = ax.twinx()
ax5.set_xlim(-r, r)
ax5.set_ylim(-r, r)

# Plotting graph for bodies
S, = ax.plot(0, 0, 'y.-', label='Sun')
M, = ax2.plot(0, 0, 'm.-', label='Jupiter')
V, = ax3.plot(0, 0, 'c.-', label='Saturn')
E, = ax4.plot(0, 0, 'b.-', label='Uranus') 
A, = ax5.plot(0, 0, 'r.-', label='Neptune')


ax.legend([S, M, V, E, A], [S.get_label(), M.get_label(), V.get_label(), E.get_label(), A.get_label()], loc=0)
  
def animation_function(j):
    i=j*150
    S.set_data(Positions[:,0,0][i], Positions[:,0,1][i])
    M.set_data(Positions[:,5,0][i], Positions[:,5,1][i])
    V.set_data(Positions[:,6,0][i], Positions[:,6,1][i])
    E.set_data(Positions[:,7,0][i], Positions[:,7,1][i])
    A.set_data(Positions[:,8,0][i], Positions[:,8,1][i])
    return 
  
animation = FuncAnimation(figure,func = animation_function,interval = 10)
plt.show()
plt.close()