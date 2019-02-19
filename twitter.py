from collections import defaultdict

tweeters = defaultdict(lambda: 0)
import requests
for i in range(100000):
    r = requests.get('http://www.twitter.com/Patrick_Myron/status/' + str(i))
    if "Myron" not in r.url and 'account/suspended' not in r.url:
        tweeters[r.url.split('/')[3]] += 1
        print(sorted(tweeters.items(), key=lambda item: item[1], reverse=True))
    # r = requests.get('https://www.instagram.com/p/' + chr(ord('A') + i))
    # print(r.url)