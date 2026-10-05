# Bremsstrahlung emission

Bremsstrahlung is electromagnetic radiation produced when a charged particle, most commonly an electron, is accelerated or decelerated by the electric field of another charged particle. In a plasma, the most important contribution usually comes from the Coulomb interaction between free electrons and ions. As the electron is deflected by the electric field of the ion, it undergoes acceleration and emits a photon. The photon energy is determined by the energy lost by the electron during the interaction. Because the electron can lose a continuous range of energies, bremsstrahlung produces a continuous radiation spectrum. For sufficiently energetic electrons, this radiation can extend into the X-ray range.

Historically, X-ray emission was found to contain both a continuous component and discrete characteristic lines. Wilhelm Röntgen discovered X-rays in 1895, while subsequent studies, including those by Charles Barkla and Arnold Sommerfeld, contributed to the understanding of their different components. The continuous component associated with the deceleration of electrons became known as bremsstrahlung, or "braking radiation", while characteristic X-rays are associated with transitions between bound atomic states.

Bremsstrahlung can result from both electron-ion and electron-electron interactions. Electron-ion bremsstrahlung is generally the main contribution considered in thermal plasma radiation because the ion's electric field can strongly deflect the electron. Electron-electron bremsstrahlung can also contribute, particularly under conditions where electron energies are sufficiently high.

# Radiation recombination

Radiative recombination occurs when a free electron is captured by an ion and becomes bound, with the excess energy released as a photon:

$e^- + x^{q+} \longrightarrow X^{(q-1)+} + h\nu$

The photon energy is approximately the sum of the electron's kinetic energy and the binding energy of the final bound state:

$h\nu = E_{kin} + E_{bind}$

Since the kinetic energy of the incident electron can have a continuous range of values in a plasma, radiative recombination contributes to the continuum emission. The presence of different possible final bound states can also produce discontinuities or edges associated with their binding energies.

# Dielectric recombination

Dielectronic recombination is a two-step resonant recombination process. First, a free electron interacts with an ion and simultaneously excites a bound electron while being captured:

$e^- + X^{q+} \longrightarrow X^{(q-1)+**}$

This produces a doubly excited, autoionizing state. The system can subsequently undergo radiative stabilization, producing a photon:

$X^{(q-1)+**} \longrightarrow X^{(q-1)+*} + h\nu$

Alternatively, the intermediate state can autoionize and return to the initial charge state. The radiative stabilization produces dielectronic satellite lines, so dielectronic recombination can contribute to line emission in X-ray spectra.

# Contributions to SXR emission

These processes correspond to different types of radiative transitions: free-free interactions (Bremsstrahlung), free-bound interactions (Radiative recombination) and bound-bound interactions (Dielectronic recombination).

Therefore, the soft X-ray emission measured by an SXR diagnostic can contain contributions from continuum processes, such as bremsstrahlung and radiative recombination, as well as discrete line and satellite-line emission associated with recombination and atomic transitions.

# Impurity lines

The identification of the charge states and atomic transitions responsible for SXR emission from high-Z impurities is fundamental in fusion experiments. Impurity radiation contributes to the total radiative power loss of the plasma and can be used to investigate impurity transport, particle confinement, and the spatial distribution of highly ionized species.

In the wavelength range of approximately 20–70 Å, the emission from highly ionized impurities does not necessarily appear as isolated spectral lines. Instead, the spectrum can exhibit a quasi-continuous structure composed of a large number of closely spaced and overlapping spectral lines. The relative contribution of these lines depends strongly on the electron temperature, electron density, and impurity charge-state distribution.

Therefore, the interpretation of an SXR signal requires knowledge of the ionization states present in the plasma. As the electron temperature changes, the relative abundance of different charge states changes, modifying both the intensity and spectral distribution of the impurity radiation. Consequently, SXR emission can be strongly sensitive to the local electron temperature and to impurity concentrations.

# Ionization equilibrium

The spatial distribution and relative abundance of different ionization states in a plasma can be described using different approximations. Two important approaches are the coronal equilibrium model and the collisional-radiative model (CRM).

## Coronal Equilibrium

The coronal equilibrium model is appropriate for sufficiently low electron densities, where radiative decay of excited states is much faster than collisional processes that would significantly modify their populations. In this regime, most ions remain in their ground state, and the populations of excited states can be treated as being in quasi-steady state.

The equilibrium between two neighboring charge states is determined by the balance between electron-impact ionization and radiative plus dielectronic recombination. For an ion with charge state $z$, the equilibrium condition can be written schematically as

$\frac{S_z(T_e)}{\alpha_{z+1}(T_e)} = \frac{n_{z+1}}{n_z}$,

where $S_z$ is the electron-impact ionization rate coefficient and $\alpha_{z+1}$ is the total recombination rate coefficient.

In the simplest coronal approximation, the fractional abundance of each charge state is therefore primarily a function of the electron temperature,

$f_z \approx f_z(T_e)$.

Consequently, in a plasma with a radial electron-temperature gradient, different charge states tend to dominate at different radial positions. Lower ionization states are generally more abundant in colder regions, while higher ionization states become dominant toward hotter regions.

This ionization structure is particularly important for SXR diagnostics because each charge state has its own set of allowed atomic transitions. Therefore, changes in the local electron temperature can modify the charge-state distribution and, consequently, the intensity and spectral composition of the observed SXR emission.

## Collisional Radiative Model (CRM)

The coronal approximation becomes insufficient when the electron density increases or when metastable states and collisional processes significantly affect the atomic populations. In this regime, collisional excitation and de-excitation, radiative decay, ionization, and recombination processes must be considered simultaneously.

The collisional-radiative model separates the atomic population into relatively long-lived states, such as the ground and metastable states, and short-lived excited states. The populations of these states are obtained by solving a coupled set of rate equations that accounts for both collisional and radiative processes.

The CRM provides effective ionization and recombination coefficients that depend on the electron temperature and density.

