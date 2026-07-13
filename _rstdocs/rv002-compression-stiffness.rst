.. |s| unicode:: 0xA0 



.. |blklogo| image:: ./_static/logo2.png
   :height: 100px
   :alt: logo


    
.. header::
    .. list-table::
        :class: header-box
        :align: left
        :widths: 90 10
        
        * - **Compression Stiffness** - v1.0.0a13 |s| |s| |s| |s|  **###Section###**
          - p. **###Page###**   

          

.. footer:: 
    .. list-table::
        :class: footer-box
        :align: left
        :widths: 84 22 16
        
        * - 2026-07-12 |s| |s| |s| **|** |s| |s| |s| R Holland        
          - **rivt**        
          - |blklogo|


                  

.. raw:: pdf

   PageBreak noHead
      
**Compression Stiffness** - v1.0.0a13

--------------------

|

.. contents:: Table of Contents
  :depth: 2

  
.. raw:: pdf
 
   PageBreak mainPage
   SetPageCounter 1

 
.. raw:: pdf

   PageBreak

      


.. _Bearing Shape Factor:

**0.2** | Bearing Shape Factor
================================================================================
 
 
 
The stiffness of rubber in compression, when the loaded surfaces are
prevented from slipping (by bonding or by mechanical location), depends
upon the shape factor S (see Fig. 1), defined as the ratio of one loaded
area to the total force-free area.  `[0.2.1]`_ 
 

.. figure:: c:/git/rivtbk-example-04-git/bk2-Bearing-Compression-Stiffness/img/fig27.jpg
   :width: 80%
   :align: center

   **Fig. 1** - Shape Factor   
    


 


       *Effect of shape factor: Experimental stress-strain curves for 6.3 mm thick
       disks of rubber (47 IRHD) in compression. The shape factor is shown
       alongside each curve; the diameter in mm is 25.4 times the shape factor.*


 

.. figure:: c:/git/rivtbk-example-04-git/bk2-Bearing-Compression-Stiffness/img/fig28.png
   :width: 60%
   :align: center

   **Fig. 2** - Compression Modulus   
    


 


       *Variation of compression modulus Ec with shape factor S for natural rubbers
       of differing hardnesses (SRF black filler used for 55 IRHD and above).
       Although deformation due to bulk compression can normally be ignored, it
       can cause a noticeable reduction in Ec when the ratio Ec/E∞ exceeds about
       10%. (E∞ is the modulus of bulk compression) To allow for
       this reduction, use a modified compression modulus obtained by dividing Ec
       by 1+(Ec/E∞). If Wood and Martin's value for bulk modulus is preferred  
       then the E∞ value in Table 3 should be doubled.*


 
 


-------------------------



.. _Compression Stiffness of Blocks:

**0.2 - 2** | Compression Stiffness of Blocks
--------------------------------------------------------------------------------
 
S = (LB) / (2t*(L+B))
 
S = shape factor
t = thickness
L = length
B = breadth
 
For a block of square section (i.e. L = B) or circular section (diameter = L):
 
S = L / (4*t)
 
The compression modulus Ec depends upon the shape factor S (for derivation
see Appendix).
 
Ec = E0(1 + 2kS2)
 
Ec = compression modulus
E0 = Young's modulus (from Table 3)
S = shape factor
k = a numerical factor (from Table 3)
 
See footnote on following page.
 
When S > 3 it may be more convenient to use
 
Ec ≈ 5GS2
 
where G is the shear modulus (from Table 3).
 

.. figure:: c:/git/rivtbk-example-04-git/bk2-Bearing-Compression-Stiffness/img/fig29.png
   :width: 80%
   :align: center

   **Fig. 3** - Compression Stiffness Kc   
    


 
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
 
F = EcAe*(1+e)
 
where e, the compressive strain, equals x/t. The non-linearity is usually
ignored for strains up to about 10%.
 
There is as yet no method of calculating that a block will be stable but
experience has shown that provided the thickness is less than one-quarter
of the least plan dimension there should be no instability.
 
 


-------------------------



.. _Compression Stiffness of Strips:

**0.2 - 3** | Compression Stiffness of Strips
--------------------------------------------------------------------------------
 
COMPRESSION STRIP
 
When a long strip of rubber is compressed the strain in the direction of
its length will be negligible.
 
Shape factor
 
S = b / (2*t)
 
 IMAGE | img/fig30.png | Compression Strip, 80, num, not 
 
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
 
 


--------------------


.. _[0.2.1]:

**[0.2.1]** 
    P.B. Lindley, Engineering Design with Natural Rubber, NR Technical Bulletin.Malaysian Rubber Producers' Research Association, Brickendonbury, U.K.



