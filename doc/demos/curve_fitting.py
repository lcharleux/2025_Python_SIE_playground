import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


def func(x, a, b, c):
    return a * x**2 + b * np.cos(c * x)


a0 = 3.0
b0 = 30.0
c0 = 2.5
x = np.linspace(0.0, 10.0, 100)
yp = func(x, a0, b0, c0)

p0 = np.ones(3)
psol, cov = optimize.curve_fit(func, x, yp, p0=p0)
ysol = func(x, *psol)

fig = plt.figure()
plt.scatter(x, yp, marker="+", color="r", label="data")
plt.plot(x, yp, "b-", label="fit")
plt.grid()
plt.xlabel("Input, $x$")
plt.ylabel("Output, $y$")
plt.savefig("curve_fitting.png")
