import numpy as np
from scipy.optimize import bisect, newton

# Definimos la función f(x)
def f(x):
    return x**5 + 5.5*x**4 + 4.5*x**3 - 9.5*x**2 - 15.5*x - 6

# Graficamos la función para estimar los intervalos donde hay raíces
import matplotlib.pyplot as plt
x = np.linspace(-5, 3, 1000)
plt.plot(x, f(x))
plt.axhline(0, color='gray', linestyle='--')
plt.title('f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

# Usamos bisect y newton en intervalos donde f(x) cambia de signo
intervals = [(-4.5, -3.5), (-3.5, -2.5), (-2.5, -1.5), (-1.5, 0), (0, 1), (1, 2), (2, 3)]
roots_bisect = []
roots_newton = []
for a, b in intervals:
    try:
        root_bisect = bisect(f, a, b)
        roots_bisect.append(root_bisect)
    except ValueError:
        pass
    # Newton necesita un punto inicial, tomamos el punto medio
    try:
        root_newton = newton(f, (a+b)/2)
        roots_newton.append(root_newton)
    except RuntimeError:
        pass

print('Raíces encontradas con bisect:', roots_bisect)
print('Raíces encontradas con newton:', roots_newton)