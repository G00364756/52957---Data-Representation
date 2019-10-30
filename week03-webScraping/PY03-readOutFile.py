# 4. Extract the first <tr> from the file (make a file called (PY03-readOutFile.py)

from bs4 import BeautifulSoup
with open("../week02-javascript/carviewer2.html") as fp:
 soup = BeautifulSoup(fp,'html.parser')
print (soup.tr)