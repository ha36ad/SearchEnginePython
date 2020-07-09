from search_engine_parser.core.engines.yahoo import Search as YahooSearch
from search_engine_parser.core.engines.google import Search as GoogleSearch
from search_engine_parser.core.engines.bing import Search as BingSearch
from search_engine_parser.core.engines.duckduckgo import Search as DuckSearch
import csv

#Intializing Search Engines
g_search = GoogleSearch()
y_search = YahooSearch()
b_search = BingSearch()
d_search = DuckSearch()

#Search prompt
search_query = input("Enter your search query here: ") 
search_set = (search_query, 2)
search_set2 = (search_query, 3)

#Searching for query
g_results = g_search.search(*search_set)
b_results = b_search.search(*search_set2)
d_results = d_search.search(*search_set2)
y_results = y_search.search(*search_set)

#Create csv file
with open('data.csv','w',newline='') as file:
    #Creating writer
    writer = csv.writer(file)
    #Writing each row's header
    writer.writerow(['Bing','DuckDuckGo','Google','Yahoo'])
    #Print first 20 links for each search engine (can comment)
    for i in range(0,21):
        print(b_results["links"][i])
        print(d_results["links"][i])
        print(y_results ["links"][i])
        print(g_results["links"][i])
       #Writing each row
        writer.writerow([b_results["links"][i], d_results["links"][i], g_results["links"][i], y_results ["links"][i] ])
        
#Modifying csv to not have repeating links
with open ('data.csv','r', newline= '') as file2, open('edited_data.csv','w', newline='') as edited_file:
    reader = csv.reader(file2)
    writer2 = csv.writer(edited_file)
    next(reader)
    writer2.writerow(['Organized Links'])
    for i in range(0,21):
        for line in reader:
            if line[i] == line[i+1]:
                writer2.writerow([line[2]])
            else:
                writer2.writerow(line)

