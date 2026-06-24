import rivtlib.rvapi as rv

rv.I("""Equivalent Viscous Damping

    | IMAGE | rvsrc/img/fig201-1.png | Viscous Damping Model, 80, num, not 
    
    Damping in actual structures is usually represented by equivalent viscous
    damping. It is the simplest form of damping to use since the governing
    differential equation of motion is linear and hence amenable to analytical
    solution. The advantage of using a linear equation of motion usually
    outweighs whatever compromises are necessary in the viscous damping
    approximation. In this section we determine the damping coefficient for
    viscous damping so that it is equivalent in some sense to the combined
    effect of all damping mechanisms present in the actual structure; these
    were mentioned in Section 1.4.

    The simplest definition of equivalent viscous damping is based on the
    measured response of a system to harmonic force at exciting frequency omega
    equal to the natural frequency omega_n of the system. The damping ratio
    zeta_eq is calculated from Eq. (3.4.1) using measured values of u_o and
    (u_st)_o. This is the equivalent viscous damping since it accounts for all
    the energy-dissipating mechanisms that existed in the experiments.

    Another definition of equivalent viscous damping is that it is the amount
    of damping that provides the same bandwidth in the frequency-response curve
    as obtained experimentally for an actual system. The damping ratio zeta_eq
    is calculated from Eq. (3.2.24) using the excitation frequencies f_a, f_b,
    and f_n (Fig. 3.4.1) obtained from an experimentally determined
    frequency-response curve.
    """)


rv.I("""section-label 
    

    | IMAGE | rvsrc/img/fig201-2.png | Viscous Damping Model, 80, num, not 

    [Figure 3.9.1 -- image file: figures/fig_3_9_1.png -- Plot of Resisting
    force (vertical axis) versus Deformation (horizontal axis), showing an
    irregularly shaped hysteresis loop determined from experiment. The area E_D
    is the energy dissipated in a cycle of harmonic vibration, the area E_So is
    the maximum strain energy, and u_o marks the deformation amplitude on the
    horizontal axis.]

    The most common method for defining equivalent viscous damping is to equate
    the energy dissipated in a vibration cycle of the actual structure and an
    equivalent viscous system. For an actual structure the force-displacement
    relation obtained from an experiment under cyclic loading with displacement
    amplitude u_o is determined; such a relation of arbitrary shape is shown
    schematically in Fig. 3.9.1. The energy dissipated in the actual structure
    is given by the area E_D enclosed by the hysteresis loop. Equating this to
    the energy dissipated in viscous damping given by Eq. (3.8.1) leads to

    4*pi*zeta_eq*(omega/omega_n)*E_So = E_D 
    
    zeta_eq = (1/(4*pi)) * (1/(omega/omega_n)) * (E_D/E_So)                              ... (3.9.1)

    where the strain energy, E_So = k*u_o**2/2, is calculated from the
    stiffness k determined by experiment.

    The experiment leading to the force-deformation curve of Fig. 3.9.1 and
    hence E_D should be conducted at omega = omega_n, where the response of the
    system is most sensitive to damping. Thus Eq. (3.9.1) specializes to

    zeta_eq = (1/(4*pi)) * (E_D/E_So)                              ... (3.9.2)

    The damping ratio zeta_eq determined from a test at omega = omega_n would
    not be correct at any other exciting frequency, but it would be a
    satisfactory approximation (Section 3.10.2).

    It is widely accepted that this procedure can be extended to model the
    damping in systems with many degrees of freedom. An equivalent viscous
    damping ratio is assigned to each natural vibration mode of the system
    (defined in Chapter 10) in such a way that the energy dissipated in viscous
    damping matches the actual energy dissipated in the system when the system
    vibrates in that mode at its natural frequency.

    In this book the concept of equivalent viscous damping is restricted to
    systems vibrating at amplitudes within the linearly elastic limit of the
    overall structure. The energy dissipated in inelastic deformations of the
    structure have also been modeled as equivalent viscous damping in some
    research studies. This idealization is generally not satisfactory, however,
    for the large inelastic deformations of structures expected during strong
    earthquakes. We shall account for these inelastic deformations and the
    associated energy dissipation by nonlinear force-deformation relations,
    such as those shown in Fig. 1.3.4 (see Chapters 5 and 7).
    """)

rv.R("""Bibliography | endnotes

    Anil K.Anil K. Chopra, Dynamics of Structures: Theory and Applications to
    Earthquake Engineering. Englewood Cliffs, NJ, USA: Prentice Hall, 1995.

    """)

rv.D("""Publish Doc 
    
    | PUBLISH | 201 Bearing Viscous Damping | pdf
    
    _[[METADATA]] 
    [doc]
    authors = R Holland
    version = 1.0.0a12
    repo = https://github.com/rivt-info/rivt-single-doc
    license = https://opensource.org/license/mit/
    copyright = -
    fork1_authors = -
    fork1_version = -
    fork1_repo = -
    fork1_license = https://opensource.org/license/mit/
    
    [layout]
    subtitle =  Isolation Bearing Design
    copyright = --
    client = Example 04 - rivtbook
    coverpage = true
    coverlogo_size = 30
    coverlogo = bearing1.png
    runninglogo = logo1.png
    runninglabel = rivt
    project_ref = proj. 0001
    pdf_pagesize = letter
    pdf_margins = 1in, 1in, 1in, 1in 
    pdf_link_underline = false
    ; table of contents levels: 1 - includes subdivisions, 2 - includes sections
    toc_level = 2

    [process]
    doc_verbose = true; if false minmize output during doc processing
    auto_cfg = true ; if false, config files are not updated from rivt file
    _[[END]]    
    """)
