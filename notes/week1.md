# MHD stability

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

(I) The energy principle, in which the potential energy change resulting from a plasma displacement $\xi(x)$ is examined

(II) Calculation of eigenfunctions and corresponding eigenvalues for the frequency $\omega$. The sign of the imaginary part of $\omega$ determines the stability

(III) Solution of the marginal stability equation ($\omega_t = 0$). Its solution satisfies the required boundary conditions for a configuration on the satilibty boundary.

## Stability theory

The basic method to determine the stability properties of a system is to analyze the behaviour of perturbations. Linear stability is determined by examining the behaviour of infinitesimal perturbations which satisfy the governing equations on the boundary conditions. The linearization is accomplisehd by writing each factor in the equations as the sum of its equilibrium value, such as

$p = p_0 + p_1$.

If whe take the product with a factor q such as p, we have

$pq = p_0q_0 + p_0q_1 + p_1q_0 + p_1q_1$.

And so on and so forth for more similar factors. In this form the terms that describe the equilibrium solution ($p_0q_0$) are canceled. Linear in the perturbed quantities ($q_0p_1$ and $p_1q_0$) are retained and higher order terms ($p_1q_1$) are negligible.

To solve these equations we use Laplace transforms. The solution has a parte which dependes on the initial conditions, and other part which is a homogeneous solutions of the equations. This homogeneous parte is comprised of eigenfunction of the system, each having an eigenvalue $\omega$, and appears in the independent factor $e^{-i\omega t}$ of the solution. In general $\omega$ is complex and

$e^{-i\omega t} = e^{-i\omega_i t + \omega_i t}$

The real part of $\omega$ describes the real frequency of the mode and the imaginary part determines stability, instability corresponding to $\omega_i > 0$.

An alternative way to determine stability is to calculate the change in potential energy to a given plasma displacement $\xi(x)$. The plasma is unstable to any perturbation $\xi(x)$ which makes  the potential energy change $\delta W[\xi]$ negative.

Because in a tokamak whe have toroidal symmetry, the perturbations can be Fourier analysed in the coordinate $\phi$. Each component has te form $e^{-in\phi}$ and can be treated separately, the component being characterized by the mode number n. Sometimes the equilibrium variation in the poloidal angle $\theta$ is sufficiently small that the Fourier components in $\theta$ are separable. So then the eigenfunctions have the form $e^{i(m\theta - n\phi)}$.

## Energy principle

The energy principle is based on the concept that if a physically allowable perturbation of an equilibrium lowers the potential energy, then the equilibrium is unstable. These instabilites are called ideal modes. The energy change resulting from a displacement $\xi(x)$ of the plasma is given by the volume integral

$\delta W = -\frac{1}{2}\int{\xi\cdot F d\tau}$,

where F(x) is the force arising from the displacement. The linearized force being given by

$F = j_1 \times B_0 + j_0 \times B_1 - \nabla p_1$,

where the subscripts 0 and 1 refer to the equilibrium and the perturbation. By a series of substitutions we arive at the final form for the energy principle such as

$\delta W = \frac{1}{2}\int{\left(\gamma p_0(\nabla\cdot\xi)^2 + (\xi\cdot\nabla p_0)\nabla\cdot\xi + \frac{1}{\mu_0}B_1^2 - j_0\cdot(B_1\times\xi)\right)d\tau} + \frac{1}{2}\int_{\text{vacuum}}{\frac{B_V^2}{2\mu_0} d\tau}$,

where $B_1$ is given by 

$B_1 = \nabla\times(\xi\times B_0)$,

and $B_V$ satisfies $\nabla\times B_V = 0$ togheter with the required $\xi$-dependent boundary conditions. If $\delta W$ is negative for any physically allowable $\xi$ the plasma is unstable. If $\delta W$ is positive, by the other way, the plasma is stable.
 
# Tokamak diagnostics

There are five major areas of investigations for tokamak diagnostics:

(I) Study of methos of setting up stable plasmas and the investigation of MHD instabilites.

(II) Determination of energy and particle containment times, and transport coefficients.

(II) Development of supplementary plasma heating methods.

(IV) Study and control of plasma impurities.

(V) Investigation of plasma fluctuations to determine their role in plasma transport.

The earliest priority of tokamak research was to establish methods of setting up and controlling discharges free of from gross MHD or positional instabilites. SO, a set of basic eletromagnetic diagnostics was developed to mesaure the plasma current, position, shape and MHD properties. This activity has been studied with coils at the edge of the plasma, to measure the magnetic field perturbations. Internal MHD effects also have been studied with X-ray diode system, who measure the emission from the hot central regions of the plasma.

Another subject of interest is measuring the energy confinement time. Thies is done by using a diamagnetic loop to determine the energy content, $W$, and calculating the confinement time from $\tau_E = W/P$, where P is the power input to the plasma. However, this is not as reliable as obtaining the plasma energy directly from measurements of the density and temperature profiles. In present tokamaks the electron temperature is often determined from electron cyclotron emission measurements. The ion temperature is often determined from the Doppler broadening of radiation produced by the decay of leves that are populated following charge exchange with neutral beams.
