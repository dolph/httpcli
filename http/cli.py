"""
Python HTTP CLI Client

"""

import argparse


def get_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('method', metavar='<http-method>', type=str,
            help='HTTP method to use (OPTIONS, GET, HEAD, POST, PUT, DELETE, '
                 'TRACE, CONNECT)')
    parser.add_argument('url', metavar='<url>', type=str,
            help='URL to work with')
    parser.add_argument('body', metavar='<body>', nargs='?',
            help='Request body')
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
            help='show verbose output')
    return parser


def parse_args(parser):
    return parser.parse_args()
