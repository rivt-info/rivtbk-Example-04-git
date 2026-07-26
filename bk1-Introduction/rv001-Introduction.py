import rivtlib.rvapi as rv

# %% rv.I("""Introduction 
rv.I("""Introduction 

    A *rivtbook* is a collection of rivt files with common subject matter that
    may be published as a PDF or text report. The files are organized under a
    root folder *rivtbk-* with a name that identifies the subject matter. Each
    *rivt doc* is contained within a *chapter folder* that includes the 
    *rivt file* its associated sources. This facilitates extracting single docs 
    or merging a chapter into a *rivt report*. 
    
    """)

# %% rv.T("""rivtbook Example | m | | text
rv.T("""rivtbook Example | m | | text

    rivtbook Folder Structure

    rivtbk-subject-matter 
    ├── bk1-chapter title            
            ├── data/                    
            ├── image/                        
            ├── scripts/
            └── rv001-book-chapter.py
    └── bk2-chapter title            `
                ├── data/                    
                ├── image/                        
                ├── scripts/
                └── rv002-book-chapter.py
    
    """)

# %% rv.I("""Copy Chapter | m | 
rv.I("""Copy Chapter | m | 

    A rivtbook chapter may be copied to a rivt report by:

    #. merging the data, image and scripts folders into the /rvsrc folder 
    #. copying the rivt file to the /rivt-report folder.
    
    | IMAGE | rvbk-rivt.jpg | rivtbook chapter copied to a report, 85, num, not 

    """)


# %% rv.D("""Publish Doc 
rv.D("""Publish Doc 
    
    | PUBLISH | rivtbook Example - Introduction | pdf
    
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
