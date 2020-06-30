import requests
from bs4 import BeautifulSoup
from csv import writer
from urllib.request import urlopen as uReq 

my_url = "http://quotes.toscrape.com/page/2/"
Client = uReq(my_url)
page_scrape_html= Client.read()
Client.close()


soup= BeautifulSoup(html_doc, 'html.parser')

soupfind =soup.findAll ('div')

