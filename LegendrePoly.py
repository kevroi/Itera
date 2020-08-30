import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.special import legendre
from sympy.interactive import printing
printing.init_printing(use_latex=True)

xvals = np.linspace(-1, 1, 1000)

# First 5 Legendre Polynomials as a function of x
plt.title("Wavefunctions of a particle in an infinite square well")
plt.xlabel(sp.Symbol(r'$x$'))
plt.ylabel(sp.Symbol(r'$y$'))
plt.xlim(-1, 1)
for i in range(1, 6):
    yvals = legendre(i)(xvals)
    plt.plot(xvals, yvals, label=fr"$P_{i}(x)$")
plt.legend()
plt.grid()
plt.show()


#Legendre Polynomials as a function of trig & hyperbolic functions
fig, ax = plt.subplots(3,2)
fig.suptitle(r"First 5 Legendre Polynomials - These are solutions to $(1-x^2)\frac{d^2y}{dx^2} -2x\frac{dy}{dx} + n(n+1)y = 0$")
ax[0,0].set(xlabel=r"$\sin(x)$", ylabel=r"$y$")
ax[1,0].set(xlabel=r"$\cos(x)$", ylabel=r"$y$")
ax[2,0].set(xlabel=r"$\tan(x)$", ylabel=r"$y$")
ax[0,1].set(xlabel=r"$\sinh(x)$", ylabel=r"$y$")
ax[1,1].set(xlabel=r"$\cosh(x)$", ylabel=r"$y$")
ax[2,1].set(xlabel=r"$\tanh(x)$", ylabel=r"$y$")

for i in range(1, 6):
    yvals = legendre(i)(np.sin(xvals))
    ax[0,0].plot(xvals, yvals, label=fr"$P_{i}(x)$")
    ax[0,0].grid()

for i in range(1, 6):
    yvals = legendre(i)(np.cos(xvals))
    ax[1,0].plot(xvals, yvals, label=r"$P_{i}(x)$")
    ax[1,0].grid()

for i in range(1, 6):
    yvals = legendre(i)(np.tan(xvals))
    ax[2,0].plot(xvals, yvals, label=r"$P_{i}(x)$")
    ax[2,0].grid()

for i in range(1, 6):
    yvals = legendre(i)(np.sinh(xvals))
    ax[0,1].plot(xvals, yvals, label=fr"$P_{i}(x)$")
    ax[0,1].grid()

for i in range(1, 6):
    yvals = legendre(i)(np.cosh(xvals))
    ax[1,1].plot(xvals, yvals, label=r"$P_{i}(x)$")
    ax[1,1].grid()

for i in range(1, 6):
    yvals = legendre(i)(np.tanh(xvals))
    ax[2,1].plot(xvals, yvals, label=r"$P_{i}(x)$")
    ax[2,1].grid()

fig.tight_layout()
plt.show()