from httpcli import content


def print_title(string):
    print(string)


def print_list(l):
    for x in l.iteritems():
        print(x)
    print('')


def print_dict(d):
    for header, value in d.iteritems():
        print('%s: %s' % (header.title(), value))
    print('')


def print_content(string, extra_newline=False):
    """Attempts to pretty print whatever string is provided."""
    if string is not None:
        print(content.get_pretty(string))
        if extra_newline:
            print('')
