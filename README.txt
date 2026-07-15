
================================================================================
| rivtbook | Isolation Bearing Design v-1.0.0a13 | R Holland | 2026-07-15
================================================================================


rivtbook Table of Contents
===================================

001 - rivtbook Example - Introduction
002 - Compression Stiffness
003 - Shear Stiffness
004 - Viscous Damping
005 - Rate Independent Damping
006 - Three Story Vibration



--------------------------------------------------------------------------------
| rivt | rivtbook Example - Introduction | R Holland | v-1.0.0a13 | 2026-07-15 - 01:04AM
--------------------------------------------------------------------------------


0.1-1 | rivtbook Example
================================================================================
 
A rivtbook is a collection of rivt files with common subject matter that
may be published as a PDF or text report. Files are organized for selective
addition to rivt reports. Each chapter is contained within a folder
with an identifying name.
 
   bk1-chapter title            
    ├── data/                    
    ├── img/                        
    ├── scripts/
    └── rv001-book-chapter.py

 
A rivtbook chapter can be copied to a rivt report by copying the data, img
and scripts folders to the rvsrc report folder and the rivt file to the
rivt-report folder.
 
          ----------------------------------------
Fig. 1 - rivtbook chapter copied to a report [file: img/rvbk-rivt.jpg  ]
          ----------------------------------------

 
 


--------------------------------------------------------------------------------
| rivt | Compression Stiffness | R Holland | v-1.0.0a13 | 2026-07-15 - 01:04AM
--------------------------------------------------------------------------------


0.2-1 | Bearing Shape Factor
================================================================================
 
The stiffness of rubber in compression, when the loaded surfaces are
prevented from slipping by bonding or by mechanical location, depends
upon the shape factor S defined as the ratio of one loaded
area to the total force-free area (see Fig. 1). [0.2.1]
 
          ----------------------------------------
Fig. 1 - Shape Factor [file: img/fig27.jpg  ]
          ----------------------------------------

 
Effect of shape factor: Experimental stress-strain curves for 6.3 mm thick
disks of rubber (47 IRHD) in compression. The shape factor is shown
alongside each curve; the diameter in mm is 25.4 times the shape factor.

 
          ----------------------------------------
Fig. 2 - Compression Modulus [file: img/fig28.png  ]
          ----------------------------------------

 
Variation of compression modulus Ec with shape factor S for natural rubbers
of differing hardnesses (SRF black filler used for 55 IRHD and above).
Although deformation due to bulk compression can normally be ignored, it
can cause a noticeable reduction in Ec when the ratio Ec/E∞ exceeds about
10%. (E∞ is the modulus of bulk compression) To allow for
this reduction, use a modified compression modulus obtained by dividing Ec
by 1+(Ec/E∞). If Wood and Martin's value for bulk modulus is preferred  
then the E∞ value in Table 3 should be doubled.

 
Table 1: IRHD hardness scale (MN/m^2) (stored: t002-1.csv)
=========  ==================  ===============  ======  =====================
Hardness    Young's mod E0       Shear mod G     k       Bulk mod 
=========  ==================  ===============  ======  =====================
30           0.92                   0.30        0.93     1000
35           1.18                   0.37        0.89     1000
40           1.50                   0.45        0.85     1000
45           1.80                   0.54        0.80     1000
50           2.20                   0.64        0.73     1030
55           3.25                   0.81        0.64     1090
60           4.45                   1.06        0.57     1150
65           5.85                   1.37        0.54     1210
70           9.40                   2.22        0.52     1330
=========  ==================  ===============  ======  =====================

 
 
Table 2: Shore A hardness scale (lbf/in^2) (stored: t002-2.csv)
=========  ==================  =============== =======  =====================
Hardness    Young's mod E0       Shear mod G     k       Bulk mod 
=========  ==================  =============== =======  =====================
35         168                    53            0.89        142 000
45         256                    76            0.80        142 000
55         460                    115           0.64        154 000
65         830                    195           0.54        171 000
75         1340                   317           0.52        189 000
=========  ==================  =============== =======  =====================

 

- k is used in the calculation of compression characteristics.

