From the helical flux

$\psi(r, \xi, t) = \psi_0(r_s) + \frac{1}{2}\psi^{\prime\prime}(r_s)(r-r_s)^2 + \tilde{\psi}\cos\xi; \qquad \xi = 2\theta - \zeta - \phi(t)$.

we wish to arrive at the total length

$W = 4\sqrt{\frac{\tilde{\psi}}{\psi^{\prime\prime}(r_s)}}$.

So, starting from the first equation and taking its derivative in respect to $r$ and $\xi$ we have

$\frac{\partial\psi}{\partial r} = \psi^{\prime\prime}(r_s)(r-r_s) - \tilde{\psi}\sin\xi \cdot \frac{\partial\xi}{\partial r}$,

however, since $\partial\xi/\partial r = 0$, we have

$\frac{\partial\psi}{\partial r} = \psi^{\prime\prime}(r_s)(r-r_s)$,

$\frac{\partial\psi}{\partial\xi} =  \tilde{\psi}\sin\xi$.

The critical points of this function are

$r = r_s$, and

$\sin\xi = 0 \Rightarrow \xi = 0 \ \  \text{or} \ \ \xi = \pi$.

We have two critical points at $r = r_s$, a minimum in $\xi = \pi$ and a maximum in unstable equilibrium in $\xi = 0$. Futhermore, we can examine these points using the determinant of the Hessian matrix. Which is given by

$H = \begin{bmatrix}\frac{\partial\psi}{\partial r^2} & \frac{\partial\psi}{\partial r\partial\xi} \\ \frac{\partial\psi}{\partial\xi\partial r}  & \frac{\partial\psi}{\partial \xi^2}  \end{bmatrix}$

$H = \begin{bmatrix}\psi^{\prime\prime}(r_s) & 0\\0 & -\tilde{\psi}\cos\xi \end{bmatrix}$.

So, it's determinant is given by

$\det H = -$\psi^{\prime\prime}(r_s)\tilde{\psi}\cos\xi.

In $\xi = 0$, $\det H < 0$, making this point a saddle point. In the other case, $\xi = \pi$, $\det H > 0$, with the above result from the derivative, this is a minium point.

We now use the quantile, which is a curve that passes by the saddle point and distinguishes open from close trajectories. We then make

$\psi_saddle = \psi_0(r_s) + \tilde{\psi}.

Therefore, the equation for the quantile is

$\psi(r, \ \xi) = \psi_0(r_s) + \tilde{\psi}$

$\psi_0(r_s) + \frac{1}{2}\psi^{\prime\prime}(r_s)(r-r_s)^2 + \tilde{\psi}\cos\xi = \psi_0(r_s) + \tilde{\psi}$

$\frac{1}{2}\psi^{\prime\prime}(r_s)(r-r_s)^2 = \tilde{\psi}(1 - \cos\xi)$

$(r-r_s)^2 = 2\sqrt{\frac{\tilde{\psi}}{\psi^{\prime\prime}(r_s)}}\sin(\xi/2)$

$r-r_s = \pm 2\sqrt{\frac{\tilde{\psi}}{\psi^{\prime\prime}(r_s)}}\sin(\xi/2)$.

In the center of the island (\xi = \pi) the curve reaches its maxium radial extension,, with borders in

$r = r_s \pm 2\sqrt{\frac{\tilde{\psi}}{\psi^{\prime\prime}(r_s)}}\sin(\xi/2)$.

The total lenght $W$ is the distance between those borders, given by

$W = \left( r_s + 2\sqrt{\frac{\tilde{\psi}}{\psi^{\prime\prime}(r_s)}}\sin(\xi/2)\right) - \left(r_s - 2\sqrt{\frac{\tilde{\psi}}{\psi^{\prime\prime}(r_s)}}\sin(\xi/2)\right) = 4\sqrt{\frac{\tilde{\psi}}{\psi^{\prime\prime}(r_s)}}\sin(\xi/2)$ 
