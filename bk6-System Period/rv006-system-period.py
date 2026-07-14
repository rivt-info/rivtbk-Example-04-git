import rivtlib.rvapi as rv

# %% rv.I("""System Period
rv.I("""System Period

    CLOUGH, PENZIEN - Dynamics of Structures, page 178

    Use flexibility formulation _[#] (see page 182)

    Also see _[#]

    calioPY Procedure Output - Example 6
    This example illustrates arrays and plotting.


    1. set up mass and stiffness arrays
    m = PL.array([[1.0,0,0],[0,1.5,0],[0,0,2.0]],float)        [1]
    k1 = 600·PL.array([[1,-1,0.0],[-1,3,-2],[0,-2,5]],float)   [2]

    2. flexibility and dynamic matrix
    f = PL.inv(k1)                                             [3]
    d = PL.inner(f,m)                                          [4]

    3. eigenvalues
    eigen = PL.eig(d)                                          [5]
    evalu = eigen[0]                                           [6]
    .  evalu = [ 0.00474  0.00104  0.00047]
    nat_freq = 1/(evalu^.5)                                    [7]
    .  nat_freq = [ 14.52482  31.00868  46.12656]

    4. normalize and scale eigenvectors
    evect = PL.array(eigen[1])                                 [8]
    .  evect = [[-0.813 -0.739  0.273]
    [-0.527  0.449 -0.694]
    [-0.246  0.502  0.666]]

    [py] for i in range(len(nat_freq)):
    [py]     evectt = PL.transpose(evect)     
    [py]     evectt[i] = evectt[i]/evectt[i][0]
    """)

# %% rv.I("""Eigenvectors and Eigenvalues 
rv.I("""Eigenvectors and Eigenvalues 
    
    normalized eigenvectors
. 
    [[ 1.     0.648  0.303]
    [ 1.    -0.608 -0.679]
    [ 1.    -2.542  2.44 ]]
    SUMMARY TABLES

    mass matrix
    1.0 0.0 0.0
    0.0 1.5 0.0
    0.0 0.0 2.0

    stiffness matrix
    600.0 -600.0 0.0
    -600.0 1800.0 -1200.0
    0.0 -1200.0 3000.0

    flexibility matrix
    0.0031 0.0014 0.0006
    0.0014 0.0014 0.0006
    0.0006 0.0006 0.0006

    dynamic matrix
    0.003 0.002 0.001
    0.001 0.002 0.001
    0.001 0.001 0.001

    xx = NP.concatenate((evals,evect),1)                          
    yy = ["freq","level 3","level 2","level 1"]                   
    tt = NP.vstack((yy,xx))                                       
    .  tt = [['freq' 'level 3' 'level 2' 'level
    ['14.52482' '1.0' '1.0' '1.0']
    ['31.00868' '0.648' '-0.608' '-2.542']
    ['46.12656' '0.303' '-0.679' '2.44']]

    eigenvectors and eigenvalues
    freq level 3 level 2 level 1
    14.52482 1.0 1.0 1.0
    31.00868 0.648 -0.608 -2.542
    46.12656 0.303 -0.679 2.44

    """)

# %% rv.I("""Plot Mode Shapes 
rv.I("""Plot Mode Shapes 
    
    _[[TEXT]] text
    1. set up mass and stiffness arrays
    [1] m = PL.array([[1.0,0,0],[0,1.5,0],[0,0,2.0]],float
    [2] k1 = 600*PL.array([[1,-1,0.0],[-1,3,-2],[0,-2,5]
   
    2. flexibility and dynamic matrix
    [3] f = PL.inv(k1)
    [4] d = PL.inner(f,m)
   
    3. eigenvalues
    [5] eigen = PL.eig(d)
    [6] evalu = eigen[0] ?5
    [7] nat_freq = 1/(evalu**.5) ?5
   
    4. normalize and scale eigenvectors
    [8] evect = PL.array(eigen[1]) ?
   
   
    -pycode-
    for i in range(len(nat_freq)):
    evectt = PL.transpose(evect)
    evectt[i] = evectt[i]/evectt[i][0]
    -insert-
   
    normalized eigenvectors
    {] evectt ?3
   
     SUMMARY TABLES
     
    -table-02 m ?4; mass matrix;
   
    -table-02 k1 ?4; stiffness matrix;

    -table-02 f ?4; flexibility matrix ;
   
    -table-02 d ?3; dynamic matrix ;
   
    -k-
    # use reshape to transpose 1d array (list)

    evals=PL.reshape(nat_freq, (len(nat_freq),1))
    xx = NP.concatenate((evals,evect),1)
    yy = ["freq","level 3","level 2","level 1"]
    tt = NP.vstack((yy,xx)) ?
    -table-01 tt ?3; eigenvectors and eigenvalues;
   ..
    # initialize eigenvector array (need (x,1) shapes for plotting
    ms = PL.shape(evect)
    zz = PL.zeros((ms[0],1))
    x1=PL.concatenate((evect,zz),1)
    -pycode-
    #plot mode shapes using pylab
    y=PL.array([0,1,2,3])
    m3=x1[2]*.35+3
    m2=x1[1]*.35+2
    m1=x1[0]*.35+1
    m=PL.concatenate((m1,m2,m3))
    PL.clf()
    PL.plot(m1,y)
    PL.plot(m2,y)
    PL.plot(m3,y)
    PL.xlim(.5,4.)
    PL.xlabel('mode')
    PL.ylabel('levels')
    PL.title("Mode Shapes\nClough\Penzien (page 178)")
    PL.grid()
    PL.savefig(_cpypath+"/figs/p178a.png")
    _[[END]]

    """)

# %% rv.R("""Bibliography | endnotes
rv.T("""Bibliography | endnotes

    R.W. Clough and J. Penzien, Dynamics of Structures. New York, NY, USA:
    McGraw-Hill, 1975.

    """)

rv.D("""Publish Doc 

    | PUBLISH |System Period | pdf
    
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
    toc_level = 1
    _[[END]]    
    """)
