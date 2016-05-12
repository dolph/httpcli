"""
Python HTTP CLI Client

"""

import argparse


def get_parser():
    parser = argparse.ArgumentParser(description=__doc__)

    # optionals
    parser.add_argument(
        '-t', '--terse', action='store_true', default=False,
        help='Only show the response body')

    # positionals
    parser.add_argument(
        'method', type=str,
        help='HTTP method to use (OPTIONS, GET, HEAD, POST, PUT, DELETE, '
             'TRACE, CONNECT)')
    parser.add_argument(
        'url', type=str, help='URL to work with')
    parser.add_argument(
        'body', nargs='?', help='Request body')
    parser.add_argument(
        'headers', nargs=argparse.REMAINDER, type=headers,
        help='Additional request headers (keyword=value)')

    return parser


def headers(string):
    msg = ('must be formatted as optional keyword arguments, '
           'e.g. --content-type=application/json')

    try:
        header, value = string.split('=', 1)
    except ValueError:
        # validate --keyword=value format
        raise argparse.ArgumentTypeError(msg)

    # validate --double-hyphen-prefixes
    if header[:2] != '--':
        raise argparse.ArgumentTypeError(msg)

    # normalize header names
    return header[2:].title(), value


def parse_args(parser):
    return parser.parse_args()
