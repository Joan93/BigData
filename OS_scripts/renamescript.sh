# UPC MASTEAM BIGDATA Rrodrigo
# This script rename fixing the file beacause spark have problem with ':'
#!/bin/bash
cd /home/rodrigo/data/bigdata2
ls | grep : $f

for f in *; do 
mv -v "$f" `echo $f | tr ':' '_' `
done
echo "End Script"
