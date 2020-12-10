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
    if re.match(pattern, entry['title']) and entry['title'] not in ['Visual Studio Code June 2020', 'Ruby 2.4.10 Released', 'Ruby 2.5.8 Released', 'Ruby 2.6.6 Released', 'Ruby 2.7.1 Released', 'Android Studio 4.1']:
      try:
        reddit.subreddit(sub).submit(entry['title'], url=entry['link'], resubmit=False)
      except:
        pass
# post('https://android-developers.blogspot.com/atom.xml', 'androiddev', 'Android Studio [0-9.]+')
post('https://code.visualstudio.com/feed.xml', 'vscode', 'Visual Studio Code (January|February|March|April|May|June|July|August|September|October|November|December)')
post('https://blog.rust-lang.org/feed.xml', 'rust', 'Announcing Rust [0-9.]+')
post('https://blog.golang.org/feed.atom', 'golang', 'Go [0-9.]+ is released')
post('https://blog.jetbrains.com/kotlin/feed/', 'kotlin', 'Kotlin [0-9.]+ Released')
post('https://devblogs.microsoft.com/typescript/feed/', 'javascript', 'Announcing TypeScript [0-9.]+$')
post('https://devblogs.microsoft.com/powershell/feed/', 'powershell', 'Announcing PowerShell [0-9.]+')
post('https://swift.org/atom.xml', 'swift', 'Swift [0-9.]+ released!')
post('https://www.ruby-lang.org/en/feeds/news.rss', 'ruby', 'Ruby [0-9.]+ Released')
post('https://feeds.feedburner.com/AmazonWebServicesBlog', 'aws', 'Now Open – AWS .* Region')