- The majority of springs are in the hardness range 40-60 IRHD.

- Average design limits: 15% compression, 50% shear.

- Theoretically, with a Poisson's ratio of 1/2, E0 should equal 3G. This is
  so for soft gum rubbers, but for harder rubbers containing a fair
  proportion of non-rubber constituents, thixotropic and other effects
  increase E0 to about 4G.

- Based on experiments on natural rubber spring vulcanizates 
  containing (above 48 IRHD) SRF black as filler. Note that
  hardness is subject to an uncertainty of about +/-2 degrees.

 
 

0.2-2 | Block Compression Stiffness
--------------------------------------------------------------------------------
 

Table 3: Shape Factor Parameters
==========  =======  =========  =============
variable    value    [value]    description
==========  =======  =========  =============
t1          0.25     0.25       thickness
L1          24       24         length
B1          12       12         breadth
==========  =======  =========  =============
 
For a rectangualar section (length = L and breadth = B):
 

┌  Eq-1 | shape factor
│
│              B₁⋅L₁     
│     S₁ = ──────────────
│          2⋅t₁⋅(B₁ + L₁)
└

S₁ = 16.0    [S₁] = 16.0  | shape factor

=======  ======  =========
B₁       L₁      t₁
=======  ======  =========
12.0     24.0    0.25
—————    —————   —————
breadth  length  thickness
=======  ======  =========
 
For a block of square section (i.e. L = B) or circular section (diameter =
L):
 

┌  Eq-2 | shape factor
│
│           L₁ 
│     S₂ = ────
│          4⋅t₁
└

S₂ = 24.0    [S₂] = 24.0  | shape factor

======  =========
L₁      t₁
======  =========
24.0    0.25
—————   —————
length  thickness
======  =========
 
The compression modulus Ec depends upon the shape factor S (for derivation
see Section 5).
 

Table 4: Ec parameters
==========  ===========  =========  ====================
variable    value        [value]    description
==========  ===========  =========  ====================
E0          100.00 p_si  0.69 MPA   compresssion modulus
k1          0.7          0.7        adjustment factor
G1          0.50 k_si    3.45 MPA   shear modulus
==========  ===========  =========  ====================
 

┌  Eq-3 | compression modulus
│
│             ⎛    2       ⎞
│     Ec = E₀⋅⎝2⋅S₁ ⋅k₁ + 1⎠
└

Ec = 35.94 k_si    [Ec] = 247.80 MPA  | compression modulus

=================  ====================  ============
k₁                 E₀                    S₁
=================  ====================  ============
0.7                100.00 p_si           16.0
—————              —————                 —————
adjustment factor  compresssion modulus  shape factor
=================  ====================  ============
 
When S > 3 it may be more convenient to use:

┌  Eq-4 | compression stiffness - modified
│
│                  2
│     E1c = 5⋅G₁⋅S₁ 
└

E1c = 640.00 k_si    [E1c] = 4412.64 MPA  | compression stiffness - modified

=============  ============
G₁             S₁
=============  ============
0.50 k_si      16.0
—————          —————
shear modulus  shape factor
=============  ============
 
          ----------------------------------------
Fig. 3 - Compression Stiffness Kc [file: img/fig29.png  ]
          ----------------------------------------

 
 
The diagram shows a rectangular rubber block of thickness t, deflecting by x
under a compressive load F applied to a cylindrical rubber sample.
 
The compression stiffness Kc is given by:
┌  Eq-5 | 
│
│          F
│     Kc = ─
│          x
└


 

Table 5: Stiffness parameters
==========  =========  ============  ====================
variable    value      [value]       description
==========  =========  ============  ====================
A1          20.00 in2  12903.20 mm2  cross-sectional area
t1          0.25 inch  6.35 mm       thickness
x1          1.00 inch  25.40 mm      deflection
==========  =========  ============  ====================
 

┌  Eq-6 | compression stiffness
│
│          A₁⋅Ec
│     Kc = ─────
│           t₁  
└

Kc = 2875.20 k_in    [Kc] = 5035.25 kN_cm  | compression stiffness

