## Definition of the helical flux

We start from the helical flux function

$$\psi(r, \xi, t) = \psi_0(r_s) + \frac{1}{2}\psi''(r_s)(r - r_s)^2 + \tilde{\psi}\cos\xi, \qquad \xi = 2\theta - \zeta - \phi(t),$$

where:

- $r$ is the radial coordinate (minor radius);
- $\theta$ and $\zeta$ are the poloidal and toroidal angles, respectively;
- $r_s$ is the radius of the resonant (rational) surface, where the safety factor satisfies $q(r_s) = m/n = 2/1$;
- $\psi_0(r_s)$ is the unperturbed flux evaluated at the resonant surface;
- $\psi^{\prime\prime}(r_s)$ is the second radial derivative of the unperturbed flux at $r_s$, which measures the magnetic shear (curvature of the flux profile);
- $\tilde{\psi}$ is the small amplitude of the helical perturbation (assumed positive);
- $\xi$ is the helical phase, combining poloidal and toroidal angles;
- $\phi(t)$ is the time-dependent phase that represents the rotation of the magnetic island (it does not affect the island width, only its angular position).

Our goal is to derive the total island width

$$W = 4\sqrt{\frac{\tilde{\psi}}{\psi''(r_s)}}.$$

## Critical points of the flux function

We compute the first derivatives of $\psi$ with respect to $r$ and $\xi$:

$$\frac{\partial\psi}{\partial r} = \psi''(r_s)(r - r_s),$$

since $\partial\xi/\partial r = 0$, and

$$\frac{\partial\psi}{\partial\xi} = -\tilde{\psi}\sin\xi.$$

The critical points are obtained by setting both derivatives to zero:

- From $\frac{\partial\psi}{\partial r} = 0$:  
  $$r = r_s.$$

- From $\frac{\partial\psi}{\partial\xi} = 0$:  
  $$\sin\xi = 0 \quad \Rightarrow \quad \xi = 0 \ \ \text{or} \ \ \xi = \pi.$$

Thus, we have two critical points at $r = r_s$:

- $\xi = 0$: maximum point;
- $\xi = \pi$: minimum point.

## Classification using the Hessian matrix

To confirm the nature of these critical points, we compute the Hessian matrix:

$$H = \begin{bmatrix}
\frac{\partial^2\psi}{\partial r^2} & \frac{\partial^2\psi}{\partial r \partial \xi} \\
\frac{\partial^2\psi}{\partial \xi \partial r} & \frac{\partial^2\psi}{\partial \xi^2}
\end{bmatrix}
= \begin{bmatrix}
\psi''(r_s) & 0 \\
0 & -\tilde{\psi}\cos\xi
\end{bmatrix}.$$

The determinant is

$$\det H = -\psi''(r_s)\tilde{\psi}\cos\xi.$$

Evaluating at each critical point:

- At $\xi = 0$: $\cos 0 = 1$, so  
  $$\det H = -\psi''(r_s)\tilde{\psi} < 0 \quad \Rightarrow \quad \text{saddle point.}$$

- At $\xi = \pi$: $\cos \pi = -1$, so  
  $$\det H = \psi''(r_s)\tilde{\psi} > 0,$$  
  and since the trace is positive $\psi''(r_s) + \tilde{\psi} > 0$, this is a local minimum, the center of the island.
  
## Equation of the separatrix

The separatrix is the contour line that passes through the saddle point. At the saddle point $(r_s, 0)$, the value of the flux is

$$\psi_{\text{saddle}} = \psi_0(r_s) + \tilde{\psi}.$$

Therefore, the separatrix satisfies

$$\psi(r, \xi) = \psi_{\text{saddle}} = \psi_0(r_s) + \tilde{\psi}.$$

Substituting the expression for $\psi$:

$$\psi_0(r_s) + \frac{1}{2}\psi''(r_s)(r - r_s)^2 + \tilde{\psi}\cos\xi = \psi_0(r_s) + \tilde{\psi}.$$

$$\frac{1}{2}\psi''(r_s)(r - r_s)^2 = \tilde{\psi}(1 - \cos\xi).$$

Using the trigonometric identity $1 - \cos\xi = 2\sin^2(\xi/2)$:

$$\frac{1}{2}\psi''(r_s)(r - r_s)^2 = 2\tilde{\psi}\sin^2(\xi/2).$$

$$\psi''(r_s)(r - r_s)^2 = 4\tilde{\psi}\sin^2(\xi/2).$$

$$r - r_s = \pm 2\sqrt{\frac{\tilde{\psi}}{\psi''(r_s)}}\sin(\xi/2).$$

## Total island width

The island reaches its maximum radial extension at the center, where $\xi = \pi\$, so

$$(r - r_s)_{\text{max}} = \pm2\sqrt{\frac{\tilde{\psi}}{\psi''(r_s)}}.$$

Thus, the island boundaries are located at

$$r = r_s \pm 2\sqrt{\frac{\tilde{\psi}}{\psi''(r_s)}}.$$

The total width $W$ is the distance between these two boundaries:

$$W = \left( r_s + 2\sqrt{\frac{\tilde{\psi}}{\psi''(r_s)}} \right) - \left( r_s - 2\sqrt{\frac{\tilde{\psi}}{\psi''(r_s)}} \right) = 4\sqrt{\frac{\tilde{\psi}}{\psi''(r_s)}}.$$

## Physical interpretation

- The island width scales as $\sqrt{\tilde{\psi}}$: larger perturbations produce wider islands.
- The width is inversely proportional to $\sqrt{\psi''(r_s)}$: stronger magnetic shear (larger curvature of the flux profile) reduces the island size.
- The separatrix delimits the region of closed field lines (inside the island) from the open ones (outside).
- The phase $\phi(t)$ controls the rotation of the island but does not affect its width, it only shifts the island in the angular coordinate \(\xi\).

---
