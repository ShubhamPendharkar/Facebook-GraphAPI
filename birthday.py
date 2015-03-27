#Write comment to all the posts.

import requests
import json

AFTER = 1353233754
TOKEN = 'CAACEdEose0cBAJn51XRwJKvOiL6sbD7FZCqZADw94RoxIsZBRkMMsFzY4slxvFsTj9QGHJJWyw63gtTPNCz9SZBcOVs3Fr1k3DLmJAEkcdXlbAZAhx3Q8HIYreGLkjPtNJMFYXXEU8NNBL28tZAVr2eOTPuboj8BkdZAjHRlAln1i5jha1ZBgQvB2KSUBCq8UqiVUETqlP1nmY3sC0BqKk1WDLfrkfKbcHIZD'

def get_posts():
    """Returns dictionary of id, first names of people who posted on my wall

    between start and end time"""

    query = ("SELECT post_id, actor_id, message FROM stream WHERE "
             "filter_key = 'others' AND source_id = me() AND "
             "created_time > 1353233754 LIMIT 200")

    payload = {'q': query, 'access_token': TOKEN}
    r = requests.get('https://graph.facebook.com/fql', params=payload)
    result = json.loads(r.text)
    return result['data']

def commentall(wallposts):
    """Comments thank you on all posts"""
    #TODO convert to batch request later

    for wallpost in wallposts:
        r = requests.get('https://graph.facebook.com/%s' % wallpost['actor_id'])

        url = 'https://graph.facebook.com/%s/comments' % wallpost['post_id']
        user = json.loads(r.text)

        message = 'Thanks a lot :)/>'
        payload = {'access_token': TOKEN, 'message': message}
        s = requests.post(url, data=payload)
        print "Wall post %s done" % wallpost['post_id']

if __name__ == '__main__':
	commentall(get_posts())
	a=get_posts()
	for items in a:
		print items['message']




