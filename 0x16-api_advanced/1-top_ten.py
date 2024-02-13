#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Get and print the titles of the first 10 hot posts for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyCustomUserAgent/1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts[0:10]:
            print(post['data']['title'])
    else:
        print(None)
