#!/usr/bin/python3
"""
function that queries the Reddit API
returns the number of sububscribers for a given subreddit
"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """Returns a list of titles of all hot posts on a given subreddit"""
    username = 'mistidevs'
    password = 'Misati@2004'
    user_pass_dict = {'user': username, 'passwd': password, 'api_type': 'json'}
    headers = {'user-agent': '/u/mistidevs API Python for Holberton School'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False)
    if r.status_code == 200:
        return (r.json()["data"]["subscribers"])
    else:
        return(0)
