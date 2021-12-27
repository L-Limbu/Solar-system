from data import initail
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

data = np.load('./data/Orbits.npy')
Names = initail.Names
N = Names.shape[0]


def plotxy():
    Positions = data[:,:,(0,1)]
    for k in range(N):
        plt.plot(Positions[:,k,0], Positions[:,k,1], '--', label=Names[k])

    plt.axis('equal')
    plt.ylabel('y (AU)')
    plt.xlabel('x (AU)')
    fontP = FontProperties()
    fontP.set_size('xx-small')
    plt.legend(bbox_to_anchor=(0.8,1), loc='upper left', prop= fontP)
    plt.savefig('./data/solarOrbit')
    plt.close()

def plotxz():
    PositionsXZ = data[:,:,(0,2)]
    for k in range(N):
        plt.plot(PositionsXZ[:,k,0], PositionsXZ[:,k,1], '--', label=Names[k])
    plt.axis('equal')
    plt.ylabel('z (AU)')
    plt.xlabel('x (AU)')
    fontP = FontProperties()
    fontP.set_size('xx-small')
    plt.legend(bbox_to_anchor=(0.8,1), loc='upper left', prop= fontP)
    plt.savefig('./data/solarOrbitXZ')
    plt.close()
    
plotxy()
plotxz()