====================  ===================  =========
A₁                    Ec                   t₁
====================  ===================  =========
20.00 in2             35940.00 p_si        0.25 inch
—————                 —————                —————
cross-sectional area  compression modulus  thickness
====================  ===================  =========
 
If S > μ/2, where S is the shape factor and μ the coefficient of friction,
slip may occur. In such cases, the rubber should be bonded to the rigid
 
The load (F)—deflexion (x) curve of rubber in compression is non-linear.
With no slip it has the approximate form
 
┌  Eq-7 | 
│
│     F = A⋅Ec⋅e⋅(e + 1)
└


 
where e, the compressive strain, equals x/t. The non-linearity is usually
ignored for strains up to about 10%.
 
There is as yet no method of calculating that a block will be stable but
experience has shown that provided the thickness is less than one-quarter
of the least plan dimension there should be no instability.
 
 

0.2-3 | Strip Compression Stiffness
--------------------------------------------------------------------------------
 
 
When a long strip of rubber is compressed the strain in the direction of
its length will be negligible.
 
Shape factor


 
┌  Eq-8 | 
│
│           b 
│     SF = ───
│          2⋅t
└


 
          ----------------------------------------
Fig. 4 - Compression Strip [file: img/fig30.png  ]
          ----------------------------------------

 
Diagram shows a long rectangular strip of rubber of width b, thickness t,
and unit length, compressed by a load F applied per unit length.
 
Compression modulus Ec
 
┌  Eq-9 | 
│
│               ⎛  2      ⎞
│          4⋅E₀⋅⎝SF ⋅k + 1⎠
│     Ec = ────────────────
│                 3        
└


 
The compression stiffness per unit length, Kc, is given by
 
┌  Eq-10 | 
│
│          F
│     Kc = ─
│          x
└


 
┌  Eq-11 | 
│
│          Ec⋅b
│     Kc = ────
│           t  
└


 
┌  Eq-12 | 
│
│                 ⎛  2      ⎞
│          4⋅E₀⋅b⋅⎝SF ⋅k + 1⎠
│     Kc = ──────────────────
│                 3⋅t        
└


 
F = load per unit length
Ec = compression modulus (corrected, if necessary, for the effect of bulk compression)
E0 = Young's modulus (from Table 3)
b = width of strip
t = thickness of strip
x = deflexion
k = a numerical factor (from Table 3)
SF = shape factor

 
The load per unit length (F)—deflexion (x) curve for a compressed strip is
non-linear. It has the approximate form
 
┌  Eq-13 | 
│
│                ⎛3⋅e    ⎞
│     F = Ec⋅b⋅e⋅⎜─── + 1⎟
│                ⎝ 2     ⎠
└


 
where e, the compressive strain, equals x/t. As in the case of blocks, the
non-linearity is usually ignored for strains up to about 10%.
 
 

0.2-4 | Derivation of Compression Characteristics
--------------------------------------------------------------------------------
 
Approximate load-deformation relations are derived below for small
compressions of rubber blocks, between rigid plates to which they adhere or
are bonded. The total displacements are considered to arise from the
superposition of simple displacements, namely, (14) the pure homogeneous
deformation defined by the displacement of one rigid bonding plate towards
the other, and (2) the subsequent displacements necessary to cause points
in the planes of the bonded surfaces to be restored to their original
positions in these planes. [0.2.2]
 
Two extreme cases are considered, infinitely long rectangular blocks, the
infinite dimension being at right angles to the direction of compression,
and circular disks, loaded axially.
 
Rectangular Blocks of Infinite Length _bold


 
The pure homogeneous deformation consists of a compressive strain e in the
vertical direction, zero strain in the length direction, and an expansion
in the width direction given, since the rubber is virtually incompressible
in volume, by e also. The rubber is placed in a state of pure shear and the
force F_1 which has to be applied to the bonded surfaces to maintain such a
deformation is given by
 
┌  Eq-14 | 
│
│          4⋅E₀⋅b⋅e
│     F₁ = ────────
│             3    
└


 
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
the bonded surfaces approach by an amount delta( = e*t). [0.2.3]
 
For a plane at a distance x from the central vertical plane, considering
unit length, we have
 
