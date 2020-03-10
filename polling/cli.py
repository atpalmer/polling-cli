import json
from json import JSONEncoder
import click
from .clients import HuffpoClient


class _Encoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, set):
            return list(o)
        return super().default(o)


def pretty_dumps(data):
    return json.dumps(data, indent=2, cls=_Encoder)


@click.group()
def main():
    pass


@main.group()
def polls():
    pass


@polls.command()
def raw():
    client = HuffpoClient()
    result = client.polls()
    print(pretty_dumps(result))


@click.option('--house', default=None)
@polls.command()
def search(house):
    client = HuffpoClient()
    result = client.polls()
    filtered = [i for i in result['items'] if i['survey_house'] == house]
    print(pretty_dumps(filtered))


@polls.group()
def options():
    pass


@options.command()
def house():
    client = HuffpoClient()
    result = client.polls()
    options = {i.get('survey_house') for i in result['items']}
    print(pretty_dumps(options))

