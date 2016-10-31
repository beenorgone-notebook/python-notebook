# http://stackoverflow.com/questions/6399978/getting-started-with-twitter-oauth2-python

import oauth2 as oauth
import requests
import pprint

from requests_oauthlib import OAuth1, OAuth1Session

CONSUMER_KEY = 'KjmtqqGMuZ7M5GXpq5pScg'
CONSUMER_SECRET = 'j7wZRGMJ2BDmueHTFnHZger2FpJ2r5vKfGcYej05w'
ACCESS_TOKEN = '266612976-ekrmoTXge65r7Qsy8FhF9Nn0hpoap6amjmps5oAC'
ACCESS_SECRET = 'vlQ3Agfb2bica7NpKfPHLjNYtZuvrr9VOHTHWTIjhwHbE'
auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

url1 = 'https://api.twitter.com/1.1/account/verify_credentials.json'
r = requests.get(url1, auth=auth)
# print(r.text)

twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN,
                        ACCESS_SECRET)
url2 = 'https://api.twitter.com/1/account/settings.json'
r2 = twitter.get(url2)
# print('===========================================')
# print(r2.text)

url3 = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
params = {'screen_name': 'beenorgone', 'count': 2}

r3 = requests.get(url3, auth=auth, params=params)
pprint.pprint(r3.text)