┌  Eq-15 | 
│
│           2⋅t⋅u             
│     t⋅x = ───── + x⋅(-δ + t)
│             3               
└


 
where 2ut/3 is the approximate volume contained between the parabolic
front of maximum displacement u and the vertical plane at x, when the
compression delta is small. Hence,
 
┌  Eq-16 | 
│
│         3⋅δ⋅x
│     u = ─────
│          2⋅t 
└


 
In an elementary section of width dx the small displacement u may be
maintained by the action of an excess hydrostatic pressure dp acting on one
curved face, where dp is given by the classical theory of elasticity in the
form
 
┌  Eq-17 | 
│
│             -8⋅E₀⋅u 
│     dp = dx⋅────────
│                  2  
│               3⋅t   
└


 
Since the curved surface at x = b/2 is force free, p may be obtained by
integrating both sides of equation (2) between the limits x = x and x =
b/2, yielding
 
┌  Eq-18 | 
│
│                ⎛ 2     ⎞
│                ⎜b     2⎟
│         2⋅E₀⋅δ⋅⎜── - x ⎟
│                ⎝4      ⎠
│     p = ────────────────
│                 3       
│                t        
└


 
The pressure p acts on the rigid bonded plates also. The corresponding
force F_2 acting on each of these surfaces may be obtained by integrating
such terms as p*dx between the limits x = b/2 and x = -b/2, to give
 
┌  Eq-19 | 
│
│              3  
│          E₀⋅b ⋅δ
│     F₂ = ───────
│              3  
│           3⋅t   
└


 
The apparent value of Young's modulus for the rubber block is given by
 
┌  Eq-20 | 
│
│           1   1
│     ℯ = F⋅─⋅1⋅─
│           b   e
└


 
where F is the total force which has to be applied to the bonded surfaces
per unit length to maintain the deformation, and is given by F_1 + F_2
where F_1 and F_2 are given by the equations. Hence,
 
┌  Eq-21 | 
│
│             2       
│         E₀⋅b    4⋅E₀
│     ℯ = ───── + ────
│            2     3  
│         3⋅t         
└


 
where the shape factor S, the ratio of one loaded surface to the force-free
surface, is equal to b/(2*t)
 
          ----------------------------------------
Fig. 5 - Initial and Deformed States [file: img/fig41.png  ]
          ----------------------------------------

 
Initial and deformed states for an infinitely long block
subjected to a small compression.

 
Circular Disks


 
The apparent Young's modulus may be derived similarly for a circular disk.
The force F_1 which must be applied to maintain the first deformation, a
simple compression of amount e, is given by [0.2.4]
 
┌  Eq-22 | 
│
│              2    
│     F₁ = E₀⋅a ⋅e⋅π
└


 
where a is the radius of the disk.
 
The force F_2 which has to be applied to maintain the second displacement
system may be calculated by a similar procedure to that used in the
previous example. Initially, vertical cylindrical surfaces are assumed to
take up parabolic forms such that the volume contained within them is
unchanged. When the compressive displacement delta is small, and the radius
r is much greater than the maximum radial displacement u, then
 
┌  Eq-23 | 
│
│         3⋅δ⋅r
│     u = ─────
│          4⋅t 
└


 
where t is the thickness of the disk. The pressure p acting at a distance r
from the centre is found to be
 
┌  Eq-24 | 
│
│              ⎛ 2    2⎞
│         E₀⋅δ⋅⎝a  - r ⎠
│     p = ──────────────
│                3      
│               t       
└


 
and hence the force F_2 is obtained as
 
┌  Eq-25 | 
│
│              4    
│          E₀⋅a ⋅δ⋅π
│     F₂ = ─────────
│               3   
│            2⋅t    
└


 
An analogous relation has been derived by Dienes and Klemm for the rate of
approach of two parallel circular plates separated by a viscous liquid.
 
The apparent Young's modulus E for a circular disc is obtained finally in
the form
 
┌  Eq-26 | 
│
│            ⎛  2     ⎞
│            ⎜ a      ⎟
│     ℯ = E₀⋅⎜──── + 1⎟
│            ⎜   2    ⎟
│            ⎝2⋅t     ⎠
└


 
where S, the ratio of one loaded surface to the force-free surface, is
equal to a/(2*t).
 
