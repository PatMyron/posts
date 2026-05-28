#!/usr/bin/env python3
import json
import sys
from urllib.parse import parse_qs, urlparse
from urllib.request import Request, urlopen


USER_AGENT = "PatMyron-post-comment-counts/1.0"


def get_json(url):
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request) as response:
        return json.load(response)


def hacker_news_count(url):
    item_id = parse_qs(urlparse(url).query).get("id", [""])[0]
    if not item_id:
        raise ValueError("Hacker News URL is missing an id query parameter")
    item = get_json(f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json")
    return item.get("descendants", 0)


def reddit_count(url):
    parsed = urlparse(url)
    json_url = parsed._replace(path=parsed.path.rstrip("/") + ".json", query="depth=1").geturl()
    listing = get_json(json_url)
    return listing[0]["data"]["children"][0]["data"].get("num_comments", 0)


def comment_count(url):
    host = urlparse(url).netloc.lower()
    if "news.ycombinator.com" in host:
        return hacker_news_count(url)
    if "reddit.com" in host:
        return reddit_count(url)
    raise ValueError(f"Unsupported URL: {url}")


def urls_from_args_or_stdin():
    if len(sys.argv) > 1:
        return sys.argv[1:]
    return [line.strip() for line in sys.stdin if line.strip()]


def main():
    for url in urls_from_args_or_stdin():
        try:
            print(f"{comment_count(url)}\t{url}")
        except Exception as error:
            print(f"0\t{url}\t{error}", file=sys.stderr)


if __name__ == "__main__":
    main()
