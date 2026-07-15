#! python

import rivtlib.rvapi as rv

# %% rv.I(r"""Rubber Elastic Properties
rv.I(r"""Rubber Elastic Properties


    IRHD hardness scale (MN/m2) _[T]

    ==========  ===============  ==============  ====  ===============
    Hardness    Young's modulus  Shear modulus    k    Bulk modulus
    IRHD +/-2   E, MN/m2         G, MN/m2              B(inf), MN/m2
    ==========  ===============  ==============  ====  ===============
    30          0.92             0.30            0.93  1000
    35          1.18             0.37            0.89  1000
    40          1.50             0.45            0.85  1000
    45          1.80             0.54            0.80  1000
    50          2.20             0.64            0.73  1030
    55          3.25             0.81            0.64  1090
    60          4.45             1.06            0.57  1150
    65          5.85             1.37            0.54  1210
    70          7.35             1.73            0.53  1270
    75          9.40             2.22            0.52  1330
    ==========  ===============  ==============  ====  ===============


    Shore A hardness scale (lbf/in2) _[T]

    ============  ===============  ==============  ====  ===============
    Shore A       Young's modulus  Shear modulus     k    Bulk modulus
    (approx.)     lbf/in2          lbf/in2               lbf/in2
    ============  ===============  ==============  ====  ===============
    35            168              53              0.89  142 000
    45            256              76              0.80  142 000
    55            460              115             0.64  154 000
    65            830              195             0.54  171 000
    75            1340             317             0.52  189 000
    ============  ===============  ==============  ====  ===============

    _[[TEXT]] note
    #. The majority of springs are in the hardness range 40-60 IRHD.
    #. Theoretically, with a Poisson's ratio of 1/2, B should equal 3G. This is
       true for soft gum rubbers. For harder rubbers containing a fair proportion
       of non-rubber constituents, thixotropic and other effects increase 3G to
       about 4G.
    _[[END]]

""")

# %% rv.V(r"""Shear Stiffness Example
rv.V(r"""Shear Stiffness Example

    Bearing Specifications _[T]
    G_1 ==: 58 * p_si | p_si, MPA, 2 | shear modulus                                                    
    K_1 ==: 200000 * p_si | p_si, MPA, 2 | bulk modulus
    rnl ==: 51 | --, --, 0 |    number of rubber layers
    rdia ==: 39.5 * inch |  inch, cm, 2 | bearing diameter                                 
    rthk ==: .4 * inch | inch, cm, 2 |  layer thickness
    sdia ==: 38 * inch | inch, cm, 2 |  shim diameter                                                
    sthk ==: .091 * inch | inch, cm, 2 |  11 guage shim thickness
    cpi ==: 3.1418 | --, --, 0 | contant pi

    Bearing Stiffness for Circular Bearing _[B]
    rht <=: rnl * rthk | inch, cm, 2 | rubber height                               
    bht <=: rht + ((rnl-1) * sthk) | inch, cm, 2 | bearing height                 
    Ks_1 <=: ((G_1 * cpi * rdia**2 / (4 * rht)))| k_in, kN_cm, 2 | shear stiffness

    Shape Factor for Circular Bearing _[B] 
    sh1_1 <=: sdia / (4 * rthk) | --, --, 0 | shape factor 1                                    
    sh2_1 <=: bht / rdia | --, --, 0 | shape factor 2
    
""")

# %% rv.I(r"""shear 
rv.I(r"""shear 
    
        Natural Frequency

    The natural frequency (n_f) in Hz of a mounted body on a spring is

    n_f = 5 / sqrt(x)

    where x is the effective deflexion of the spring in centimetres. The
    effective deflexion is affected (and usually decreases) by the amplitude
    effect and by non-linear springs (Fig. 16).

    [Figure: fig16 _static_load_deformation_curve.png] Fig. 16.--OAB is a
    'static' load deformation curve. Its exact position and shape will depend
    on the amount of structure breakdown. The static stiffness at A is the
    slope of the tangent AC. When a dynamic, small amplitude deformation ED is
    superimposed on the static deformation at A its stiffness is the slope of
    AF. Thus the effective dynamic deformation FG is smaller than CG or OG, and
    the natural frequency will be higher than that predicted from static
    behaviour. C and F are generally closer to O than illustrated, especially
    with gum and lightly-filled natural rubber vulcanizates.

    [Figure: fig17_transmissibility_graph.png] Fig. 17.--The transmissibility
    of a natural rubber containing 40 parts by weight of carbon black.
    Temperature 19 degrees C. Experimental data of Snowdon, J. C., Brit. J.
    Appl. Phys, 1958, 9, 461-9. The full line is the theoretical relationship
    for no damping.

    Transmissibility

    Transmissibility (T) is the ratio of the amplitude of the vibration on the
    'protected' side of the spring to that of the disturbing vibration, or when
    the spring is on a rigid base, the ratio of the corresponding forces. T
    depends on the ratio of the disturbing frequency n to the natural frequency
    n_f of the mounted system (see above).

    Under normal operating conditions when n > 3*n_f natural rubber gives
    attenuation comparable with materials having no damping (Fig. 17). At
    resonance, when n = n_f, the small amount of damping in natural rubber
    prevents the peak value of T becoming excessive.

    Stiffness Characteristics

    A mathematical theory of rubber-like elasticity has been developed for
    elastic deformations of up to several hundred per cent. The theory applies
    strictly only to ideal rubbers, which are completely reversible,
    incompressible and isotropic, but in practice actual rubber springs have
    been shown to conform quite well. The behaviour of certain kinds of rubber
    spring may therefore be calculated for deformations of any practicable
    amount.

    However, when the deformation is complex, an exact solution may be
    unattainable. In some of these cases approximate relationships can be
    derived from the classical theory of elasticity. This theory, which is the
    basis of standard engineering practice, only applies to materials in which
    the strains are very small (a few per cent), but the errors introduced by
    extrapolation to strains of the order of 10-20% are not excessive. In the
    stiffness equations which follow, terms beyond the first have only been
    given where their contribution is likely to exceed the variability of the
    elastic constants. Calculated stiffnesses should be within +-15% of the
    actual stiffness in most cases; small adjustments can be obtained by slight
    changes of rubber hardness.

    In general, stiffness is particular to a given direction, the stiffnesses
    in other directions may sometimes be an order of magnitude different as,
    for example, in bridge bearings. By the suitable selection and location of
    two or more units the stiffness of a composite spring in three different
    directions can be varied independently. The design of such springs, of
    which the inclined shear mounting is a typical example, requires only a
    knowledge of mechanics and the principal stiffnesses of the units.

    SHEAR MOUNTING

    [Figure: fig18_shear_mounting.png]
    Fig. 18. Shear mounting.
""")


# %% rv.D(r"""Publish Doc
rv.D(r"""Publish Doc 

    | PUBLISH | Shear Stiffness | txt
    
    _[[METADATA]] 
    [process]
    ;-----------------------------------------
    doc_verbose = true; if false minmize output during doc processing
    auto_cfg = true ; if false, config files are not updated from rivt file
    [doc]
    ;-----------------------------------------
    authors = R Holland
    version = 1.0.0a14
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
    toc_level = 1
    _[[END]]    
    """)