As the thickness of the block is increased, the termsrepresenting the
contribution F_2 to the total force decrease, so that when the condition on
which the calculation for F_2 is based -- that the width or radius is much
greater than the thickness -- becomes inapplicable. The contribution
F_2 to the total force becomes relatively small. The equations may
therefore be expected to apply over a considerable range of thicknesses.
 
NOTE: In practice it is necessary to multiply the S2 term by the factor
k, given in Table 1. [0.2.5]
 
 


--------------------------------------------------------------------------------
| rivt | Shear Stiffness | R Holland | v-1.0.0a13 | 2026-07-15 - 01:04AM
--------------------------------------------------------------------------------


0.3-1 | Rubber Elastic Properties
================================================================================
 
 

Table 1: IRHD hardness scale (MN/m2)
 
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
 
 

Table 2: Shore A hardness scale (lbf/in2)
 
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
 
#. The majority of springs are in the hardness range 40-60 IRHD. #.
Theoretically, with a Poisson's ratio of 1/2, B should equal 3G. This is    true
for soft gum rubbers. For harder rubbers containing a fair proportion    of non-
rubber constituents, thixotropic and other effects increase 3G to    about 4G.


 
 

0.3-2 | Shear Stiffness Example
--------------------------------------------------------------------------------
 

Table 3: Bearing Specifications
==========  ==============  ===========  =======================
variable    value           [value]      description
==========  ==============  ===========  =======================
G_1         58.00 p_si      0.40 MPA     shear modulus
K_1         200000.00 p_si  1378.95 MPA  bulk modulus
rnl         51              51           number of rubber layers
rdia        39.50 inch      100.33 cm    bearing diameter
rthk        0.40 inch       1.02 cm      layer thickness
sdia        38.00 inch      96.52 cm     shim diameter
sthk        0.09 inch       0.23 cm      11 guage shim thickness
cpi         3.1418          3.1418       contant pi
==========  ==============  ===========  =======================
 
Bearing Stiffness for Circular Bearing



┌  Eq-1 | rubber height
│
│     rht = rnl⋅rthk
└

rht = 20.40 inch    [rht] = 51.82 cm  | rubber height

===============  ================
rthk             rnl
===============  ================
0.40 inch        51
—————            —————
layer thickness  number of rubber
-                layers
===============  ================

┌  Eq-2 | bearing height
│
│     bht = rht + sthk⋅(rnl - 1)
└

bht = 24.95 inch    [bht] = 63.37 cm  | bearing height

=============  ================  =============
sthk           rnl               rht
=============  ================  =============
0.09 inch      51                20.40 inch
—————          —————             —————
11 guage shim  number of rubber  rubber height
thickness      layers            -
=============  ================  =============

┌  Eq-3 | shear stiffness
│
│                      2
│           G₁⋅cpi⋅rdia 
│     Ks₁ = ────────────
│              4⋅rht    
└

Ks₁ = 3.48 k_in    [Ks₁] = 6.10 kN_cm  | shear stiffness

==========  ================  =============  =============
cpi         rdia              G₁             rht
==========  ================  =============  =============
3.1418      39.50 inch        58.00 p_si     20.40 inch
—————       —————             —————          —————
contant pi  bearing diameter  shear modulus  rubber height
==========  ================  =============  =============
 
Shape Factor for Circular Bearing



┌  Eq-4 | shape factor 1
│
│              sdia 
│     sh₁ ₁ = ──────
│             4⋅rthk
└

sh₁ ₁ = 24    [sh₁ ₁] = 24  | shape factor 1

===============  =============
rthk             sdia
===============  =============
0 inch           38 inch
—————            —————
layer thickness  shim diameter
===============  =============

┌  Eq-5 | shape factor 2
│
│             bht 
│     sh₂ ₁ = ────
│             rdia
└

sh₂ ₁ = 1    [sh₂ ₁] = 1  | shape factor 2

