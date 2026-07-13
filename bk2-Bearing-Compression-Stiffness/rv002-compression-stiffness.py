import rivtlib.rvapi as rv

# %% rv.I("""Shape Factor 
rv.I("""Bearing Shape Factor 



    The stiffness of rubber in compression, when the loaded surfaces are
    prevented from slipping (by bonding or by mechanical location), depends
    upon the shape factor S (see Fig. 1), defined as the ratio of one loaded
    area to the total force-free area. _[#]

    | IMAGE | img/fig27.jpg | Shape Factor, 80, num, not 

    _[[TEXT]] italic
    Effect of shape factor: Experimental stress-strain curves for 6.3 mm thick
    disks of rubber (47 IRHD) in compression. The shape factor is shown
    alongside each curve; the diameter in mm is 25.4 times the shape factor.
    _[[END]]

    | IMAGE | img/fig28.png | Compression Modulus, 60, num, not 

    _[[TEXT]] italic
    Variation of compression modulus Ec with shape factor S for natural rubbers
    of differing hardnesses (SRF black filler used for 55 IRHD and above).
    Although deformation due to bulk compression can normally be ignored, it
    can cause a noticeable reduction in Ec when the ratio Ec/E∞ exceeds about
    10%. (E∞ is the modulus of bulk compression) To allow for
    this reduction, use a modified compression modulus obtained by dividing Ec
    by 1+(Ec/E∞). If Wood and Martin's value for bulk modulus is preferred  
    then the E∞ value in Table 3 should be doubled.
    _[[END]]

    Table 3  HARDNESS AND ELASTIC MODULI

    Based on experiments on natural rubber spring vulcanizates similar to A in Table 1 and
    containing (above 48 IRHD) SRF black as filler. Note that hardness is subject to an
    uncertainty of about +/-2 degrees.


    _[[TABLE]] IRHD hardness scale
    ====================  ===========================  ========================  ====  ===========================
    Hardness (IRHD +/-2)  Young's modulus E0 (MN/m^2)  Shear modulus G (MN/m^2)  k     Bulk modulus E_inf (MN/m^2)
    ====================  ===========================  ========================  ====  ===========================
    30                    0.92                         0.30                      0.93  1000
    35                    1.18                         0.37                      0.89  1000
    40                    1.50                         0.45                      0.85  1000
    45                    1.80                         0.54                      0.80  1000
    50                    2.20                         0.64                      0.73  1030
    55                    3.25                         0.81                      0.64  1090
    60                    4.45                         1.06                      0.57  1150
    65                    5.85                         1.37                      0.54  1210
    70                    7.35                         1.73                      0.53  1270
    75                    9.40                         2.22                      0.52  1330
    ====================  ===========================  ========================  ====  ===========================
    _[[END]]


    _[[TABLE]] Shore A hardness scale
    =================  ==========================  ========================  ====  =======================
    Shore A (approx.)  Young's modulus (lbf/in^2)  Shear modulus (lbf/in^2)  k     Bulk modulus (lbf/in^2)
    =================  ==========================  ========================  ====  =======================
    35                 168                         53                        0.89  142 000
    45                 256                         76                        0.80  142 000
    55                 460                         115                       0.64  154 000
    65                 830                         195                       0.54  171 000
    75                 1340                        317                       0.52  189 000
    =================  ==========================  ========================  ====  =======================
    _[[END]]]

    _[[TEXT]] topic
    Notes

    - k is used in the calculation of compression characteristics.

    - The majority of springs are in the hardness range 40-60 IRHD.

    - Average design limits: 15% compression, 50% shear.

    - Theoretically, with a Poisson's ratio of 1/2, E0 should equal 3G. This is
      so for soft gum rubbers, but for harder rubbers containing a fair
      proportion of non-rubber constituents, thixotropic and other effects
      increase E0 to about 4G.
    _[[END]]]

""")
    


