from httpcli import cli
from httpcli import client
from httpcli import content
from httpcli import output


def main():
    parser = cli.get_parser()
    namespace = cli.parse_args(parser)
    namespace.headers = dict(namespace.headers)

    # set request content type automatically, unless user-specified
    content_type = content.detect_content_type(namespace.body)
    if content_type is not None:
        namespace.headers.setdefault('Content-Type', content_type)

    response, body = client.request(
        namespace.method,
        namespace.url,
        body=namespace.body,
        headers=namespace.headers)

    if not namespace.terse:
        # show request info
        output.print_title('%s %s' % (namespace.method.upper(), namespace.url))
        output.print_dict(namespace.headers)
        output.print_content(namespace.body, extra_newline=True)

        # show response info
        output.print_title('%s %s' % (response.status, response.reason))
        output.print_dict(response)

    output.print_content(body)

    if response.status >= 400:
        raise SystemExit(1)
