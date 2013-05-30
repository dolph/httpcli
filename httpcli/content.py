import json


CONTENT_TYPES = {
    'json': 'application/json',
    'text': 'text/plain'
}


def detect_content_type(string):
    if string is None:
        return None

    try:
        json.loads(string)
        return CONTENT_TYPES['json']
    except:
        pass

    return CONTENT_TYPES['text']


def get_pretty(string):
    """Attempts to return a pretty printed version of provided string."""
    content_type = detect_content_type(string)

    if content_type == CONTENT_TYPES['json']:
        d = json.loads(string)
        return json.dumps(d, indent=2)
    else:
        return string
