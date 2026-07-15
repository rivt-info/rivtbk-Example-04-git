#! python
"""generate a rivtbook

Run this Python script in the rivtbk root folder to generate a PDF or txt book.
The HTML format is not available for books. Copy and rename this file to save
custom book settings (e.g. make-rivtbook-2.py). See https://www.rivt.info for
more details.

"""

import os
import sys
import importlib

# ======== Modify rivtbook settings between the double lines ==============
# ======== Update book_filename, must start with rivtbk- ==================

booksetS = f"""
[book]
;-----------------------------------------
book_filename = rivtbk-Isolation-Bearing-Design.txt
version = 1.0.0a13
exclude = -- ; comma separated doc numbers to exclude eg. rv102, rv204
[process]
;-----------------------------------------
auto_cfg = true ; writes config files, false allows for manual editing
regen_pdf = false ; regenerate pdf doc files 
book_verbose = true ; generate report - verbose output
[layout]
;--------------- cover page and runner settings
;--- add logo files to img folder in first chapter, size is % page width
title = Isolation Bearing Design
subtitle = Property Calculations and Design Examples
client = rivtbook Example
project_ref = Proj. 0004
authors = R Holland 
copyright = StL
coverlogo = bearing1.png
coverlogo_size = 50
running_logo = rivt02.png 
running_label = rivt
;----------------- PDF settings
; colors: red, blue, green, black, gray, brown, maroon, gray, olive, cyan
; margins: top, right, bottom, left    page size: letter, legal, A4 
pdf_link_underline = false
pdf_link_color = blue
pdf_pagesize = letter
pdf_margins = 1in, 1in, 1in, 1in 
;------------------ TOC levels
; 1: include subdivisions    2: include subdivisions and sections
toc_level = 1
"""
# ============================================================================
# the following lines are required following the settings
os.environ["bookset"] = booksetS
module_name = 'rivtlib.rvbook'
if module_name in sys.modules:
    # Reloads the module on subsequent iterations
    importlib.reload(sys.modules[module_name])
else:
    # Loads the module for the first time
    __import__(module_name)
