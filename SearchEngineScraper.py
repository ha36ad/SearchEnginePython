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
search_set = (search_query, 1)
search_set2 =(search_query, 2)

#Searching for query
g_results = g_search.search(*search_set)
b_results = b_search.search(*search_set2)
d_results = d_search.search(*search_set2)
y_results = y_search.search(*search_set)

# print first title from google search
for i in range(0,5):
    if g_results["links"] == y_results["links"]:
        print(b_results["links"][i])
        print(d_results ["links"][i])
        print("")
    else:
        print(g_results["links"][i])
        print(y_results ["links"][i])
        
    if i == 5:
        break
