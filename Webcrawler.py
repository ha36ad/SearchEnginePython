import scrapy
from pathlib import Path

#project name + url
project_path = input("Enter your path (C:, D:, etc.) : ")
path = Path(project_path)
my_url = input("Enter the url you are crawling: ")

# Function for creating a  file
def write_file(path, data):
    with open (path,"w") as file:
        file.write(data)
        
#Create queue and crawl files
def create_queue(project_path, url):
    queue =  path / "queue.txt"
    crawl =  path / "crawl.txt"
    
    #Writing  the files
    write_file(queue, url)
    write_file(crawl,  " ")    

#Calling the  queue function
create_queue(path , my_url)   

#Appending files instead of creating new ones
def append_file (path, data):
    with open (path,"a") as file:
        file.write(data + '/n')

#Clearing a file's contents
def clear_file (path):
    with open(path, "w") as file:
        pass

#Using a set to increase speed
def file_sets (file_name):
    #Intialize an empty set
    result = set()
    #Convert each element to a set
    with open(file_name, "r") as file:
        for line in file:
            result.add(line.replace('\n', ''))
    return result

#Function to go from a set to a file
def sets_file(links, file):
    clear_file(file)
    for link in sorted(links):
        append_file(file, link)
        
#Spider
class Spider(scrapy.Spider):
    #Name of Spider
    name = "Spider"
    start_urls = [
        'http://quotes.toscrape.com/page/2/']
#Parsing
def parse(self,response):
    page =response.url.split('/')[-1]
    file_name ='spider-%s.html' %page
    with open(file_name,"w") as file:
        file.write(response.body)
    title = response.css(".set::text").extract_first()
    
