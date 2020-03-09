import json
import click
from .clients import HuffpoClient


def pretty_dumps(data):
    return json.dumps(data, indent=2)


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

