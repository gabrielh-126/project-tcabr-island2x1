## MHD stability

Basic destabilizing forces:

(I) Current gradients

(II) Pressure gradients combined with adverse magnetic field curvature

Futhermore we can divide the instabilities in two categories:

(I) Ideal modes, instabilities that would occur even if the plasma were perfectly conducting

(II) Resistive modes, which occur dependent on the finite resistivity of the plasma

They have an infinite spectrum of possible modes, whose take the form $exp[i(m\theta - n\phi)]$, with m and n being the poloidal and toroidal mode numbers.

m - how many times the disturbance oscilates in the poloidal direction

n - how many times the disturbance oscilates in the toroidal direction

The stabilizing effects for MHD modes arise from:

(I) Magnetic field line bending, the production of a magnetic field perpendicular to the equilibrium field. This effect inscreases with m

(II) Magnetic field line compression, the production of a magnetic field parallel to the equilibrium field.

(III) Good magnetic field curvature, the centre of curvature being in the opposite direction to the pressure gradient.

For low mode numbers, the modes are not localized. However, their resonant surfaces must satisfy $m/n = q$, where q is the safety factor.

There are three principal theoretical procedures for determining stability:

(I) The energy principle, in which the potential energy change resulting from a plasma displacement $\chi(x)$ is examined

(II) Calculation of eigenfunctions and corresponding eigenvalues for the frequency $\omega$. The sign of the imaginary part of $\omega$ determines the stability

(III) Solution of the marginal stability equation ($\omega_t = 0$). Its solution satisfies the required boundary conditions for a configuration on the satilibty boundary.

## Stability theory

The basic method to determine the stability properties of a system is to analyze the behaviour of perturbations. Linear stability is determined by examining the behaviour of infinitesimal perturbations which satisfy the governing equations on the boundary conditions. The linearization is accomplisehd by writing each factor in the equations as the sum of its equilibrium value, such as

$p = p_0 + p_1$.

If whe take the product with a factor q such as p, we have

$pq = p_0q_0 + p_0q_1 + p_1q_0 + p_1q_1$.

And so on and so forth for more similar factors. In this form the terms that describe the equilibrium solution ($p_0q_0$) are canceled. Linear in the perturbed quantities ($q_0p_1$ and $p_1q_0$) are retained and higher order terms ($p_1q_1$) are negligible.

To solve these equations we use Laplace transforms. The solution has a parte which dependes on the initial conditions, and other part which is a homogeneous solutions of the equations. This homogeneous parte is comprised of eigenfunction of the system, each having an eigenvalue $\omega$, and appears in the independent factor $e^[-i\omega t]$ of the solution. In general $\omega$ is complex and

$e^[-i\omega t] = e^[-i\omega_i t + \omega_i t]$

The real part of $\omega$ describes the real frequency of the mode and the imaginary part determines stability, instability corresponding to $\omega_i > 0$.

An alternative way to determine stability is to calculate the change in potential energy to a given plasma displacement $\chi(x)$. The plasma is unstable to any perturbation $\chi(x)$ which makes  the potential energy change $\delta W[\chi]$ negative.

Because in a tokamak whe have toroidal symmetry, the perturbations can be Fourir analysed in the coordinate $\phi$. Each component has te form $e^[-in\phi]$ and can be treated separately, the component being characterized by the mode number n. Sometimes the equilibrium variation in the poloidal angle $\theta$ is sufficiently small that the Fourier components in $\theta$ are separable. So then the eigenfunctions have the form $e^[i(m\theta - n\phi)].

##Growth rates 
