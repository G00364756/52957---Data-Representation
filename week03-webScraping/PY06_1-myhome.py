# 14. Modify the code to retrieve the first <div> with class="PropertyListingCard "
# 15. Modify that code to get the price
# class="PropertyListingCard__Price"
# 16. Also get the address

import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.myhome.ie/residential/mayo/property-for-sale?page=1")
soup = BeautifulSoup(page.content, 'html.parser')
listings = soup.find("div", class_="PropertyListingCard" )
price = listings.find(class_="PropertyListingCard__Price").text
address = listings.find(class_="PropertyListingCard__Address").text
print (price)
print (address)