# %% rv.V("""Block Compression Stiffness
rv.V("""Block Compression Stiffness

    Shape Factor Parameters _[T]
    t1 ==: .25 | inch, mm, 2 | thickness
    L1 ==: 24.0 | inch, mm, 2 | length
    B1 ==: 12.0 | inch, mm, 2 | breadth

    For a rectangualar section (length = L and breadth = B):
    
    S1 <=: L1 * B1 / (2*t1*(L1+B1)) | --, --, 2 | shape factor

    For a block of square section (i.e. L = B) or circular section (diameter = L):

    S2 <=: L1 / (4*t1) | --, --, 2 | shape factor

    The compression modulus Ec depends upon the shape factor S (for derivation
    see Section 5).

    Ec parameters _[T]
    E0 ==: 1*k_si | k_si, PA, 2 | compresssion modulus
    k1 ==: 150*k_si | k_si, PA, 2 | bulk modulus
    G1 ==: 0.5*k_si | k_si, PA, 2 | shear modulus

    E2 <=: E0*(1 + 2*k1*S1**2) | k_in, kN_cm, 2 | compression stiffness

    When S > 3 it may be more convenient to use:
    E3 <=: 5*G1*S1**2 | k_in, kN_cm, 2 | compression stiffness - modified

    | IMAGE | img/fig29.png | Compression Stiffness Kc, 80, num, not 

    Rubber block in compression. Diagram shows a rectangular rubber block of
    thickness t, deflecting by x under a compressive load F applied to a
    cylindrical rubber sample.

    The compression stiffness, Kc, is given by

    Kc = F/x = Ec*A/t

    where
    F = compressive load
    Ec = compression modulus (corrected, if necessary, for the effect of bulk compression)
    A = cross-sectional area
    t = thickness
    x = deflexion

    It is not advisable to rely on friction alone to prevent slip under a
    compressive load when using unbonded rubber parts, because slip may occur
    if S > μ/2, where S is the shape factor and μ the coefficient of friction.

    The load (F)—deflexion (x) curve of rubber in compression is non-linear.
    With no slip it has the approximate form

    F = Ec*A*e*(1+e)

    where e, the compressive strain, equals x/t. The non-linearity is usually
    ignored for strains up to about 10%.

    There is as yet no method of calculating that a block will be stable but
    experience has shown that provided the thickness is less than one-quarter
    of the least plan dimension there should be no instability.

""")


# %% rv.V("""Strip Analysis
rv.V("""Strip Compression Stiffness

    When a long strip of rubber is compressed the strain in the direction of
    its length will be negligible.

    Shape factor

    S = b / (2*t)

   | IMAGE | img/fig30.png | Compression Strip, 80, num, not 

    Diagram shows a long rectangular strip of rubber of width b, thickness t,
    and unit length, compressed by a load F applied per unit length.

    Compression modulus Ec

    Ec = 4*E0*(1 + k*S**2) / 3

    The compression stiffness per unit length, Kc, is given by

    Kc = F/x = Ec*b/t = (4*b*E0*(1 + k*S**2)) / (3*t)

    where
    F = load per unit length
    Ec = compression modulus (corrected, if necessary, for the effect of bulk compression)
    E0 = Young's modulus (from Table 3)
    b = width of strip
    t = thickness of strip
    x = deflexion
    k = a numerical factor (from Table 3)
    S = shape factor

    The load per unit length (F)—deflexion (x) curve for a compressed strip is
    non-linear. It has the approximate form

    F = Ec*b*e*(1 + 3*e/2)

    where e, the compressive strain, equals x/t. As in the case of blocks, the
    non-linearity is usually ignored for strains up to about 10%.

""")

