import json
import requests


def url(path):
    return f'https://elections.huffingtonpost.com/pollster/api/v2/{path}'


class HuffpoClient(object):
    def polls(self):
        response = requests.get(url('polls'))
        response.raise_for_status()
        return response.json()


def pretty_dumps(data):
    return json.dumps(data, indent=2)


def main():
    client = HuffpoClient()
    result = client.polls()
    print(pretty_dumps(result))


if __name__ == '__main__':
    main()
