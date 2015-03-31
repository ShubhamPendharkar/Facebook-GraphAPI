import requests # pip install requests
import json

base_url = 'https://graph.facebook.com/me'

# Get 10 likes for 10 friends
fields = 'id,name,books'
ACCESS_TOKEN = 'CAACEdEose0cBAMKRIHCtYP4OvkN7XR0xySmlrnFfOhLUoV9UwlGnxVXq74jk4B2oeZBsEZB6eiFCe1JxGdXdgTguiX4JAtJXHvqPosJa2TF6SZAgHyNEkwrOqG71L43h4i7VZCiltbZB5ZChj8F4ZAyfIeQqlRYSeWe3l9zTVap1hWGw62WRI6ZAstMUN6Y5J9WZAmvstKYLL6AZB19HXmO1Uh'
'''ACCESS_TOKEN = 'CAACEdEose0cBAEhd7SvZBX0ApUI4pKsJaZAZBDB0pFHH9JKyVD9I39CQVLBe8rtr8BPW5JiGeZCgy1XWGkCaq8bnDj9jc94ASvSEVnDV06kkq4CR2phghbZBGY3VARD2obTWqD7JFsiSzfWNuUrfbC6bNFVpkLHNRp2y3J4VVHX0utPAfstZCdsxZBmaV7xo0gb8ZAKoy6mAGVQtOlMvqaMgOAsqdZBjsfmsZD'
'''
url = '%s?fields=%s&access_token=%s' % \
    (base_url, fields, ACCESS_TOKEN,)

# This API is HTTP-based and could be requested in the browser,
# with a command line utlity like curl, or using just about
# any programming language by making a request to the URL.
# Click the hyperlink that appears in your notebook output
# when you execute this code cell to see for yourself...
#print url

# Interpret the response as JSON and convert back
# to Python data structures
content = requests.get(url).json()

# Pretty-print the JSON and display it
print json.dumps(content,indent = 1)
