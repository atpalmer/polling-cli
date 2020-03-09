import json
import click
from .clients import HuffpoClient


def pretty_dumps(data):
    return json.dumps(data, indent=2)


@click.command()
def main():
    client = HuffpoClient()
    result = client.polls()
    print(pretty_dumps(result))

