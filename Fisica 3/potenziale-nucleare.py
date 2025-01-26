import matplotlib.pyplot as plt
import numpy as np
def nuclear_potential(r):
    # Costanti del modello
    A = 50  # Intensità della repulsione a corto raggio
    B = 75  # Intensità dell'attrazione a medio raggio
    mu = 0.7  # Parametro di Yukawa (1/fm)

    # Parte repulsiva (A/r^12)
    repulsive = A / r**12

    # Parte attrattiva (-B * exp(-mu * r) / r)
    attractive = -B * np.exp(-mu * r) / r

    # Potenziale totale
    return repulsive + attractive

x = np.linspace(0,5, 100000)
def V(x):
    if x>0:
        return nuclear_potential(x)
    elif x == 0:
        return 5000
def y(x):
    return - (13.3)**2/(4*np.pi) * (np.exp(-0.7 * x)/x)
def f(x):
    if x == 0:
        return 5000
    elif x <= 2.5:
        return -30
    elif x> 2.5:
        return 0
f_list = []
z_list = []
V_list = []
for i in x:
    f_list.append(f(i))
    z_list.append(0)
    V_list.append(V(i))
f_list = np.array(f_list)
z_list = np.array(z_list)
plt.figure()
plt.xlabel(r"$r$ [fm]")
plt.ylabel(r"$V$ [MeV]")
plt.ylim(-40,+40)
plt.xlim(-0.1,5)
plt.plot(x, z_list, color="black")
plt.grid(True, ls="dashed", color="gray")
plt.plot(x, f_list, color="tab:blue", label="Modello a buca di potenziale")
plt.plot(x, V_list, color="tab:orange", label="Modello più accurato")
plt.legend()
plt.show()
