import re
import string

class ParsesSearchPath:
    #Parse the Postgres "search_path" configuration value into an array.
    #@param  string|list|null  searchPath
    #@return list
    def parseSearchPath(searchPath):
      if type(searchPath) is str:
          x=re.search('/[^\s,"\']+/', searchPath)
      if x:
          return searchPath.strip()
      else:
          return []
