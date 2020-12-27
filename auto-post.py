import feedparser
import os
import praw
import re
import time
reddit = praw.Reddit(client_id=os.environ['ID'],
                     client_secret=os.environ['SECRET'],
                     password=os.environ['PASS'],
                     user_agent='testscript',
                     username=os.environ['USER'])
def post(feed, subs, pattern):
  d = feedparser.parse(feed)
  for entry in d['entries']:
    try:
      if time.mktime(time.localtime()) - time.mktime(entry['published_parsed']) > 60 * 60 * 24 * 7:
        continue
    except:
      pass
    if re.match(pattern, entry['title'], re.IGNORECASE) and time.mktime(time.localtime()) - time.mktime(entry['updated_parsed']) < 60 * 60 * 24 * 7:
      for sub in subs:
        try:
          if 'feedburner_origlink' in entry:
            entry['link'] = entry['feedburner_origlink']
          reddit.subreddit(sub).submit(entry['title'], url=entry['link'], resubmit=False)
        except Exception as e:
          print(e)
post('https://www.docker.com/blog/feed/', ['docker', 'programming'], 'Introducing Docker Engine [0-9.]+')
post('https://feeds.feedburner.com/AmazonWebServicesBlog', ['aws', 'AmazonWebServices'], 'Now Open – AWS .* Region')
post('https://azurecomcdn.azureedge.net/en-us/updates/feed/', ['azure'], 'Microsoft .* establish .* region')
post('https://code.visualstudio.com/feed.xml', ['vscode', 'programming'], 'Visual Studio Code (January|February|March|April|May|June|July|August|September|October|November|December)')
post('https://android-developers.blogspot.com/atom.xml', ['androiddev'], 'Android Studio [0-9.]+')
post('https://blog.jetbrains.com/kotlin/feed/', ['kotlin', 'androiddev'], 'Kotlin [0-9.]+ Released')
post('https://swift.org/atom.xml', ['swift', 'iOSProgramming'], 'Swift [0-9.]+ released!')
post('https://feeds.feedburner.com/PythonInsider', ['python'], 'Python [0-9.]+ ')
post('https://blog.rust-lang.org/feed.xml', ['rust', 'programming'], 'Announcing Rust [0-9.]+')
post('https://blog.golang.org/feed.atom', ['golang', 'programming'], 'Go [0-9.]+ is released')
post('https://devblogs.microsoft.com/typescript/feed/', ['javascript', 'typescript', 'programming'], 'Announcing TypeScript [0-9.]+$')
post('https://devblogs.microsoft.com/powershell/feed/', ['powershell'], 'Announcing PowerShell [0-9.]+')
post('https://www.ruby-lang.org/en/feeds/news.rss', ['ruby'], 'Ruby [0-9.]+ Released')
# post('https://www.youtube.com/feeds/videos.xml?channel_id=UC88Cq0GO7AZebZh4Z0K3-AA', ['pittsburgh'], 'NEIGHBORHOODS OF PITTSBURGH')
