import requests
import urllib.request

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

for i in range(100000):
    # res = urllib.request.urlopen('https://www.fb.com/' + str(i))
    # finalurl = res.geturl()
    # print(finalurl)
    r = requests.get('https://www.facebook.com/' + str(i), headers=headers)
    print(r.headers)
    # if 'https://www.facebook.com/' + str(i) not in r.url:
    #     print(r.url)