import requests


def get(url, params, headers):
    return requests.get(url, params=params, headers=headers)

def post(url, params, headers):
    return requests.post(url, json=params, headers=headers)
