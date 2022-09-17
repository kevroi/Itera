# Monte Carlo Simulations

## Monte Carlo Integration (one dimension)
This is a numerical method based on the relationship between the mean value of a function over an interval [a,b], and the integal of the function over the same interval. For a sufficiently large N,

$$
\int_a^b f(x) \textrm{d}x = \lim_{n \to \infty} \frac{b-a}{n} \sum_{i=1}^n f(x_i)
$$

Using this to numerically integrate sin(x) using 1000 x-values:

![Monte Carlo in action](./plots/MonteSS.png)

The code for generating this figure can be found in `mc_1d/MonteCarloInt.py`.

## Volume of an n-dimensional Sphere (multi-dimensional)
The script `mc_n_sphere/nSphere.py` computes the volume of a sphere of radius r, living in n+1 dimensions (mathematically known as an n-sphere, S<sub>n</sub>).

S<sub>n</sub> = { x ϵ ℝ<sup>n+1</sup> : ||x|| = r }

Error analysis across different dimensions:
<img src="./plots/nSphereErr.png" alt="Integration Error as a function of points used">