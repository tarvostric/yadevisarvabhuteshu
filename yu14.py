
import numpy as np
import matplotlib.pyplot as plt

ħ = 6.022*10**-34  
m = 1.6*10**-27  
N = 1525 
L = 16.0 

#harmonic oscillator
def V(x):
    return 0.5 * m * x**2

x = np.linspace(-L, L, N)
dx = x[1] - x[0]
ψ = np.zeros(N)

#Gaussian wave packet centered at x=0
ψ = np.exp(-(x**2)/(2*(L/10)**2)) / np.sqrt(dx)

def schrodinger_eq(ψ, V, E):
    d2ψ = np.zeros(N)
    for i in range(2, N):
        d2ψ[i] = 2*(V(x[i]) - E) * ψ[i] - ψ[i-1] + 2*ψ[i-2]
        d2ψ[i] *= (2/m) / dx**2
    return d2ψ

mine = 0.0
maxe = 10.0
tolerance = 1e-7

while maxe - mine > tolerance:
    E = (mine + maxe) / 2
    d2ψ = schrodinger_eq(ψ, V, E)
    
    if np.isnan(d2ψ).any():
        maxe = E
    else:
        mine = E

ψ /= np.sqrt(np.sum(ψ**2) * dx)

plt.plot(x, V(x), label='Potential Energy')
plt.plot(x, ψ**2, label='Probability Density')
plt.title(f'Ground State Energy: {E:.4f}')
plt.legend()
plt.show()
