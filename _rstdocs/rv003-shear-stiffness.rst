.. |s| unicode:: 0xA0 



.. |blklogo| image:: ./_static/logo1.png
   :height: 100px
   :alt: logo


    
.. header::
    .. list-table::
        :class: header-box
        :align: left
        :widths: 90 10
        
        * - **003 Shear Stiffness** - v1.0.0a12 |s| |s| |s| |s|  **###Section###**
          - p. **###Page###**   

          

.. footer:: 
    .. list-table::
        :class: footer-box
        :align: left
        :widths: 84 22 16
        
        * - 2026-06-30 |s| |s| |s| **|** |s| |s| |s| R Holland        
          - **rivt**        
          - |blklogo|


                  

.. role:: btext
   :class: big-text

.. role:: mtext
    :class: medium-text

.. role:: stext
    :class: small-text

|
|
|
|
        
.. image:: _static/bearing1.png
   :width: 30%
   :align: center

|
|
|
|
|

.. rst-class:: center

    :mtext:`Seismic Isolation Bearing Design`

|

.. rst-class:: center

    :btext:`003 Shear Stiffness`
    
|
|
|
|
|


.. rst-class:: center

    :mtext:`Example 04 - rivtbook`

|

.. rst-class:: center

    :stext:`proj. 0004`

   
.. raw:: pdf

   PageBreak noHead
      
**003 Shear Stiffness** - v1.0.0a12

--------------------

|

.. contents:: Table of Contents
  :depth: 2

  
.. raw:: pdf
 
   PageBreak mainPage
   SetPageCounter 1

 
.. raw:: pdf

   PageBreak

      


.. _Rubber Elastic Properties:

**0.3i** | Rubber Elastic Properties
================================================================================
 
 

**Table 1**: IRHD hardness scale (MN/m2)


 
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
 
 

**Table 2**: Shore A hardness scale (lbf/in2)


 
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
 


.. note::  

   #. The majority of springs are in the hardness range 40-60 IRHD.
   #. Theoretically, with a Poisson's ratio of 1/2, B should equal 3G. This is
      true for soft gum rubbers. For harder rubbers containing a fair proportion
      of non-rubber constituents, thixotropic and other effects increase 3G to
      about 4G.


 
 


-------------------------



.. _Shear Stiffness Example:

**0.3 - 2v** | Shear Stiffness Example
--------------------------------------------------------------------------------
 

**Table 3**: Bearing Specifications


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
 
**Bearing Stiffness for Circular Bearing**




|


**Eq. 1:**  rubber height

.. code-block:: text 

           rht = rnl⋅rthk

           rht = 20.40 inch     [rht] = 51.82 cm   | rubber height

           rthk             rnl
           ———————————————  ————————————————
           0.40 inch        51
           —————            —————
           layer thickness  number of rubber
           -                layers
           ———————————————  ————————————————




|


**Eq. 2:**  bearing height

.. code-block:: text 

           bht = rht + sthk⋅(rnl - 1)

           bht = 24.95 inch     [bht] = 63.37 cm   | bearing height

           rnl               sthk           rht
           ————————————————  —————————————  —————————————
           51                0.09 inch      20.40 inch
           —————             —————          —————
           number of rubber  11 guage shim  rubber height
           layers            thickness      -
           ————————————————  —————————————  —————————————




|


**Eq. 3:**  shear stiffness

.. code-block:: text 

                            2
                 G₁⋅cpi⋅rdia 
           Ks₁ = ────────────
                    4⋅rht    

           Ks₁ = 3.48 k_in     [Ks₁] = 6.10 kN_cm   | shear stiffness

           rht            rdia              cpi         G₁
           —————————————  ————————————————  ——————————  —————————————
           20.40 inch     39.50 inch        3.1418      58.00 p_si
           —————          —————             —————       —————
           rubber height  bearing diameter  contant pi  shear modulus
           —————————————  ————————————————  ——————————  —————————————


 
**Shape Factor for Circular Bearing**




|


**Eq. 4:**  shape factor 1

.. code-block:: text 

                    sdia 
           sh₁ ₁ = ──────
                   4⋅rthk

           sh₁ ₁ = 24     [sh₁ ₁] = 24   | shape factor 1

           rthk             sdia
           ———————————————  —————————————
           0 inch           38 inch
           —————            —————
           layer thickness  shim diameter
           ———————————————  —————————————




|


**Eq. 5:**  shape factor 2

.. code-block:: text 

                   bht 
           sh₂ ₁ = ────
                   rdia

           sh₂ ₁ = 1     [sh₂ ₁] = 1   | shape factor 2

           rdia              bht
           ————————————————  ——————————————
           40 inch           25 inch
           —————             —————
           bearing diameter  bearing height
           ————————————————  ——————————————


 
 
