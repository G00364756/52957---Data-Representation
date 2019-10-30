# 5. Modify the program to get all the <tr>

from bs4 import BeautifulSoup
with open("../week02-javascript/carviewer2.html") as fp:
 soup = BeautifulSoup(fp,'html.parser')
#print (soup.tr)
 rows = soup.findAll("tr")
for row in rows:
    print("------")
    print(row)