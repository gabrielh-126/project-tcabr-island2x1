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

The earliest priority of tokamak research was to establish methods of setting up and controlling discharges free of from gross MHD or positional instabilites. So, a set of basic eletromagnetic diagnostics was developed to mesaure the plasma current, position, shape and MHD properties. This activity has been studied with coils at the edge of the plasma, to measure the magnetic field perturbations. Internal MHD effects also have been studied with X-ray diode system, who measure the emission from the hot central regions of the plasma.

Another subject of interest is measuring the energy confinement time. Thies is done by using a diamagnetic loop to determine the energy content, $W$, and calculating the confinement time from $\tau_E = W/P$, where P is the power input to the plasma. However, this is not as reliable as obtaining the plasma energy directly from measurements of the density and temperature profiles. In present tokamaks the electron temperature is often determined from electron cyclotron emission measurements. The ion temperature is often determined from the Doppler broadening of radiation produced by the decay of leves that are populated following charge exchange with neutral beams. The importance of impurities was realized early in the tokamak programme when it was found that it was not possible to obtain a stable tokamak discharge in a insufficiently clean vessel. Plasma impurities radiate strongly and result in the reduction o $\tau_E$, preventing the ignition. It was also recognized that the production of reproducible discharges depend strongly on the control of impurities. These problems led to a substantial development of spectroscopic diagnostics to examine the production and behaviour of impurities.

Measurements of high frequency plasma fluctuations have been undertaken to establish possible mechanisms to account for the anomalous transport observed in tokamaks. The principal techiniques involve the use of heavy ion beam probles and edge probes. Both magnetic and eletrostatic turbulence are regarded as possible causes of anomalous transport. The evaluation of these effects requires measurements of the fluctuations of dennsitu, temperature, and field strenght throughout the plasma volume.

## Magnetic measurements

Basic measurements of a tokamak are the plasma current, loop voltage, plasma position and hape, stored plasma energy, and current distribution. The local magnetic field can be measured using a small coil. The principle is to determine the flux linking the coil from the induced voltage V

$\Phi = - \int_{t_0}^{t}{V(t^')dt^'}$,

and to calculate the average value of the normal component of magnetic field B from the flux using

$B\cdot n = \frac{\Phi}{NA}$,

where N is the number of turns and A is their average area. All components of the magnetic field may be measured using sets of orthogonal coils.

The toroidal field outside  the plasma is determined by the external field coils and is usually measured by only a few detector coils. The strenght and direction of the field in the poloidal plane dependes on the plasma behaviour. Magnetic coils are place on the vacuum vessel to determine the local field in the direction normal to and parallel to the measuring surface. In addition to the coils determining B on the measuring surface, there are also Rogowski coils to determine current, and toroidal and poloidal flux loops to determine the total enclosed flux and the loop voltage.

### Plasma current

Ampère's law relates the integral of the magnetic field strenght round a closed loop to the total current enclosed by the loop:

$I = \frac{1}{\mu_0}\oint B\cdot dl$,

where $dl$ is an element of lenght of the loop. The toroidal current is determined using a continous Rogowski coil. The coil consits of multiple turn coil of wire which returns along the exis of the coil to avoid enclosing any the flux parallel to the current. If the individual turns are small compared with the total size of the coil, then $B$ varies only slighty across a turn and the flux measured per unit length of coils, given by

$d\Phi = nAB\cdot dl$,

where n are the turn per unit lenght, each of area A. So the total flux linking the coil is

$\Phi = nA\oint B\cdot dl$.

We can put all togheter to determine the current such as

$I(t) = -\frac{\int_{t_0}^{t}{V(t^')dt^'}}{nA\mu_0}$.

### Loop voltage

The simplest measurements is that of the toroidal loop voltage which is determined by measring the voltage round a toroidal loop of wire parallel to the plasma. The loop voltage is useful in determining resistance and the Joule heating of the plasma. The voltage is induced by flux changes due both to currents in the primary circuit and the plasma current itself. Only when plasma current and the current density profile are constant in time, the toroidal voltage is uniform across the plasma and equal to the loop voltage measured at the surface.

### Plasma surface

The shape and position of the outermost closed magnetic surface of the plasma can be determined from the toroidal loop voltage and poloidal field mesured at many points on the vacuum vessel. To identify the last closed flux surface, we need an extrapolation from the measured poloidal flux, $\psi$, at the wall using $\nabla^2\psi = 0$. This procesdure relies on measurements being made relatively close to the plasma surface, otherwise errors in extrapolation become large.

### Plasma position and shave

In addition to giving the position of the plasma surface, the magnetic mesaruements can be used to give the position of the centre of the current channel. One mehtod is to evaluate moments of the current density profile. The first current moment gives the position of the current centre, $R_c$ defined bu

$R_c^2 = \frac{1}{I}\int j_\phi R^2dA$.

In the simplest case where the measuring surface is a flux surface, $R_c$ is

$R_c^2 = \frac{1}{\mu_0 I}\oint B_pR^2dl$.

where $j_\phi$ is the toroidal current density and B_p is the poloidal field at the surface. Higher moments give information on the shape of the current channel. The second moment gives the elongation and the third one gives the triangularity.

### Plasma energy and internal inductance

The plasma energy can be determined using the force balance between the magneticfield and  the kinetic pressure. There are two methods, onde using the force balance along the major radius, the other the force balance along the minor radius.

The quantities required are the magnitude and direction of the magnetic field at the measuring surface, and the diamagnetic flux. The latter is the difference between the total toroidal flux with plasma and that in the absence of plasma. This flux is measured with a loop enclosing the plasma, encircling it poloidally. The vacuum flux is determined either bt measuring the current flowing in the toroidal field coils, or the toroidal field outside the vacuum vessel.

### Instability measurements

Several mhd instabilities occur in tokamaks, using coils these perturbations can be detected at the plasma edge even when the amplitude of the instability is quite small. This is because the instabilities usually rotate due to the plasma velocity and the diagmanetic velocity, leading to timesclaes $10^3 - 10^4$ times shorter than typical timesclaes for changes in the equilibrium magnetic field.

Magnetic perturbations sometimes become stationary in the laboratory frame due to a process knwon as mode locking. The detection of such stationary perturbations is more difficuld and relies on the integrating the output of several coils combined in such a way as to eliminate the equilibrium field, and only detect the toroidal harmonic perturbations such as n = 1 or 2.

By making measurements at different poloidal and toroidal locations the structure of magnetic perturbations can be determined as well as their amplitude and frequency. The struture may vary across the radius, with modes m = 1, n = 1 there may be an structure in the centre and an m = 3, n = 1 the structure may be near the plasma edge.


