#!/usr/bin/python3
import requests
"""
Queries the Reddit API and returns the number of subscribers
"""


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers subreddit.
    If an invalid subreddit is given, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'Naka/1.0'}

    response = requests.get(url, headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']

        return subscribers
    else:
        return 0
