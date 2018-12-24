#!/usr/bin/env python
# -*- coding: utf-8 -*-
import html
import os
import sys
import urllib
from pathlib import Path
from urllib.parse import quote_plus


def list_directory(path):
    list = sorted(os.listdir(path), key=lambda a: a.lower())
    r = []
    try:
        displaypath = urllib.parse.unquote(path, errors='surrogatepass')
    except UnicodeDecodeError:
        displaypath = urllib.parse.unquote(path)
    displaypath = html.escape(displaypath, quote=False).rsplit('/')[-1]
    enc = sys.getfilesystemencoding()
    title = '📁 %s' % displaypath
    r.append('<!DOCTYPE HTML>\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=%s">' % enc)
    r.append('<title>%s</title>\n</head>' % title)
    r.append('<body>\n<h1>%s</h1>' % title)
    r.append('<hr>\n<ul>')
    for name in list:
        if name in {'index.html', 'create_index.py'}:
            continue
        fullname = os.path.join(path, name)
        displayname = linkname = name
        # Append / for directories or @ for symbolic links
        if os.path.isdir(fullname):
            displayname = name + "/"
            linkname = name + "/"
        if os.path.islink(fullname):
            displayname = name + "@"
            # Note: a link to a directory displays with @ and links with /
        r.append('<li><a href="%s">%s</a></li>' % (urllib.parse.quote(linkname, errors='surrogatepass'),
                                                   html.escape(displayname, quote=False)))
    r.append('</ul>\n<hr>\n</body>\n</html>\n')
    encoded = '\n'.join(r)  # .encode(enc, 'surrogateescape')
    return encoded


cur_dir = Path(__file__).parent

for dir in sorted(cur_dir.rglob('')):
    if dir.is_dir():
        print(list_directory(dir._str))
        with open(dir / 'index.html', 'w') as idx:
            print('========', dir, '========')
            idx.write(list_directory(dir._str))

#
#         with open(dir / 'index.html', 'w') as idx:
#             print('========', dir, '========')
#
#             hrefs = "<br>\n".join(f'''<a href="{quote_plus(f.name, encoding='utf8')}">{f.name}</a>''' for f in sorted(dir.iterdir()) if
#                                   f.name != 'index.html' and not f.name.endswith('.py'))
#
#             txt = f'''<!DOCTYPE html>
# <html>
# <head>
#     <meta charset='utf-8'>
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>listing</title>
# </head>
# <body>
#
# {hrefs}
#
# </body>
# </html>
# '''
#             print(txt)
#             idx.write(txt)
