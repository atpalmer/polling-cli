import requests


def url(path):
    return f'https://elections.huffingtonpost.com/pollster/api/v2/{path}'


class HuffpoClient(object):
    def polls(self):
        response = requests.get(url('polls'))
        response.raise_for_status()
        return response.json()

