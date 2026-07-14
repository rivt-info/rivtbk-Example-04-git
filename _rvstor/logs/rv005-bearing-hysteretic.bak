import rivtlib.rvapi as rv

# %% rv.I("""Rate Independent Damping
rv.I("""Rate Independent Damping

    Experiments on structural metals indicate that the energy dissipated
    internally in cyclic straining of the material is essentially independent
    of the cyclic frequency. Similarly, forced vibration tests on structures
    indicate that the equivalent viscous damping ratio is roughly the same for
    all natural modes and frequencies. Thus we refer to this type of damping as
    rate-independent linear damping. Other terms used for this mechanism of
    internal damping are structural damping, solid damping, and hysteretic
    damping. We prefer not to use these terms because the first two are not
    especially meaningful and the third is ambiguous because hysteresis is a
    characteristic of all materials or structural systems that dissipate
    energy. _[#]

    Rate-independent damping is associated with static hysteresis due to
    plastic strain, localized plastic deformation, crystal plasticity, and
    plastic flow in a range of stresses within the apparent elastic limit. On
    the microscopic scale the inhomogeneity of stress distribution within
    crystals and stress concentration at crystal boundary intersections produce
    local stress high enough to cause local plastic strain even though the
    average "global" stress may be well below the elastic limit. This damping
    mechanism does not include the energy dissipation in global plastic
    deformations, which, as mentioned earlier, is handled by a nonlinear
    relationship between force fS and deformation u.

    The simplest device that can be used to represent rate-independent linear
    damping is to assume that the damping force is proportional to velocity and
    inversely proportional to frequency:

    fD = (η*k/ω) * u̇    _[M]

    where k is the stiffness of the structure and η is a damping coefficient.
    The energy dissipated by this type of damping in a cycle of vibration at
    frequency ω is independent of ω (Fig. 3.10.1). It is given by Eq. (3.8.1)
    with c replaced by η*k/ω:

    ED = π*η*k*u0**2 = 2*π*η*E_So   _[M]

    In contrast, the energy dissipated in viscous damping increases linearly
    with the forcing frequency, as shown in Fig. 1.

    | IMAGE | img/fig3-10-1.jpg | Viscous and Rate Independent Damping, 50, num, not 

    Rate-independent damping is easily described if the excitation is harmonic
    and we are interested only in the steady-state response of this system.
    Difficulties arise in translating this damping mechanism back to the time
    domain. Thus it is most useful in the frequency-domain method of analysis
    (Section 1.10.3). The complex term k*(1 + i*η)*u represents both the
    elastic and damping forces at the same time; k*(1 + i*η) is the complex
    stiffness of the system. There are advantages in this terminology if the
    reader is familiar with complex-variable notation. The complex stiffness
    has no physical meaning, however, in the same engineering sense as the
    elastic stiffness.

""")

# %% rv.I("""Steady-State Response to Harmonic Force
rv.I("""Steady-State Response to Harmonic Force | pdfpage

    The equation for an SDF system with rate-independent linear damping,
    denoted by a crossed box in Fig. 3.10.2, is Eq. (3.2.1) with the damping
    term replaced by Eq. (3.10.1):

    m*ü + (η*k/ω)*u̇ + k*u = p(t)   _[M]

    The mathematical solution of this equation is quite complex for arbitrary
    p(t). Here we consider only the steady-state motion due to a sinusoidal
    forcing function, p(t) = p0*sin(ω*t), which is described by

    u(t) = u0 * sin(ω*t - φ)   _[M]

    The amplitude u0 and phase angle φ are

    u0 = (u_st) * 1 / sqrt( (1 - (ω/ωn)**2)**2 + η**2 )   _[M]

    φ = arctan( η / (1 - (ω/ωn)**2) )    _[M]

    These results are obtained by modifying the viscous damping ratio in Eqs.
    (3.2.11) and (3.2.12) to reflect the damping force associated with
    rate-independent damping, Eq. (3.10.1). In particular, ζ was replaced by

    ζ = c/c_c    _[M]

    ζ = (η*k/ω) / (2*m*ωn)   _[M]

    ζ = η / (2*(ω/ωn))   _[M]

    Shown in Fig 3 by solid lines are plots of u0/(u_st)0 and φ as a
    function of the frequency ratio ω/ωn for damping coefficient η = 0, 0.2,
    and 0.4; the dashed lines are described in the next section. Comparing
    these results with those in Fig. 3.2.6 for viscous damping, two differences
    are apparent: First, resonance (maximum amplitude) occurs at ω = ωn, not at
    ω < ωn. Second, the phase angle for ω = 0 is φ = arctan(η) instead of zero
    for viscous damping; this implies that motion with rate-independent damping
    can never be in phase with the forcing function.

    | IMAGE | img/fig_3.10.2.jpg | SDF Rate Independent Linear Damping, 70, num, not 

    These differences between forced vibration with rate-independent damping
    and forced vibration with viscous damping are not significant, but they are
    the source of some difficulty in reconciling physical data. In most damped
    vibration, damping is not viscous, and to assume that it is without knowing
    its real physical characteristics is an assumption of some error. In the
    next section this error is shown to be small when the real damping is rate
    independent.

    | IMAGE | img/fig_3.10.3.png | Rate Independent Damping, 70, num, not 

""")

