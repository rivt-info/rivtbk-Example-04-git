
Commands read and format files

API Scope           Command                                                
========== =============================================================== 
rv.R         | COPY |  abs src path | abs dest path | file pattern       
rv.R         | SHELL |  abs path | os, wait                              
rv.I, V      | TEXT |  rel path | type                                   
rv.I, V      | TABLE |  rel path | title,width,head;nohead,num;non       
rv.I, V      | IMAGE |  rel path | caption, scale, num;non, time;not     
rv.I, V      | IMAGE2 |  rel path1, rel path2 | c1,c2,s1,s2,n1,n2        
rv.V         | PYTHON |  rel path | rivt;namespace                       
rv.V         | VALTABLE |  rel path | title, width, num;non              
rv.V         | FUNCTION |  function, arg, var, type | label               
rv.D         | ATTACHPDF |  rel path | front;back, title                 
rv.D         | PUBLISH |  doc title | type                               
========== =============================================================== 

Parent paths for commands

================ =========================== ======
   Command           Parent Path [1]          R/W
================ =========================== ======
| COPY |                os root                R
| SHELL |               os root                R
| IMAGE |            rivt-report/              R
| IMAGE2 |           rivt-report/              R
| TABLE |            rivt-report/              R
| VALTABLE |         rivt-report/  [2,3]       R
| TEXT |             rivt-report/  [4]         R
| PYTHON |           rivt-report/              R
| ATTACHPDF |        rivt-report/              R
| PUBLISH |          _published/   [5]         W
================ =========================== ======

[1] relative file paths in commands generally begin with rvsrc/ 
[2] authored values are read from rvsrc/subdirectories
[3] values written by rivt may be read from rv_stor/vals  
[4] sections stored by rivt may be read from rv_stor/sect  
[5] docs are written to subdirectories of _published
