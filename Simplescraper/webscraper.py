import requests
import bs4
from csv import writer
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq 

#url to scrape
my_url =input("Enter the url of the website you want to scrape: ")

#Grabs webpage's details
Client = uReq(my_url)
#Reading the webpage's details and storing it
page_scrape_html = Client.read()

#Terminating the connection
Client.close()

#ask user for element
element_tag = input("Enter the tag of the element that will be extracted: ")
element_type = input("Is the element a class or id?: ")
element_name = input("Enter the element name that will be extracted: ")

#if statement to check whether input is a class or id
if element_type == "class":
    elementtype =  "class"
elif elementtype == "id":
    elementtype = "id"
    
#Parsing the  html file
page_soup = soup(page_scrape_html, "html.parser")

#Finding an element, in this case, the <span> tag with a class of text
soupfind = page_soup.findAll (element_tag,{elementtype:element_name})

#creating a csv file
file_name ="scrape.csv"
f = open("scrape.csv",'w')
title = "Result\n"
f.write(title)
        
#loop to list out all the text
for soup_contain in soupfind:    
    soup_containn = soup_contain.text
    print(soup_containn)
    f.write(soup_containn + "\n")
#close the file
f.close()
