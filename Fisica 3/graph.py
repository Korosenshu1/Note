import numpy as np
import matplotlib.pyplot as plt

# Parametri forniti
sigma_th = 0.66e-24
Gamma_prime = 1e10
Gamma = 6.2e6
Gamma_2 = 100.2e6
omega_0 = 1e15

# Intervallo di omega
omega = np.linspace(omega_0-1e10,omega_0+1e10, 100000)

# Definizione della funzione sigma(omega)
def sigma(omega, omega_0, Gamma, Gamma_prime, sigma_th):
    numerator = (omega_0**4) / 4
    denominator = (omega - omega_0)**2 + ((Gamma + Gamma_prime) / 2)**2
    return sigma_th * numerator / denominator

# Calcolo di sigma(omega)
sigma_values = sigma(omega, omega_0, Gamma, Gamma_prime, sigma_th)
sigma_values_2 = sigma(omega, omega_0, Gamma_2, Gamma_prime, sigma_th)



# Creazione del grafico
plt.figure(figsize=(10, 6))
plt.plot(omega, sigma_values, label=r"$\sigma(\omega)$", color="tab:blue")
plt.plot(omega, sigma_values_2, label=r"$\sigma_2(\omega)$", color="tab:orange")
plt.axvline(x=omega_0, color="red", linestyle="--", label=r"$\omega_0$")
plt.title(r"Plot di $\sigma(\omega)$", fontsize=16)
plt.xlabel(r"$\omega$ (rad/s)", fontsize=14)
plt.ylabel(r"$\sigma(\omega)$", fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)
plt.show()



