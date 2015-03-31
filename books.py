#Print name of books liked by id=741504455940261 (Shubham Pendharkar).

import requests # pip install requests
import json	

base_url = 'https://graph.facebook.com/636504769758172'
ACCESS_TOKEN='CAACEdEose0cBAIkAki14SzZAElas0RShemivQ91wEsHA8nxbzrZBifHgOzECKqihNX4Ew6Mth4MZAAXsxaasdFpZBwEebhEhXdC6oU9VDqdZC6kkukykprkq2Ge99RIYjtDJJzlv05yZCqC79ftkqK3w9lP5NrA0ZANMqhuL10Ui9ZAX3rbH2XcNLsh7ZBuMKy6H7Ex9EftOV3QBvsHkT1Pb8Q1QrZB2lxOAcZD'
fields ='books{name,likes}'


def get_books():
    """
        Returns the list of posts on my timeline
    """

    parameters = {'access_token': ACCESS_TOKEN}
    r = requests.get('https://graph.facebook.com/741504455940261/books', params=parameters)
    result = json.loads(r.text)
    return result["data"]

r=get_books()
for book in r:
	print book['name']	



