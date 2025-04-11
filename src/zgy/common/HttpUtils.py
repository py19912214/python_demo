import requests


def get(url, params, headers):
    print(url)
    return requests.get(url, params=params, headers=headers)


def post(url, params, headers):
    print(url)
    print(headers)
    return requests.post(url, json=params, headers=headers, verify=False)


def postFile(url, files, headers):
    print(url)
    return requests.post(url, files=files, headers=headers, verify=False)
