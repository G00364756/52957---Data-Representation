# 1. Test that we can retrieve a web page from the web. save this file at PY01-testRequest.py in a
# folder called week03-webScraping

import requests
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print (page)
print("-------------------")
print (page.content)
