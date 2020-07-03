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



