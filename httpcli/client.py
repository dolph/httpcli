import httplib2


def request(method, url, body=None, headers=None):
    client = httplib2.Http()

    response, content = client.request(
        url, method.upper(), body=body, headers=headers)

    return response, content
