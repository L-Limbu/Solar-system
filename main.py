import numpy as np
from data import initail
#constants
G = 6.67408e-11
Au = 1.49598e11
N = initail.Names.shape[0]

'''Initializing the conditions where initial_x_v contains the initial 
positions and velocity.'''
initial_x = np.array([initail.xPosition, initail.yPosition,initail.zPosition])*1e3
initail_v = np.array([initail.xVelocity, initail.yVelocity, initail.zVelocity])*1e3
initial_x_v = np.concatenate((initial_x.T, initail_v.T), axis=1)


def acceleration(a, b, M):
    '''a & b are the position vectors of different bodies
    and this function returns the acceleration of a body.'''
    r = a - b
    r_magnititude = np.sqrt(r@r)
    r_hat = r/r_magnititude
    return -G*M*r_hat/r_magnititude**2

def runge_kutta4(f, X,dt):
    '''4th order Runge-Kutta method used to compute the derivate/integral'''
    tn = 0
    xn = X
    while True:
        yield tn, xn
        k1 = f(tn, xn)
        k2 = f(tn + dt/2, xn + k1*dt/2)
        k3 = f(tn + dt/2, xn + k2*dt/2)
        k4 = f(tn + dt, xn + k3*dt)
        xn = xn + (1/6)*(k1 + 2*k2 + 2*k3 + k4)*dt
        tn = tn + dt

def vel_acc(t, X):
    '''This function computes and stores the velocity and accleleration'''
    
    v_a = np.zeros([N,6])
    v_a[:, (0,1,2)] = X[:,(3,4,5)]
    for i in range(N):
        a = X[:, (0,1,2)][i]
        for j in range(N):
            b = X[:,(0,1,2)][j]
            M = initail.Masses[j]
            if i != j:
                v_a[(i),(3,4,5)] += acceleration(a,b,M)
    return v_a


def run():
    '''Computes the data on planet's orbit (measured in Astronomical Unit (AU) and days'''
    
    Positions = []
    iterations = runge_kutta4(vel_acc, initial_x_v, dt=1e4)
    for n in range(600000):
        t, X = next(iterations)
        Positions.append(X)
    Positions = np.array(Positions)
    Positions = Positions[:,:,(0,1,2)]/Au
    return np.save('./data/Orbits.npy', Positions)

run()





