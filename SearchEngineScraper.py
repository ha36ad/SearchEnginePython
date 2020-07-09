from search_engine_parser.core.engines.yahoo import Search as YahooSearch
from search_engine_parser.core.engines.google import Search as GoogleSearch
from search_engine_parser.core.engines.bing import Search as BingSearch
from search_engine_parser.core.engines.duckduckgo import Search as DuckSearch

#Intializing Search Engines
g_search = GoogleSearch()
y_search = YahooSearch()
b_search = BingSearch()
d_search = DuckSearch()

#Search prompt
search_query = input("Enter your search query here: ") 
search_set = (search_query, 2)
searc_set2 = (search_query, 3)

#Searching for query
g_results = g_search.search(*search_set)
b_results = b_search.search(*search_set2)
d_results = d_search.search(*search_set2)
y_results = y_search.search(*search_set)

# print first 10 links from each search engine
for i in range(0,11):
    if g_results["links"] == y_results["links"] and g_results["links"] == d_results["links"] and g_results["links"] == b_results["links"] :
        print(b_results["links"][i+2])
        print(d_results ["links"][i+1])
        print(y_results ["links"][i+3])
        
    else:
        print(b_results["links"][i])
        print(d_results["links"][i])
        print(y_results ["links"][i])

    print(g_results["links"][i])
    
  
