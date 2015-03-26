#Print name of given id and books liked by id=741504455940261 (Shubham Pendharkar) along with the total likes of the book.

import requests # pip install requests
import json	

base_url = 'https://graph.facebook.com/636504769758172'
ACCESS_TOKEN='CAACEdEose0cBALjczYRqrRU2oWwW8D70PhINvI1q71l96ulZCQJGZBpywH8LxgIYl5qxvrgal23FMdfMu7kbCqSsf147lml2CbBS99gpZCIbgg58CL07HG62wkWRhqhehmfXMiuZCz1GK5H66Tr2wqK1cRIqvNYs4yAjTAZBQ37GjpY2Vwdg7ldxRf27nzMl7a5WWYxv0Th8LHpK8ZB3oUf5pqxavvhvEZD'
fields ='books{name,likes}'
url = '%s?fields=%s&access_token=%s' % \
    (base_url, fields, ACCESS_TOKEN,)

content = requests.get(url).json()

# Pretty-print the JSON and display it
print json.dumps(content, indent=1)
