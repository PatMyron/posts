import feedparser
import os
import praw
import re
import time
from urllib.parse import urlparse, urlunparse

reddit = praw.Reddit(client_id=os.environ['ID'],
                     client_secret=os.environ['SECRET'],
                     password=os.environ['PASS'],
                     user_agent='testscript',
                     username=os.environ['USER'])

def within(entry, seconds):
    try:
      return time.mktime(time.localtime()) - time.mktime(entry['published_parsed']) < seconds
    except:
      pass
    return time.mktime(time.localtime()) - time.mktime(entry['updated_parsed']) < seconds

def normalize_link(entry):
    entry['link'] = entry.get('feedburner_origlink', entry['link'])
    parsed_url = list(urlparse(entry['link']))
    parsed_url[4] = '&'.join([x for x in parsed_url[4].split('&') if not x.startswith('utm_')])
    entry['link'] = urlunparse(parsed_url)

def post(feed, subs, pattern):
  for entry in feedparser.parse(feed)['entries']:
    if re.match(pattern, entry['title'], re.IGNORECASE) and within(entry, 60 * 60 * 24):
      for sub in subs:
        try:
          normalize_link(entry)
          reddit.subreddit(sub).submit(entry['title'], url=entry['link'], resubmit=False)
        except Exception as e:
          print(e)
post('https://stackoverflow.blog/feed/', ['programming'], '.*Survey.*Results|.*Take.*Survey|.*Survey.*Open|.*Survey.*Live') # 2
post('https://blog.chromium.org/atom.xml', ['chrome', 'programming'], 'Chrome [0-9.]+') # 8
post('https://github.blog/feed/', ['git', 'github', 'programming'], '.* Git [0-9.]+') # 5
post('https://www.docker.com/blog/feed/', ['docker', 'programming'], 'Introducing Docker Engine [0-9.]+') # 0.5
post('https://feeds.feedburner.com/AmazonWebServicesBlog', ['aws', 'AmazonWebServices'], 'Now Open – AWS .* Region') # 3
post('https://azurecomcdn.azureedge.net/en-us/updates/feed/', ['azure'], 'Microsoft .* establish .* region') # 6
post('https://kubernetes.io/feed.xml', ['kubernetes'], 'Kubernetes [0-9.]+:') # 4
post('https://www.hashicorp.com/blog/products/terraform/feed.xml', ['terraform'], 'Announcing( HashiCorp)? Terraform [0-9.]+') # 1
post('https://www.latex-project.org/feed.xml', ['latex'], '.* LaTeX release') # 2
post('https://code.visualstudio.com/feed.xml', ['vscode', 'programming'], 'Visual Studio Code (January|February|March|April|May|June|July|August|September|October|November|December)') # 11
post('https://blog.rstudio.com/index.xml', ['rstats'], '(Announcing )?RStudio v?[0-9]\.[0-9](?! Preview)') # 1
post('https://android-developers.blogspot.com/atom.xml', ['androiddev'], 'Android Studio [0-9.]+') # 3
post('https://blog.jetbrains.com/kotlin/feed/', ['kotlin', 'androiddev'], 'Kotlin [0-9.]+ Released') # 4
post('https://swift.org/atom.xml', ['swift', 'iOSProgramming'], 'Swift [0-9.]+ released!') # 2
post('https://feeds.feedburner.com/PythonInsider', ['python'], 'Python [0-9.]+ ') # 10
post('https://blog.rust-lang.org/feed.xml', ['rust', 'programming'], 'Announcing Rust [0-9.]+') # 9
post('https://blog.golang.org/feed.atom', ['golang', 'programming'], 'Go [0-9.]+ is released') # 2
post('https://devblogs.microsoft.com/typescript/feed/', ['javascript', 'typescript', 'programming'], 'Announcing TypeScript [0-9.]+$') # 4
post('https://devblogs.microsoft.com/powershell/feed/', ['powershell'], 'Announcing PowerShell [0-9.]+') # 2
post('https://www.ruby-lang.org/en/feeds/news.rss', ['ruby'], 'Ruby [0-9.]+ Released') # 8
post('https://palletsprojects.com/blog/feed.xml', ['flask', 'python', 'programming'], 'Flask [0-9.]+ Released') # 1
post('https://www.djangoproject.com/rss/weblog/', ['django', 'python', 'programming'], 'Django [0-9.]+ Released') # 1
post('https://intellij-rust.github.io/feed.xml', ['rust'], 'IntelliJ Rust Changelog ') # 24
# post('https://rust-analyzer.github.io/feed.xml', ['rust'], 'Changelog ') # 52
# post('https://www.youtube.com/feeds/videos.xml?channel_id=UC88Cq0GO7AZebZh4Z0K3-AA', ['pittsburgh'], 'NEIGHBORHOODS OF PITTSBURGH')
