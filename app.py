import urllib.parse
import base64
import json


CONSUMER_KEY = ""
CONSUMER_SECRET = ""
# 1. Write to DB (JSONLINES)
# 2. Scheduler to run once a week?



def tweet_info(data, handler):
    # Create a json lines file for each keyword.
    # For every keyword,
    # List of screen names
    # dump these to a json file.
    return json.dumps(data)


def get_followers(data, handler):
    directory_name = os.path.dirname(os.path.getabspath(__file__))
    file_name = os.path.join(directory_name, 'jsonlines.jsonl')
    followers = gramex.cache.open(file_name, 'json')
    for follower in followers:
        ...
    pass
    return
    # read json file
    # retrieve list of followers
    # send a request to twitter api

def last_transform(data, handler):
    # dumps to a final json
    ...
