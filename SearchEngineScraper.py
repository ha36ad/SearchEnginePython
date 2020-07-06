import pprint
from search_engine_parser.core.engines.bing import Search as BingSearch
from search_engine_parser.core.engines.google import Search as GoogleSearch
from search_engine_parser.core.engines.yahoo import Search as YahooSearch
from search_engine_parser.core.engines.duckduckgo import Search as DuckSearch

#Search set
search = ('preach to the choir', 1)

#Desired search engines
g_search = GoogleSearch()
y_search = YahooSearch()
b_search = BingSearch()
d_search = DuckSearch()

#Result variables
g_results = g_search.search(*search)
y_results = y_search.search(*search)
b_results = b_search.search(*search)
d_results = d_search.search(*search)
a = {
    "Bing": b_results,
    "DuckDuckGo": d_results,
    "Google": g_results,
    "Yahoo": y_results
    }
