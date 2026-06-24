#! python
"""generate a rivtbook

Run this Python script in the rivtbk folder to generate a PDF book. Copy and
rename this file to save custom book settings (e.g. make-rivtbook-2.py).
See https://www.rivt.info for more details.

"""

import os
import sys
import importlib

# ========= Modify report settings between the double lines ==============
reportset = f"""
[settings]
;------- report file name including the pdf extension
;----------------------------------------------------------------
;
rept_filename = rivtbk-Isolation Bearing Design.pdf
;
;----------------------------------------------------------------
;------- comma separated list of doc numbers to exclude eg. rv102, rv204
exclude = -- 
;-------  rivt writes config files, false allows for manual editing
auto_cfg = true
;------- regenerate pdf doc files 
regen_pdf = false 
;------- generate report - verbose output
rep_verbose = true

[format]
title = Tree Fort
subtitle = Structural Design
client = Report Example
project_ref = Proj. 0003
authors = R Holland 
copyright = StL
version = 1.0.0a12
;----- put logo, header, footer files in *page* folder, size is % page width
coverlogo = bearing1.png
coverlogo_size = 50
running_logo = rivt02.png 
running_label = rivt
;----- table of contents levels: 1 - includes subdivisions, 2 - includes sections
toc_level = 1
;----- underline links in PDF - true or false
pdf_link = false 
;----- page size letter, legal, A4 - margins top, right, bottom and left
pdf_pagesize = letter
pdf_margins = 1in, 1in, 1in, 1in 
"""
# ============================================================================
# the following lines are required following the settings
os.environ["reportset"] = reportset
module_name = 'rivtlib.rvreport'
if module_name in sys.modules:
    # Reloads the module on subsequent iterations
    importlib.reload(sys.modules[module_name])
else:
    # Loads the module for the first time
    __import__(module_name)
