import rivtlib.rvapi as rv

# %% rv.I("""System Period
rv.V("""Eigenvalues and Vectors

    Analyze a 3-story shear frame using the flexibility method to determine
    natural frequencies and mode shapes (after Clough and Penzien _[#])
    The model can be used to analyze a two story isolated structure
    by modeling the first story stiffness and mass
    as the isolated foundation system. In this example, the model
    is calibrated to reproduce the Clough example.

    | IMAGE | frames.jpg | Structural Model, 70, num, not 

    Normalized mode shapes are calculated and compared to Penzien and 
    Clough. _[#]
    
    | IMAGE | modes.jpg | Mode Shapes from Clough, 70, num, not 
""")

# %% rv.T("""Eigen Script | | | PYTHON
rv.T("""Eigen Script | | | PYTHON
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
    #
    nat_freq = 1/(np.sqrt(evalus))
    #
    #                natural frequencies
    print(" "*8,nat_freq)
    #
    evect = np.array(eigen[1])                                
    #
    #               eigenvectors
    print(tw.indent(str(evect), " "*8))
    """)

# %% rv.T("""Plot Script | | | PYTHON
rv.T("""Plot Script | | | PYTHON
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
    """)
    
rv.I("""Plot Mode Shapes | n |

    **blue:** mode 1 _[R]
    **red:** mode 2 _[R]
    **green:** mode 3 _[R] 
    | IMAGE | mode_shapes.png | Calculated Normalized Modes, 90, num, not

    
    _[[ENDNOTES]]
    R.W. Clough and J. Penzien, Dynamics of Structures. New York, NY, USA:
    McGraw-Hill, 1975. pg. 178-180

    ibid. pg. 180-182
    _[[END]]] 

    """)

# %% rv.D("""Publish Doc 
rv.D("""Publish Doc 

    | PUBLISH |Three Story Vibration| pdf
    
    
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
    toc_level = 2
    _[[END]]    
    """)
