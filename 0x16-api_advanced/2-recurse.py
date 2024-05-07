#!/usr/bin/python3
"""
function that queries the Reddit API
returns a list containing the titles 
of all hot articles for a given subreddit
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function to retrieve hot article titles for a subreddit.

    Args:
        subreddit (str): The subreddit name.
        hot_list (list, optional): The list to store hot article titles.
        after (str, optional): The fullname of the last retrieved item for pagination.

    Returns:
        list or None: A list of hot article titles, or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(url, headers={"User-Agent": "Python:reddit-hot-titles:v1.0"}, params=params)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return None
        else:
            raise e

    data = response.json()

    if "error" in data:
        return None

    for post in data["data"]["children"]:
        hot_list.append(post["data"]["title"])

    after = data["data"]["after"]
    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