================  ==============
rdia              bht
================  ==============
40 inch           25 inch
—————             —————
bearing diameter  bearing height
================  ==============
 
 

0.3-3 | shear
--------------------------------------------------------------------------------
 
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



--------------------------------------------------------------------------------
| rivt | Rate Independent Damping | R Holland | v-1.0.0a13 | 2026-07-15 - 01:04AM
--------------------------------------------------------------------------------


0.5-1 | Rate Independent Damping
================================================================================
 
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
energy. [0.5.1]
 
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
 
┌  Eq-1 | 
│
│          k⋅u̇⋅η
│     fD = ─────
│            ω  
└


 
where k is the stiffness of the structure and η is a damping coefficient.
The energy dissipated by this type of damping in a cycle of vibration at
frequency ω is independent of ω (Fig. 3.10.1). It is given by Eq. (3.8.1)
with c replaced by η*k/ω:
 
┌  Eq-2 | 
│
│              2    
│     ED = k⋅u₀ ⋅η⋅π
└


 
In contrast, the energy dissipated in viscous damping increases linearly
with the forcing frequency, as shown in Fig. 1.
 
          ----------------------------------------
Fig. 1 - Viscous and Rate Independent Damping [file: img/fig3-10-1.jpg  ]
          ----------------------------------------

 
Rate-independent damping is easily described if the excitation is harmonic
and we are interested only in the steady-state response of this system.
Difficulties arise in translating this damping mechanism back to the time
domain. Thus it is most useful in the frequency-domain method of analysis
(Section 1.10.3). The complex term k(1 + iη)*u represents both the
elastic and damping forces at the same time; k(1 + iη) is the complex
stiffness of the system. There are advantages in this terminology if the
reader is familiar with complex-variable notation. The complex stiffness
has no physical meaning, however, in the same engineering sense as the
elastic stiffness.
 
 

0.5-2 | Steady-State Response to Harmonic Force
--------------------------------------------------------------------------------
 
The equation for an SDF system with rate-independent linear damping,
denoted by a crossed box in Fig. 3.10.2, is Eq. (3.2.1) with the damping
term replaced by Eq. (3.10.1):
 
┌  Eq-3 | 
│
│           k⋅u̇⋅η             
│     k⋅u + ───── + m⋅ü = p(t)
│             ω               
└


 
The mathematical solution of this equation is quite complex for arbitrary
p(t). Here we consider only the steady-state motion due to a sinusoidal
forcing function, p(t) = p0sin(ωt), which is described by
 
┌  Eq-4 | 
│
│     u(t) = u₀⋅sin(t⋅ω - φ)
└


 
The amplitude u0 and phase angle φ are
 
┌  Eq-5 | 
│
│                            1            
│     u₀ = uₛₜ⋅1⋅─────────────────────────
│                      ___________________
│                     ╱                 2 
│                    ╱       ⎛        2⎞  
│                   ╱    2   ⎜    ⎛ω ⎞ ⎟  
│                  ╱    η  + ⎜1 - ⎜──⎟ ⎟  
│                ╲╱          ⎝    ⎝ωn⎠ ⎠  
└


 
┌  Eq-6 | 
│
│               ⎛    η    ⎞
│     φ = arctan⎜─────────⎟
│               ⎜        2⎟
│               ⎜    ⎛ω ⎞ ⎟
│               ⎜1 - ⎜──⎟ ⎟
│               ⎝    ⎝ωn⎠ ⎠
└


 
These results are obtained by modifying the viscous damping ratio in Eqs.
(3.2.11) and (3.2.12) to reflect the damping force associated with
rate-independent damping, Eq. (3.10.1). In particular, ζ was replaced by
 