# %% rv.I("""Derivation of Compression Characteristics 
rv.I("""Derivation of Compression Characteristics 

    Approximate load-deformation relations are derived below for small
    compressions of rubber blocks, between rigid plates to which they adhere or
    are bonded. The total displacements are considered to arise from the
    superposition of simple displacements, namely, (1) the pure homogeneous
    deformation defined by the displacement of one rigid bonding plate towards
    the other, and (2) the subsequent displacements necessary to cause points
    in the planes of the bonded surfaces to be restored to their original
    positions in these planes. _[#]

    Two extreme cases are considered, infinitely long rectangular blocks, the
    infinite dimension being at right angles to the direction of compression,
    and circular disks, loaded axially.

    Rectangular Blocks of Infinite Length

    The pure homogeneous deformation consists of a compressive strain e in the
    vertical direction, zero strain in the length direction, and an expansion
    in the width direction given, since the rubber is virtually incompressible
    in volume, by e also. The rubber is placed in a state of pure shear and the
    force F_1 which has to be applied to the bonded surfaces to maintain such a
    deformation is given by

    F_1 = 4*E_0*b*e/3     (1)

    per unit length, where E_0 is the Young's modulus of the rubber and b is
    the width of the block.

    The second displacement system is that causing points in the planes of the
    bonded surfaces to be restored to their original positions in these planes.
    In order to calculate the corresponding system of forces which has to be
    applied to the bonded surfaces, it is necessary to make the simplifying
    assumption that horizontal planes remain plane during the deformation, as
    seems probable when the width b is much greater than the thickness t.
    Vertical sections consequently take up parabolic forms, as represented
    diagrammatically in Fig. 41.

    The maximum outward displacement of any originally vertical section is
    dictated by the requirement that the volume contained between it and the
    central plane in the undeformed state shall equal the volume contained
    between it and the central plane when it takes up the parabolic form and
    the bonded surfaces approach by an amount delta( = e*t).

    For a plane at a distance x from the central vertical plane, considering
    unit length, we have

    x*t = x*(t - delta) + 2*u*t/3

    where 2*u*t/3 is the approximate volume contained between the parabolic
    front of maximum displacement u and the vertical plane at x, when the
    compression delta is small. Hence,

    u = 3*x*delta/(2*t)

    In an elementary section of width dx the small displacement u may be
    maintained by the action of an excess hydrostatic pressure dp acting on one
    curved face, where dp is given by the classical theory of elasticity in the
    form

    dp = -(8*E_0*u/(3*t**2))*dx     (2)

    Since the curved surface at x = b/2 is force free, p may be obtained by
    integrating both sides of equation (2) between the limits x = x and x =
    b/2, yielding

    p = 2*E_0*delta*(b**2/4 - x**2)/t**3

    The pressure p acts on the rigid bonded plates also. The corresponding
    force F_2 acting on each of these surfaces may be obtained by integrating
    such terms as p*dx between the limits x = b/2 and x = -b/2, to give

    F_2 = E_0*delta*b**3/(3*t**3)     (3)

    The apparent value of Young's modulus for the rubber block is given by

    E = (F/b)*(1/e)

    where F is the total force which has to be applied to the bonded surfaces
    per unit length to maintain the deformation, and is given by F_1 + F_2
    where F_1 and F_2 are given by equations (1) and (3) respectively. Hence,

    E = 4*E_0/3 + E_0*b**2/(3*t**2) = 4*E_0*(1 + S**2)/3     (4)

    where the shape factor S, the ratio of one loaded surface to the force-free
    surface, is equal to b/(2*t)

    [Figure: Fig. 41 -- Initial and deformed states for an infinitely long block subjected to a small compression. See image file "fig41_diagram.png".]

    Fig. 41.--Initial and deformed states for an infinitely long block subjected to a small compression.

    *From Appendix I of The Compression of Bonded Rubber Blocks, by A. N. Gent and P. B. Lindley, Proceedings of the Institution of Mechanical Engineers, 1959, Vol. 173, No. 3, pages 111-122.
    SOUTHWELL, R. V. 1941 'An Introduction to the Theory of Elasticity', p. 126 (Clarendon Press Oxford).
    ADKINS, J. E. 1954 Proc. Camb. phil. Soc., vol. 50, p. 334.

    45

    Circular Disks

    The apparent Young's modulus may be derived similarly for a circular disk. The force F_1 which must be applied to maintain the first deformation, a simple compression of amount e, is given by

    F_1 = E_0*pi*a**2*e

    where a is the radius of the disk.

    The force F_2 which has to be applied to maintain the second displacement system may be calculated by a similar procedure to that used in the previous example. Initially, vertical cylindrical surfaces are assumed to take up parabolic forms such that the volume contained within them is unchanged. When the compressive displacement delta is small, and the radius r is much greater than the maximum radial displacement u, then

    u = 3*r*delta/(4*t)

    where t is the thickness of the disk. The pressure p acting at a distance r from the centre is found to be

    p = E_0*delta*(a**2 - r**2)/t**3

    and hence the force F_2 is obtained as

    F_2 = pi*E_0*delta*a**4/(2*t**3)

    An analogous relation has been derived by Dienes and Klemm for the rate of approach of two parallel circular plates separated by a viscous liquid.

    The apparent Young's modulus E for a circular disc is obtained finally in the form

    E = E_0*(1 + a**2/(2*t**2)) = E_0*(1 + 2*S**2)     (5)

    where S, the ratio of one loaded surface to the force-free surface, is equal to a/(2*t).

    As the thickness of the block is increased, the terms in equations (4) and (5) representing the contribution F_2 to the total force decrease, so that when the condition on which the calculation for F_2 is based -- that the width or radius is much greater than the thickness -- becomes quite inapplicable, the contribution F_2 to the total force becomes relatively small. Equations (4) and (5) may therefore be expected to apply over a considerable range of thicknesses.

    NOTE: In practice it is necessary to multiply the S**2 term by the factor k, given in Table 3.

    DIENES, G. J. and KLEMM, H. F. 1946 J. Appl. Phys., vol. 17, p. 458.
    
""")

# %% rv.R("""Footnotes | endnotes
rv.R("""Footnotes | endnotes

    P.B. Lindley, Engineering Design with Natural Rubber, NR Technical Bulletin.
    Malaysian Rubber Producers' Research Association, Brickendonbury, U.K. 
    pages 26-28, 1959.
    
    P.B. Lindley, Engineering Design with Natural Rubber, NR Technical Bulletin.
    Malaysian Rubber Producers' Research Association, Brickendonbury, U.K. 
    pages 45-46, 1959.

""")

# %% rv.D("""Publish Doc 
rv.D("""Publish Doc 
    
    | PUBLISH | Compression Stiffness | txt
    
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