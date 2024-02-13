#!/usr/bin/python3
"""
Queries the Reddit API to get the titles
of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """Recursively get the titles of all hot articles for a given subreddit."""

    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers={'User-Agent': 'MyCustomUserAgent/1.0'},
        params={'limit': 100, 'after': after},
    )

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data['data']['children']
    for post in posts:
        hot_list.append(post['data']['title'])

    after = data['data']['after']
    if after is not None:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
