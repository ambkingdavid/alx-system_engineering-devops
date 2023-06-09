#!/usr/bin/python3
"""
    Query reddit
"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom User Agent"}
    params = {"limit": 100, "after": after} if after else {"limit": 100}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        articles = data["data"]["children"]
        for article in articles:
            title = article["data"]["title"].lower()
            for word in word_list:
                if word.lower() in title:
                    word_count[word] = word_count.get(word, 0) + 1

        after = data["data"]["after"]
        if after:
            count_words(subreddit, word_list, after, word_count)
        else:
            sorted_counts = sorted(word_count.items(),
                                   key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print("Invalid subreddit or no posts match.")
