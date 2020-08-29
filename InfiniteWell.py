import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from sympy.interactive import printing
printing.init_printing(use_latex=True)

# Need to have Latex installed in your machine for this to work
# plt.rc('text', usetex=True) 
# plt.rc('font', family='serif')

L = 2 * np.pi # length of box along x-axis

xvals = np.linspace(0, L, 1000)

def psi(n,x):
    return np.sqrt(2/L) * np.sin(n*np.pi*x/L) # define the wave function

yvals1 = psi(1,xvals)
yvals2 = psi(2,xvals)
yvals3 = psi(3,xvals)

plt.title("Wavefunctions of a particle in an infinite square well")
plt.xlabel(sp.Symbol(r'$x$'))
plt.ylabel(sp.Symbol(r'$\psi(x)$'))

# Use these labels if you have Latex installed
# plt.xlabel(r"$x$")
# plt.ylabel(r"$\psi$")

plt.xlim(0, L)
plt.plot(xvals, yvals1, label="n=1")
plt.plot(xvals, yvals2, label="n=2")
plt.plot(xvals, yvals3, label="n=3")
plt.legend()
plt.grid()

plt.show()