┌  Eq-7 | 
│
│          c 
│     ζ = ───
│         c_c
└


 
┌  Eq-8 | 
│
│           k⋅η   
│     ζ = ────────
│         ω⋅2⋅m⋅ωn
└


 
┌  Eq-9 | 
│
│           η  
│     ζ = ─────
│         ⎛2⋅ω⎞
│         ⎜───⎟
│         ⎝ωn ⎠
└


 
Shown in Fig 3 by solid lines are plots of u0/(u_st)0 and φ as a
function of the frequency ratio ω/ωn for damping coefficient η = 0, 0.2,
and 0.4; the dashed lines are described in the next section. Comparing
these results with those in Fig. 3.2.6 for viscous damping, two differences
are apparent: First, resonance (maximum amplitude) occurs at ω = ωn, not at
ω < ωn. Second, the phase angle for ω = 0 is φ = arctan(η) instead of zero
for viscous damping; this implies that motion with rate-independent damping
can never be in phase with the forcing function.
 
          ----------------------------------------
Fig. 2 - SDF Rate Independent Linear Damping [file: img/fig_3.10.2.jpg  ]
          ----------------------------------------

 
These differences between forced vibration with rate-independent damping
and forced vibration with viscous damping are not significant, but they are
the source of some difficulty in reconciling physical data. In most damped
vibration, damping is not viscous, and to assume that it is without knowing
its real physical characteristics is an assumption of some error. In the
next section this error is shown to be small when the real damping is rate
independent.
 
          ----------------------------------------
Fig. 3 - Rate Independent Damping [file: img/fig_3.10.3.png  ]
          ----------------------------------------

 
 

0.5-3 | Solution Using Equivalent Viscous Damping
--------------------------------------------------------------------------------
 
In this section an approximate solution for the steady-state harmonic
response of a system with rate-independent damping is obtained by modeling
this damping mechanism as equivalent viscous damping.
 
Matching dissipated energies at ω = ωn (Fig. 3.10.1) led to Eq. (3.9.2),
where ED is given by Eq. (3.10.2), leading to the equivalent viscous
damping ratio:
 
┌  Eq-10 | 
│
│            η
│     ζ_eq = ─
│            2
└


 
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
 

0.5-4 | Harmonic Vibration with Coulomb Friction
--------------------------------------------------------------------------------
 
Equation of Motion


 
Shown in Fig. 3.11.1 is a mass-spring system with Coulomb friction force F
= μ*N that opposes sliding of the mass. As defined in Section 2.4, the
coefficients of static and kinetic friction are assumed to be equal to μ,
and N is the normal force across the sliding surfaces. The equation of
motion is obtained by including the exciting force in Eqs. (2.4.1) and
(2.4.2) governing the free vibration of the system:
 
m*ü + k*u ± F = p(t)


 
The sign of the friction force changes with the direction of motion; the
positive sign applies if the motion is from left to right (u̇ > 0) and the
negative sign is for motion from right to left (u̇ < 0). Each of the two
differential equations is linear, but the overall problem is nonlinear
because the governing equation changes every half-cycle of motion.
Therefore, exact analytical solutions would not be possible except in
special cases.
 
Steady-State Response to Harmonic Force


 
An exact analytical solution for the steady-state response of the system of
Fig. 4 subjected to harmonic force was developed by J. P. Den Hartog in
1933.
 
          ----------------------------------------
Fig. 4 - SDF Coulomb Damping [file: img/fig_3.11.1.jpg  ]
          ----------------------------------------

 
The analysis is not included here, but his results are shown by solid
lines in Fig. 5. The displacement amplitude u0, normalized relative to
(u_st)0 = p0/k, and the phase angle φ are plotted as a function of the
frequency ratio ω/ωn for three values of F/p0. If there is no friction, F =
0 and u0/(u_st)0 = (Rd)_ζ=0, the same as in Eq. (3.1.11) for an undamped
system. The friction force reduces the displacement amplitude u0, with the
reduction depending on the frequency ratio ω/ωn.
 
          ----------------------------------------
Fig. 5 - Damping with Coulomb Friction [file: img/fig_3.11.2.png  ]
          ----------------------------------------

 
Deformation response factor and phase angle of a system
with Coulomb friction excited by harmonic force. Exact solution from J. P.
Den Hartog; approximate solution is based on equivalent viscous damping.    

 
 


--------------------------------------------------------------------------------

[0.5.1] Anil K.Anil K. Chopra, Dynamics of Structures: Theory and Applications
toEarthquake Engineering. Englewood Cliffs, NJ, USA: Prentice Hall, 1995.



