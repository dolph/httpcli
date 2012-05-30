=======
httpcli
=======

Just another command line HTTP client (in the spirit of cURL).

Example Usage
=============

HTTP verbs are specified as a positional argument, followed by the URL to be
acted on. The goal is to reflect the feel of a standard HTTP header. For
example::

    $ http get http://localhost/

To provide a request body (e.g. for a POST or PUT), use the third positional
argument::

    $ http post http://localhost/documents '{"json": "document"}'

Arbitrary request headers can be specified as CLI args::

    $ http get http://localhost/ --x-forwarded-for=10.0.0.50

This would be translated as `X-Forwarded-For: 10.0.0.50` in the subsequent HTTP
request. To illustrate this, we can enable verbose output::

    $ http --verbose get http://localhost/ --x-forwarded-for=10.0.0.50

    GET http://localhost/
    =====================

    X-Forwarded-For: 10.0.0.50

    200 OK
    ======

    Status: 200
    Content-Length: 396
    Content-Location: http://localhost/
    Date: Wed, 30 May 2012 19:26:03 GMT
    Content-Type: application/json

    {
      "documents": [
        {
          "id": "c1be0fde3c0f4d27be15e1e3812cfd65b58325c3",
          "value": "a"
        },
        {
          "id": "67dc85dceacd3734ae53f1a69f56785dfe4c4c71",
          "value": "b"
        }
      ]
    }

Built-In Help
=============

Example help output::

    $ http --help
    usage: http [-h] [-v] method url [body] ...

    Python HTTP CLI Client

    positional arguments:
    method         HTTP method to use (OPTIONS, GET, HEAD, POST, PUT, DELETE,
                    TRACE, CONNECT)
    url            URL to work with
    body           Request body
    headers        Additional request headers (keyword=value)

    optional arguments:
    -h, --help     show this help message and exit
    -v, --verbose  show verbose output

