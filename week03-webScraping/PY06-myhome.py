# 11. Open myhome.ie in a browser and search for houses for sale in a county, you will see that
# the search results are in multiple pages navigate to the second page and note the URL

# 12. Create a file called py06-myhome.py, and write the code to read the page. (this may take a
# little time to run

import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.myhome.ie/residential/mayo/property-for-sale?page=1")
soup = BeautifulSoup(page.content, 'html.parser')
print (soup.prettify())