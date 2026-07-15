
--------------------------------------------------------------------------------
| rivt | Compression Stiffness | R Holland | v-1.0.0a14 | 2026-07-15 - 11:19AM
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

=======  =========  ======
B₁       t₁         L₁
=======  =========  ======
12.0     0.25       24.0
—————    —————      —————
breadth  thickness  length
=======  =========  ======
 
For a block of square section (i.e. L = B) or circular section (diameter =
L):
 

┌  Eq-2 | shape factor
│
│           L₁ 
│     S₂ = ────
│          4⋅t₁
└

S₂ = 24.0    [S₂] = 24.0  | shape factor

=========  ======
t₁         L₁
=========  ======
0.25       24.0
—————      —————
thickness  length
=========  ======
 
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

=================  ============  ====================
k₁                 S₁            E₀
=================  ============  ====================
0.7                16.0          100.00 p_si
—————              —————         —————
adjustment factor  shape factor  compresssion modulus
=================  ============  ====================
 
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

=========  ====================  ===================
t₁         A₁                    Ec
=========  ====================  ===================
0.25 inch  20.00 in2             35940.00 p_si
—————      —————                 —————
thickness  cross-sectional area  compression modulus
=========  ====================  ===================
 
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
 
 
