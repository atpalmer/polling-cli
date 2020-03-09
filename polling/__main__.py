import json
from .clients import HuffpoClient


def pretty_dumps(data):
    return json.dumps(data, indent=2)


def main():
    client = HuffpoClient()
    result = client.polls()
    print(pretty_dumps(result))


if __name__ == '__main__':
    main()
