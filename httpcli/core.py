from httpcli import cli
from httpcli import client
from httpcli import content
from httpcli import output


def main():
    parser = cli.get_parser()
    namespace = cli.parse_args(parser)
    namespace.headers = dict(namespace.headers)

    # set request content type automatically, unless user-specified
    namespace.headers['Content-Type'] = namespace.headers.get('Content-Type',
            content.detect_content_type(namespace.body))

    response, body = client.request(
            namespace.method,
            namespace.url,
            body=namespace.body,
            headers=namespace.headers)

    if namespace.verbose:
        # show request info
        output.print_title('%s %s' % (namespace.method.upper(), namespace.url))
        output.print_dict(namespace.headers)
        output.print_content(namespace.body)

        # show response info
        output.print_title('%s %s' % (response.status, response.reason))
        output.print_dict(response)

    output.print_content(body)
