#!/usr/bin/python3
"""
Queries the Reddit API and
returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers (not active users, total subscribers)
    for a given subreddit.
    If an invalid subreddit is given, the function returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Python/requests'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    elif response.status_code == 302:
        return 0
    elif response.status_code == 404:
        return 0
    else:
        return 0
