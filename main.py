import json
import requests

def url(path):
    return f'https://elections.huffingtonpost.com/pollster/api/v2/{path}'

def dumps(data):
    return json.dumps(data, indent=2)

def main():
    response = requests.get(url('polls'))
    print(dumps(response.json()))

if __name__ == '__main__':
    main()
