import rivtlib.rvapi as rv

rv.I("""Introductionv| endnotes

    This is an example of a rivtbook. rivtbooks are collections of rivt files
    organized around a common subject. Each rivt file (subdivision) and its
    associated resources are contained in a unique folder to faciliate direct
    selection and insertion into rivt docs and reports.

    """)

rv.D("""Publish Doc 
    
    A rivt file may be published as a text, PDF or HTML doc by specifying the
    PUBLISH type parameter as txt, pdf or html. 
    
    Published files are found in sub-folders of the _published folder. A text
    version of the doc or report is is always written to the rivt and
    _rivt-public folders as a README.txt file which is displayed on the
    first page of a GitHub repo. 
    
    | PUBLISH | 101 Introduction | pdf
    
    _[[METADATA]] 
    [doc]
    authors = R Holland
    version = 1.0.0a12
    repo = https://github.com/rivt-info/rivt-single-doc
    license = https://opensource.org/license/mit/
    copyright = -
    fork1_authors = -
    fork1_version = -
    fork1_repo = -
    fork1_license = https://opensource.org/license/mit/
    
    [layout]
    subtitle =  Isolation Bearing Design
    copyright = --
    client = Example 04 - rivtbook
    coverpage = true
    coverlogo_size = 30
    coverlogo = bearing1.png
    runninglogo = logo2.png
    runninglabel = rivt
    project_ref = proj. 0004
    pdf_pagesize = letter
    pdf_margins = 1in, 1in, 1in, 1in 
    pdf_link_underline = false
    ; table of contents levels: 1- includes subdivisions, 2 - includes sections
    toc_level = 1

    [process]
    doc_verbose = true; if false minmize output during doc processing
    auto_cfg = true ; if false, config files are not updated from rivt file
    _[[END]]    
    """)