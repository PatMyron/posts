import feedparser
import os
import praw
import re
reddit = praw.Reddit(client_id=os.environ['ID'],
                     client_secret=os.environ['SECRET'],
                     password=os.environ['PASS'],
                     user_agent='testscript',
                     username=os.environ['USER'])
def post(feed, sub, pattern):
  d = feedparser.parse(feed)
  for entry in d['entries']:
    if re.match(pattern, entry['title'], re.IGNORECASE) and not re.match('(Visual Studio Code June 2020|Ruby (2.4.10|2.5.8|2.6.6|2.7.1)|Swift (3.0|4.1|4.2)|Android Studio 4.1|NEIGHBORHOODS OF PITTSBURGH - (HOMEWOOD|MEXICAN WAR STREETS|LAWRENCEVILLE|POLISH HILL|MT. OLIVER|MOUNT WASHINGTON|SPRING HILL|WILKINSBURG|GREENFIELD))', entry['title']):
      try:
        reddit.subreddit(sub).submit(entry['title'], url=entry['link'], resubmit=False)
      except:
        pass
# post('https://feeds.feedburner.com/AmazonWebServicesBlog', 'aws', 'Now Open – AWS .* Region')
# post('https://android-developers.blogspot.com/atom.xml', 'androiddev', 'Android Studio [0-9.]+')
# post('https://feeds.feedburner.com/PythonInsider', 'python', 'Python [0-9.]+ ')
post('https://azurecomcdn.azureedge.net/en-us/updates/feed/', 'azure', 'Microsoft .* establish .* region')
post('https://code.visualstudio.com/feed.xml', 'vscode', 'Visual Studio Code (January|February|March|April|May|June|July|August|September|October|November|December)')
post('https://blog.rust-lang.org/feed.xml', 'rust', 'Announcing Rust [0-9.]+')
post('https://blog.golang.org/feed.atom', 'golang', 'Go [0-9.]+ is released')
post('https://blog.jetbrains.com/kotlin/feed/', 'kotlin', 'Kotlin [0-9.]+ Released')
post('https://devblogs.microsoft.com/typescript/feed/', 'javascript', 'Announcing TypeScript [0-9.]+$')
post('https://devblogs.microsoft.com/powershell/feed/', 'powershell', 'Announcing PowerShell [0-9.]+')
post('https://swift.org/atom.xml', 'swift', 'Swift [0-9.]+ released!')
post('https://www.ruby-lang.org/en/feeds/news.rss', 'ruby', 'Ruby [0-9.]+ Released')
post('https://www.youtube.com/feeds/videos.xml?channel_id=UC88Cq0GO7AZebZh4Z0K3-AA', 'pittsburgh', 'NEIGHBORHOODS OF PITTSBURGH')
