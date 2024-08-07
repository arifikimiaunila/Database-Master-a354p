import re
import string

class ParsesSearchPath:
    #Parse the Postgres "search_path" configuration value into an array.
    #@param  string|list|null  searchPath
    #@return list
    def parseSearchPath(searchPath, matches, schema):
      if type(searchPath) is str:
          re.findall('/[^\s,"\']+/', searchPath, matches)
            
          searchPath = matches[0]
        
      if type(searchPath) is not None:
          return list(str.strip(schema))
      else:
          return []
