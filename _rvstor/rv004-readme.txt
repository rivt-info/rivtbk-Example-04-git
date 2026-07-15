
--------------------------------------------------------------------------------
| rivt | Viscous Damping | R Holland | v-1.0.0a13 | 2026-07-15 - 01:04AM
--------------------------------------------------------------------------------


0.4-1 | Equivalent Viscous Damping
================================================================================
 
Equivalent viscous damping is the simplest form of damping for analysis
since the governing differential equation of motion is linear and hence
amenable to analytical solution. This section determines the damping
coefficient for viscous damping so that it is equivalent in some sense to
the combined effect of all damping mechanisms present in the actual
structure. [0.4.1]
 
          ----------------------------------------
Fig. 1 - Ideal Viscous Damping Model [file: img/fig201-1.png  ]
          ----------------------------------------

 
The simplest definition of equivalent viscous damping is based on the
measured response of a system to harmonic force at exciting frequency omega
equal to the natural frequency omega_n of the system. The damping ratio
zeta_eq is calculated from using measured values of u_o and
(u_st)_o. This is the equivalent viscous damping since it accounts for all
the energy-dissipating mechanisms that existed in the experiments.
 
 

0.4-2 | Measured Viscous Damping
--------------------------------------------------------------------------------
 
 
          ----------------------------------------
Fig. 2 - Measured Viscous Damping Model [file: img/fig201-2.png  ]
          ----------------------------------------

 
The most common method for defining equivalent viscous damping is to equate
the energy dissipated in a vibration cycle of the actual structure and an
equivalent viscous system. For an actual structure the force-displacement
relation obtained from an experiment under cyclic loading with displacement
amplitude u_o is determined; such a relation of arbitrary shape is shown
schematically in Fig. 2. The energy dissipated in the actual structure
is given by the area E_D enclosed by the hysteresis loop. Equating this to
the energy dissipated in viscous damping given by Eq.1 leads to
 

Eq.1
[LaTeX] 4 \\pi \\zeta_{\\mathrm{eq}} \\frac{\\omega}{\\omega_n} E_{S o}=E_D \\quad

 
or, equivalently,
 
┌  Eq-2 | 
│
│               1     1        1  
│     ζ_eq = 1⋅───⋅1⋅────⋅E_D⋅────
│              4⋅π   ⎛ω ⎞     E_So
│                    ⎜──⎟         
│                    ⎝ωₙ⎠         
└


 
where the strain energy, E_So = ku_o2/2, is calculated from the
stiffness k determined by experiment.
 
The experiment leading to the force-deformation curve of Fig. 3.9.1 and
hence E_D should be conducted at omega = omega_n, where the response of the
system is most sensitive to damping. Thus Eq.  specializes to
 
┌  Eq-3 |                           
│
│               1       1  
│     ζ_eq = 1⋅───⋅E_D⋅────
│              4⋅π     E_So
└


 
The damping ratio zeta_eq determined from a test at omega = omega_n would
not be correct at any other exciting frequency, but it would be a
satisfactory approximation.
 
It is widely accepted that this procedure can be extended to model the
damping in systems with many degrees of freedom. An equivalent viscous
damping ratio is assigned to each natural vibration mode of the system in
such a way that the energy dissipated in viscous damping matches the actual
energy dissipated in the system when the system vibrates in that mode at
its natural frequency.
 
In this book the concept of equivalent viscous damping is restricted to
systems vibrating at amplitudes within the linearly elastic limit of the
overall structure. The energy dissipated in inelastic deformations of the
structure have also been modeled as equivalent viscous damping in some
research studies. This idealization is generally not satisfactory, however,
for the large inelastic deformations of structures expected during strong
earthquakes. We shall account for these inelastic deformations and the
associated energy dissipation by nonlinear force-deformation relations.
 
 


--------------------------------------------------------------------------------

[0.4.1] Anil K. Chopra, Dynamics of Structures: Theory and Applications
toEarthquake Engineering. Englewood Cliffs, NJ, USA: Prentice Hall, 1995.

