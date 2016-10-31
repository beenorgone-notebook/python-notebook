# get html link as <a ... href="..." ... >
html_link_regex = \
    re.compile('<a\s(?:.*?\s)*?href=[\'"](.*?)[\'"].*?>')
