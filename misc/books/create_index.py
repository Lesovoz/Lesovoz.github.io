#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path
from urllib.parse import  quote_plus


cur_dir = Path(__file__).parent

for dir in sorted(cur_dir.rglob('')):
    if dir.is_dir():
        with open(dir / 'index.html', 'w') as idx:
            print('========', dir, '========')

            hrefs = "<br>\n".join(f'''<a href="{quote_plus(f.name, encoding='utf8')}">{f.name}</a>''' for f in sorted(dir.iterdir()) if f.name != 'index.html' and not f.name.endswith('.py'))

            txt = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>listing</title>
</head>
<body>            

{hrefs}

</body>
</html>
'''
            print(txt)
            idx.write(txt)
