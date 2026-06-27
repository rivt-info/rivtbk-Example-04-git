
--------------------------------------------------------------------------------
| rivt | 103 Shear Stiffness | R Holland | v-1.0.0a12 | 2026-06-26 - 01:56AM
--------------------------------------------------------------------------------


1.3 | Rubber Elastic Properties
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


 
 

1.3 - 2 | Shear Stiffness Example
--------------------------------------------------------------------------------
 

Table 3: Bearing Specifications
==========  ================  ===========  =======================
variable    value             [value]      description
==========  ================  ===========  =======================
G_1         58.00 lb_in2      0.40 MPA     shear modulus
K_1         200000.00 lb_in2  1378.95 MPA  bulk modulus
rnl         51                51           number of rubber layers
rdia        39.50 inch        100.33 cm    bearing diameter
rthk        0.40 inch         1.02 cm      layer thickness
sdia        38.00 inch        96.52 cm     shim diameter
sthk        0.09 inch         0.23 cm      11 guage shim thickness
cpi         3.1418            3.1418       contant pi
==========  ================  ===========  =======================
 
Bearing Stiffness for Circular Bearing



┌  Eq-1 | rubber height
│
│     rht = rnl⋅rthk
└

rht = 20.40 inch    [rht] = 51.82 cm  | rubber height

=======================  ===============
rnl                      rthk
=======================  ===============
51                       0.40 inch
—————                    —————
number of rubber layers  layer thickness
=======================  ===============

┌  Eq-2 | bearing height
│
│     bht = rht + sthk⋅(rnl - 1)
└

bht = 24.95 inch    [bht] = 63.37 cm  | bearing height

=======================  =============  =======================
rnl                      rht            sthk
=======================  =============  =======================
51                       20.40 inch     0.09 inch
—————                    —————          —————
number of rubber layers  rubber height  11 guage shim thickness
=======================  =============  =======================

┌  Eq-3 | shear stiffness
│
│                      2
│           G₁⋅cpi⋅rdia 
│     Ks₁ = ────────────
│              4⋅rht    
└

Ks₁ = 3.48 k_i    [Ks₁] = 6.10 kN_cm  | shear stiffness

=============  ================  ==========  =============
rht            rdia              cpi         G₁
=============  ================  ==========  =============
20.40 inch     39.50 inch        3.1418      58.00 lb_in2
—————          —————             —————       —————
rubber height  bearing diameter  contant pi  shear modulus
=============  ================  ==========  =============
 
Shape Factor for Circular Bearing



┌  Eq-4 | shape factor 1
│
│              sdia 
│     sh₁ ₁ = ──────
│             4⋅rthk
└

sh₁ ₁ = 24    [sh₁ ₁] = 24  | shape factor 1

=============  ===============
sdia           rthk
=============  ===============
38 inch        0 inch
—————          —————
shim diameter  layer thickness
=============  ===============

┌  Eq-5 | shape factor 2
│
│             bht 
│     sh₂ ₁ = ────
│             rdia
└

sh₂ ₁ = 1    [sh₂ ₁] = 1  | shape factor 2

==============  ================
bht             rdia
==============  ================
25 inch         40 inch
—————           —————
bearing height  bearing diameter
==============  ================
 
 
