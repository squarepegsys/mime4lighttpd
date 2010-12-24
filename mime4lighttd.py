#!/usr/local/bin/python

fp = file("mime.types")
out = file("mime.out","w")

for line in fp:
   if line.find(";")<0 or line.strip()==None:
      continue
  
   type,extlist = line.strip()[:-1].split(None,1)

   for ext in extlist.split():
      outstr="\".%s\" => \"%s\",\n" %(ext,type)
      out.write(outstr)

fp.close()
out.close()

        
    
