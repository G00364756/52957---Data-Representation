# 3. Test that you can read a file, we will use the carviewer2.html file that we made last week
# should be up a directory and in the week02 folder ie ("../week02/carviewer2.html")

from bs4 import BeautifulSoup
with open("../week02-javascript/carviewer2.html") as fp:
 soup = BeautifulSoup(fp,'html.parser')
print (soup.prettify())