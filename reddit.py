from collections import defaultdict

import requests

SESSION = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}

tweeters = defaultdict(lambda: 0)

for i in range(100000):
    r = SESSION.get('https://www.reddit.com/comments/' + str(i))
    if '/r/' in r.url:
        r = SESSION.get('https://www.reddit.com/comments/' + str(i) + '.json', headers=headers)
        tweeters[r.json()[0]['data']['children'][0]['data']['author']] += 1
        print(sorted(tweeters.items(), key=lambda item: item[1], reverse=True))
