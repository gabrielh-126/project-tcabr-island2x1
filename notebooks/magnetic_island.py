## Plotting magnetic island in 2/1

import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

# Parameters
r_s = 1
psi = 1
psi_til = 0.04
Delta = 2*np.sqrt(psi_til/psi)

# Coordinates
xi = np.linspace(0, 2*np.pi, 300)
r = np.linspace(r_s - Delta, r_s+Delta, 300)
r_pos = r_s + Delta*np.sin(xi/2)
r_neg = r_s - Delta*np.sin(xi/2)

# Total length
plt.plot([np.pi, np.pi], [r_s - Delta, r_s + Delta], 'b--', linewidth=2.5, label="Length W")
plt.text(np.pi+0.3, r_s, f'W = {2*Delta:.2f}', fontsize=12, color='blue')

# Graph plotting
plt.plot(xi, r_pos, 'r-', linewidth=2.5, label='Separatrix')
plt.plot(xi, r_neg, 'r-', linewidth=2.5)
plt.plot(0, r_s, 'ko', markersize=10, label='Saddle point (ξ=0)')
plt.plot(np.pi, r_s, 'go', markersize=10, label = "Island center (ξ=π)")

# Contour (Uncomment for the contour lines)
#R, XI = np.meshgrid(r, xi)
#psi_ = 0.5 * psi * (R - r_s)**2 + psi_til * np.cos(XI)
#contours = plt.contour(XI, R, psi_, levels=20, cmap='viridis', linewidths=0.8)
#plt.clabel(contours, inline=True, fontsize=8, fmt='%.2f')

# Layout
plt.xlabel(r'$\xi$ (helicoidal phase)', fontsize=14)
plt.ylabel(r'$r$ (radius)', fontsize=14)
plt.title(r'Magnetic island 2/1 in coordinates $(r, \xi)$', fontsize=16)
plt.grid(True, alpha=0.3)
plt.legend(loc='upper right')
plt.tight_layout()
plt.legend()
plt.show()
