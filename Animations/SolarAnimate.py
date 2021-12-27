
from matplotlib import lines, pyplot as plt
from matplotlib.animation import FuncAnimation

import numpy as np

data = np.load('../data/Orbits.npy')
Positions = data[:,:,(0,1)]

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

ax6 = ax.twinx()
ax6.set_xlim(-r, r)
ax6.set_ylim(-r, r)

ax7 = ax.twinx()
ax7.set_xlim(-r, r)
ax7.set_ylim(-r, r)

ax8 = ax.twinx()
ax8.set_xlim(-r, r)
ax8.set_ylim(-r, r)

ax9 = ax.twinx()
ax9.set_xlim(-r, r)
ax9.set_ylim(-r, r)


# Plotting graph for bodies
S, = ax.plot(0, 0, '.-', color='#F3FF33', label='Sun')
M, = ax2.plot(0, 0, '.-', color='#E933FF', label='Mercury')
V, = ax3.plot(0, 0, '.-', color='#FF33C4', label='Venus')
E, = ax4.plot(0, 0, '.-', color='#3396FF', label='Earth') 
A, = ax5.plot(0, 0, '.-', color='#FF3333', label='Mars')
J, = ax6.plot(0,0, '.-', color = '#FF5733', label='Jupiter')
W, = ax7.plot(0,0, '.-', color='#36FF33', label='Saturn')
U, = ax8.plot(0,0, '.-', color='#3358FF', label='Uranus')
N, = ax9.plot(0,0, '.-', color='#C133FF', label='Neptune')


ax.legend([S, M, V, E, A, J, W, U, N], [S.get_label(), M.get_label(), V.get_label(), E.get_label(), A.get_label(),
        J.get_label(), W.get_label(), U.get_label(), N.get_label()], loc=0)
  
def animation_function(i):
    j=150
    while i < 4000:
        S.set_data(Positions[::j,0,0][i], Positions[::j,0,1][i])
        M.set_data(Positions[::j,1,0][i], Positions[::j,1,1][i])
        V.set_data(Positions[::j,2,0][i], Positions[::j,2,1][i])
        E.set_data(Positions[::j,3,0][i], Positions[::j,3,1][i])
        A.set_data(Positions[::j,4,0][i], Positions[::j,4,1][i])
        J.set_data(Positions[::j,5,0][i], Positions[::j,5,1][i])
        W.set_data(Positions[::j,6,0][i], Positions[::j,6,1][i])
        U.set_data(Positions[::j,7,0][i], Positions[::j,7,1][i])
        N.set_data(Positions[::j,8,0][i], Positions[::j,8,1][i])
        return 
  
animation = FuncAnimation(figure,func = animation_function,interval = 10)
plt.show()
plt.close()
print(Positions[:,0,0].shape[0])