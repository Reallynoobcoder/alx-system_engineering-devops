#!/usr/bin/python3
import requests
"""
queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'Naka/1.0'}

    respons = requests.get(url, headers=headers, allow_redirects=False)

    if respons.status_code == 200:

        data = respons.json()
        posts = data['data']['children']

        for post in posts[0:10]:
            print(post['data']['title'])
    else:
        print(None)
