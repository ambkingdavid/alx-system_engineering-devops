#!/usr/bin/python3
"""
    function that queries the Reddit API and returns the
    number of subscribers for a given reddit
"""


import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers of a subreddit
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "Fake Agent"
            }
    response = requests.get(url, headers=headers)
    outcome = response.json()
    if response.status_code != 200:
        data = 0
    else:
        data = outcome.get('data').get('subscribers')
    return data
