 
.. raw:: pdf

   PageBreak

      


.. _Eigenvalues and Vectors:

**0.6-1** | Eigenvalues and Vectors
================================================================================]
 
Analyze a 3-story shear frame using the flexibility method to determine
natural frequencies and mode shapes (after Clough and Penzien  `[0.6.1]`_ )
The model can be used to analyze a two story isolated structure
by modeling the first story stiffness and mass
as the isolated foundation system. In this example, the model
is calibrated to reproduce the Clough example.
 

.. figure:: C:/git/rivtbk-example-04-git/bk6-System-Period/image/frames.jpg
   :width: 70%
   :align: center

   **Fig. 1.1** - Structural Model   
    


 
Normalized mode shapes are calculated and compared to Penzien and 
Clough.  `[0.6.2]`_ 
 

.. figure:: C:/git/rivtbk-example-04-git/bk6-System-Period/image/modes.jpg
   :width: 70%
   :align: center

   **Fig. 1.2** - Mode Shapes from Clough   
    


 


-------------------------



.. _Eigen Script:

**0.6-2** | Eigen Script
--------------------------------------------------------------------------------

.. code-block:: python

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
   #
   #                eigenvalues
   print(" "*8,evalus)
            [0.00474206 0.00103739 0.00047055]
   #
   nat_freq = 1/(np.sqrt(evalus))
   #
   #                natural frequencies
   print(" "*8,nat_freq)
            [14.52166783 31.04769646 46.09947622]
   #
   evect = np.array(eigen[1])                                
   #
   #               eigenvectors
   print(tw.indent(str(evect), " "*8))
           [[-0.81332769 -0.73942881  0.27304451]
            [-0.52747169  0.44853685 -0.69406171]
            [-0.24550292  0.50205551  0.66612689]]



-------------------------



.. _Plot Script:

**0.6-3** | Plot Script
--------------------------------------------------------------------------------

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   import os
   from tabulate import tabulate as tb
   # initialize eigenvector array (need (x,1) shapes for plotting
   ms = np.shape(evect)
   zz = np.zeros((ms[0],1))
   x1=np.concatenate((evect,zz),1)
   # plot mode shapes using matplotlib
   y=np.array([0,1,2,3])
   m3=x1[2]*.75+5
   m2=x1[1]*.75+3
   m1=x1[0]*.75+1.5
   m=np.concatenate((m1,m2,m3))
   plt.clf()
   plt.plot(m1,y)
   plt.plot(m2,y)
   plt.plot(m3,y)
   plt.xlim(.5,6.)
   plt.xlabel("mode")
   plt.ylabel("levels")
   plt.title("Mode Shapes")
   plt.grid()
   curdir=os.getcwd()
   imgdir=os.path.join(curdir,"image","mode_shapes.png")
   plt.savefig(imgdir)
   # table of eigenvalues and normalized eigenvectors
   evectt = np.transpose(evect)     
   for i1 in range(len(nat_freq)):
        evectt[i1] = evectt[i1]/evectt[i1][0] 
   v1 = np.concatenate((nat_freq[:, np.newaxis],evect),1)                          
   v2 = np.round(v1, 4)
   h1 = ["freq","level 3","level 2","level 1"]                   
   tb1 = np.vstack((h1,v2))
   #               Table of eigenvalues and normalized eigenvectors
   print(tb(tb1, headers="firstrow", tablefmt="rst"))
   =======  =========  =========  =========
      freq    level 3    level 2    level 1
   =======  =========  =========  =========
   14.5217     1          1          1
   31.0477     0.6485    -0.6066    -2.5419
   46.0995     0.3018    -0.679      2.4396
   =======  =========  =========  =========



-------------------------



.. raw:: pdf

   PageBreak



.. _Plot Mode Shapes:

**0.6-4** | Plot Mode Shapes
--------------------------------------------------------------------------------
 

.. rst-class:: align-right

   **blue:** mode 1


.. rst-class:: align-right

   **red:** mode 2


.. rst-class:: align-right

   **green:** mode 3


.. figure:: C:/git/rivtbk-example-04-git/bk6-System-Period/image/mode_shapes.png
   :width: 90%
   :align: center

   **Fig. 4.1** - Calculated Normalized Modes   
    


 
 

--------------------


.. _[0.6.1]:

**[0.6.1]** 
    R.W. Clough and J. Penzien, Dynamics of Structures. New York, NY, USA:McGraw-Hill, 1975. pg. 178-180





.. _[0.6.2]:

**[0.6.2]** 
    ibid. pg. 180-182




 
 
