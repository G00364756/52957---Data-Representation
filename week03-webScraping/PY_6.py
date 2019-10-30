# 6. Now for each row let’s get the contents of the TD

from bs4 import BeautifulSoup
with open("../week02-javascript/carviewer2.html") as fp:
 soup = BeautifulSoup(fp,'html.parser')
#print (soup.tr)
 rows = soup.findAll("tr")
for row in rows:
    print("------")
    #print(row)
    cols = row.findAll("td")
    for col in cols:
        print(col.text)