rv.I("""Solution Using Equivalent Viscous Damping | pdfpage

    In this section an approximate solution for the steady-state harmonic
    response of a system with rate-independent damping is obtained by modeling
    this damping mechanism as equivalent viscous damping.

    Matching dissipated energies at ω = ωn (Fig. 3.10.1) led to Eq. (3.9.2),
    where ED is given by Eq. (3.10.2), leading to the equivalent viscous
    damping ratio:

    ζ_eq = η/2  _[M]

    Substituting this ζ_eq for ζ in Eqs. (3.2.10) to (3.2.12) gives the system
    response. The resulting amplitude u0 and phase angle φ are shown by the
    dashed lines in Fig. 3.10.3. This approximate solution matches the exact
    result at ω = ωn because that was the criterion used in selecting ζ_eq.
    Over a wide range of excitation frequencies the approximate solution is
    seen to be accurate enough for many engineering applications. Thus Eq.
    (3.10.3) - which is difficult to solve for arbitrary force p(t) that
    contains many harmonic components of different frequencies ω - can be
    replaced by the simpler Eq. (3.2.1) for a system with equivalent viscous
    damping defined by Eq. (3.10.8). This is the basic advantage of equivalent
    viscous damping.
""")

rv.I("""Harmonic Vibration with Coulomb Friction | pdfpage

    Equation of Motion  _[B]

    Shown in Fig. 3.11.1 is a mass-spring system with Coulomb friction force F
    = μ*N that opposes sliding of the mass. As defined in Section 2.4, the
    coefficients of static and kinetic friction are assumed to be equal to μ,
    and N is the normal force across the sliding surfaces. The equation of
    motion is obtained by including the exciting force in Eqs. (2.4.1) and
    (2.4.2) governing the free vibration of the system:

    m*ü + k*u ± F = p(t) _[B]

    The sign of the friction force changes with the direction of motion; the
    positive sign applies if the motion is from left to right (u̇ > 0) and the
    negative sign is for motion from right to left (u̇ < 0). Each of the two
    differential equations is linear, but the overall problem is nonlinear
    because the governing equation changes every half-cycle of motion.
    Therefore, exact analytical solutions would not be possible except in
    special cases.

    Steady-State Response to Harmonic Force _[B]

    An exact analytical solution for the steady-state response of the system of
    Fig. 4 subjected to harmonic force was developed by J. P. Den Hartog in
    1933. 
    
    | IMAGE | img/fig_3.11.1.jpg | SDF Coulomb Damping, 70, num, not 

    The analysis is not included here, but his results are shown by solid
    lines in Fig. 5. The displacement amplitude u0, normalized relative to
    (u_st)0 = p0/k, and the phase angle φ are plotted as a function of the
    frequency ratio ω/ωn for three values of F/p0. If there is no friction, F =
    0 and u0/(u_st)0 = (Rd)_ζ=0, the same as in Eq. (3.1.11) for an undamped
    system. The friction force reduces the displacement amplitude u0, with the
    reduction depending on the frequency ratio ω/ωn.
    
    | IMAGE | img/fig_3.11.2.png |  Damping with Coulomb Friction, 70, num, not 

    _[[TEXT]] italic
    Deformation response factor and phase angle of a system
    with Coulomb friction excited by harmonic force. Exact solution from J. P.
    Den Hartog; approximate solution is based on equivalent viscous damping.    
    _[[END]]]

""")

rv.T("""Bibliography | endnotes

    Anil K.Anil K. Chopra, Dynamics of Structures: Theory and Applications to
    Earthquake Engineering. Englewood Cliffs, NJ, USA: Prentice Hall, 1995.

""")

rv.D("""Publish Doc 

    | PUBLISH | Rate Independent Damping | pdf
    
    _[[METADATA]] 
    [process]
    ;-----------------------------------------
    doc_verbose = true; if false minmize output during doc processing
    auto_cfg = true ; if false, config files are not updated from rivt file
    [doc]
    ;-----------------------------------------
    authors = R Holland
    version = 1.0.0a13
    repo = https://github.com/rivt-info/rivt-example-04
    license = https://opensource.org/license/mit/
    copyright = --
    fork1_authors = --
    fork1_version = --
    fork1_repo = --
    fork1_license = https://opensource.org/license/mit/
    [layout]
    ;----------------------- cover page and runner settings
    ;--- put logo files in /img folder of first chapter, size is % page width
    subtitle =  Seismic Isolation Bearing Design
    copyright = --
    client = Example 04 - rivtbook
    coverpage = false
    coverlogo_size = 30
    coverlogo = bearing1.png
    runninglogo = logo2.png
    runninglabel = rivt
    project_ref = proj. 0004
    ;------------------------ PDF settings
    ;--- colors: red, blue, green, black, gray, brown, maroon, gray, olive, cyan
    ;--- margins: top, right, bottom, left    page size: letter, legal, A4    
    pdf_link_color = brown
    pdf_link_underline = false
    pdf_pagesize = letter
    pdf_margins = 1in, 1in, 1in, 1in 
    ;----------------------- TOC levels
    ;--- 1: include subdivisions   2: include subdivisions and sections
    toc_level = 2
    _[[END]]    
""")

