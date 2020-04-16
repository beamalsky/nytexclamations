import time
import sys
import tweepy
from pprint import pprint

from nytexclamations import get_exclamations

LOCAL_DEVELOPMENT = True

if LOCAL_DEVELOPMENT:
    from secrets import *

else:
    from os import environ

    CONSUMER_KEY = environ['CONSUMER_KEY']
    CONSUMER_SECRET = environ['CONSUMER_SECRET']
    ACCESS_KEY = environ['ACCESS_KEY']
    ACCESS_SECRET = environ['ACCESS_SECRET']
    NYT_API_KEY = environ['NYT_API_KEY']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

exclamations = get_exclamations(NYT_API_KEY)

for exclamation in exclamations:
    e = str(exclamation)

    try:
        api.update_status(e)
        print("New tweet posted: " + e)
    except tweepy.error.TweepError:
        print("Duplicate found: " + e)
