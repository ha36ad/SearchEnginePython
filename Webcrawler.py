import scrapy
from pathlib import Path

#project path input
project_path = input("Enter your path (C:, D:, etc.) : ")
#Storing user's path
path = Path(project_path)
#URL input
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

create_queue(path , my_url)   




