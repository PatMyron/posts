from collections import defaultdict

import requests

tweeters = defaultdict(lambda: 0)

from firebase import firebase

firebase = firebase.FirebaseApplication('https://hacker-news.firebaseio.com', None)
for i in range(100000):
    r = requests.get('https://news.ycombinator.com/item?id=' + str(i))
    tweeters[firebase.get('/v0/item/' + str(i), 'by')] += 1
    print(sorted(tweeters.items(), key=lambda item: item[1], reverse=True))
