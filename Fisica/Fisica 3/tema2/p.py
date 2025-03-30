import numpy as np

def cherenkov_angle(beta, n):
    """Calcola l'angolo di Cherenkov in radianti."""
    if beta * n < 1:
        return 0  # Nessuna radiazione Cherenkov
    return np.arccos(1 / (n * beta))

def critical_angle(n):
    """Calcola l'angolo critico per la riflessione totale."""
    return np.arcsin(1 / n)

def confined_fraction(beta, n):
    """Restituisce la frazione della radiazione Cherenkov confinata."""
    theta_C = cherenkov_angle(beta, n)
    theta_crit = critical_angle(n)
    if theta_C == 0 or theta_C < theta_crit:
        return 0  # Nessuna radiazione confinata
    return (np.cos(theta_crit) - np.cos(theta_C)) / (1 - np.cos(theta_C))

# Parametri
theta_inc = np.linspace(0, np.pi/2, 100)
n = 1.5
beta = 0.9  # Velocità scelta

frac_confinata = confined_fraction(beta, n)

print(f"Frazione di luce confinata: {frac_confinata:.3f}")
