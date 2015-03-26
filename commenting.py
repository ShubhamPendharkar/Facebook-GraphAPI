#Comment on a post with post id=741504455940261_774462089311164

import requests
import json

TOKEN='' 

def get_posts():
    """
        Returns the list of posts on my timeline
    """

    parameters = {'access_token': TOKEN}
    r = requests.get('https://graph.facebook.com/me/feed', params=parameters)
    result = json.loads(r.text)
    return result['data']

def comment_on_posts():
        url = 'https://graph.facebook.com/741504455940261_774462089311164/comments'
        message = 'Commenting through the Graph API'
        parameters = {'access_token': TOKEN, 'message': message}
        s = requests.post(url, data = parameters)
	print "done"

if __name__ == '__main__':
    comment_on_posts()
