# Nuova funzione con coefficiente intermedio
import numpy as np
from matplotlib import pyplot as plt
def h(x):
    return x**2 / 2 - x**4 / 10

# Intervallo di x
x = np.linspace(-3, 3, 400)
y = h(x)

# Plot
#plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r"$\frac{x^2}{2} - \frac{x^4}{10}$", color='tab:blue')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel("x")
plt.ylabel("V(x)")
plt.grid(True)
plt.show()

