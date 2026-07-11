import rivtlib.rvapi as rv

# %% rv.I("""Introduction 
rv.I("""rivtbook Example 

    A rivtbook is a collection of rivt files with a common subject and organized
    for selective addition to rivt docs and reports. A rivtbook may be published as
    a PDF or text report to facilitate review and selection of chapters.
    
    rivtbooks do not need to be organized into divisions. A sequence of chapters
    is sufficient as chapters will be renumbered in the target report. The folder
    structure for rivtbooks faciliates copy-paste of chapters. 
    
    The rivt file and its source files are contained within the same folder
    (orange). A rivtbook chapter can be imported into a rivt report by copying
    the *rivt file* (blue) to the *rivt-report* folder and its source folders
    (green) to the *rvsrc* folder.
    
    
    | IMAGE | img/rvbk-rivt.jpg | How to copy a rivtbook chapter to a rivt report, 100, num, not 

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