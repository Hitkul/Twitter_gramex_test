import os
import json
import requests
from gramex.config import variables


def make_requests():
    for keyword in variables['keywords']:
        r = requests.get(''.join([variables['URLROOT'], keyword]))
    return r.status_code


def writedisk(result, handler):
    dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(dir, 'tweets.jsonl'), 'a') as out:
        for status in result['statuses']:
            json.dump(status, out)
    return result
