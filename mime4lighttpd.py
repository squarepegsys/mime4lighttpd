#!/usr/local/bin/python
import sys

fp = file(sys.argv[1])
out = file("mime.out","w")

out.write("mimetype.assign = (\n")

for line in fp:
   if line.find(";")<0 or not line.strip():
      continue
  
   type,extlist = line.strip()[:-1].split(None,1)

   for ext in extlist.split():
      outstr="\".%s\" => \"%s\",\n" %(ext,type)
      out.write(outstr)

out.write(")\n")

fp.close()
out.close()

        
    
