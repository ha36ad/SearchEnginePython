import requests
import bs4
from csv import writer
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq 


#url to scrape
my_url = "http://quotes.toscrape.com/page/2/"

#Grabs webpage's details
Client = uReq(my_url)
#Reading the webpage's details and storing it
page_scrape_html = Client.read()

#Terminating the connection
Client.close()

#Parsing the  html file
page_soup = soup(page_scrape_html, "html.parser")
print(page_soup.body.text)

soupfind = page_soup.findAll ('span',{"class":"text"})
print(soupfind)
print(len(soupfind))