--------------------------------------------------------------------------------
| rivt | Three Story Vibration | R Holland | v-1.0.0a13 | 2026-07-15 - 01:04AM
--------------------------------------------------------------------------------


0.6-1 | Eigenvalues and Vectors
================================================================================
 
Analyze a 3-story shear frame using the flexibility method to determine
natural frequencies and mode shapes (fter Clough and Penzien [0.6.1])
 
          ----------------------------------------
Fig. 1 - Structural Model [file: img/frames.jpg  ]
          ----------------------------------------

 
import numpy as np
import numpy.linalg as la
import textwrap as tw
# set up mass and stiffness arrays
m = np.array([[1.0,0,0],[0,1.5,0],[0,0,2.0]],float)        
k1 = 600*np.array([[1,-1,0.0],[-1,3,-2],[0,-2,5]],float)   
# flexibility and dynamic matrix
f = la.inv(k1)                                            
d = np.inner(f,m)                                         
eigen = la.eig(d)                                         
evalus = eigen[0]
print("\neigenvalues:\n"," "*8,evalus)

eigenvalues:
          [0.00474206 0.00103739 0.00047055]
#
nat_freq = 1/(np.sqrt(evalus))
print("\nnatural frequencies:\n"," "*8,nat_freq)                                           

natural frequencies:
          [14.52166783 31.04769646 46.09947622]
#
evect = np.array(eigen[1])                                
print("\neigenvectors:\n",tw.indent(str(evect), " "*8))

eigenvectors:
         [[-0.81332769 -0.73942881  0.27304451]
         [-0.52747169  0.44853685 -0.69406171]
         [-0.24550292  0.50205551  0.66612689]]
 
 

0.6-2 | Plot Mode Shapes
--------------------------------------------------------------------------------
 
          ----------------------------------------
Fig. 2 - Structural Model [file: img/modes.jpg  ]
          ----------------------------------------

 
Plot normalized mode shapes and compare to Penzien and Clough. [0.6.2]
 
import numpy as np
import matplotlib.pyplot as plt
import os
from tabulate import tabulate as tb
# initialize eigenvector array (need (x,1) shapes for plotting
ms = np.shape(evect)
zz = np.zeros((ms[0],1))
x1=np.concatenate((evect,zz),1)
#plot mode shapes using matplotlib
y=np.array([0,1,2,3])
m3=x1[2]*.35+5
m2=x1[1]*.35+3
m1=x1[0]*.35+1
m=np.concatenate((m1,m2,m3))
plt.clf()
plt.plot(m1,y)
plt.plot(m2,y)
plt.plot(m3,y)
plt.xlim(.5,6.)
plt.xlabel('mode')
plt.ylabel('levels')
plt.title("Mode Shapes")
plt.grid()
curdir=os.getcwd()
imgdir=os.path.join(curdir,"img","mode_shapes.png")
plt.savefig(imgdir)
# table of eigenvalues and normalized eigenvectors
evectt = np.transpose(evect)     
for i in range(len(nat_freq)):
     evectt[i] = evectt[i]/evectt[i][0] 
xx = np.concatenate((nat_freq[:, np.newaxis],evect),1)                          
xx = np.round(xx, 4)
yy = ["freq","level 3","level 2","level 1"]                   
tt = np.vstack((yy,xx))
print("\nTable of eigenvalues and normalized eigenvectors\n",
tb(tt, headers="firstrow", tablefmt="rst"))    

Table of eigenvalues and normalized eigenvectors
 =======  =========  =========  =========
   freq    level 3    level 2    level 1
=======  =========  =========  =========
14.5217     1          1          1
31.0477     0.6485    -0.6066    -2.5419
46.0995     0.3018    -0.679      2.4396
=======  =========  =========  =========
 
          ----------------------------------------
Fig. 3 - Calculated Normalized Modes [file: img/mode_shapes.png  ]
          ----------------------------------------

 
 


--------------------------------------------------------------------------------

[0.6.1] R.W. Clough and J. Penzien, Dynamics of Structures. New York, NY,
USA:McGraw-Hill, 1975. pg. 178-180

[0.6.2] ibid. pg. 180-182


