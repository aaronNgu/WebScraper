from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup

myURL = 'https://www.newegg.ca/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20cards'
#opening connection
uClient = uReq(myURL)
page_HTML = uClient.read()
uClient.close()
#parse the page_HTML using html parser
page_soup = soup(page_HTML, "html.parser")
containers = page_soup.findAll("div", {"class" : "item-info"})

filename = "products.csv"
f = open(filename,"w")
headers = "brand, product_name, shipping\n"
f.write(headers)

for container in containers:
     brand =  container.div.a.img["title"]

     title_container = container.findAll("a",{"class":"item-title"})
     productName = title_container[0].text

     shipping_container = container.findAll("li",{"class":"price-ship"})
     shippingPrice =  shipping_container[0].text.strip()

     print("brand : " + brand)
     print("productName : " + productName)
     print("shippingPrice : " + shippingPrice)
     f.write(brand + "," + productName.replace(",","| ") + "," + shippingPrice + "\n")

f.close()
