from http import cli
from http import client
from http import output


def main():
    parser = cli.get_parser()
    namespace = cli.parse_args(parser)

    headers = {'accept': 'application/json'}

    response, content = client.request(
            namespace.method,
            namespace.url,
            body=namespace.body,
            headers=headers)

    if namespace.verbose:
        # show request info
        output.print_title('%s %s' % (namespace.method.upper(), namespace.url))
        output.print_dict(headers)
        output.print_content(namespace.body)

        # show response info
        output.print_title('%s %s' % (response.status, response.reason))
        output.print_dict(response)

    output.print_content(content)
