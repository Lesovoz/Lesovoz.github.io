#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path
from urllib.parse import  quote_plus


cur_dir = Path(__file__).parent

for dir in sorted(cur_dir.rglob('')):
    if dir.is_dir():
        with open(dir / 'index.html', 'w') as idx:
            print('========', dir, '========')

            hrefs = "<br>\n".join(f'<a href="{quote_plus(f.name)}">{f.name}</a>' for f in sorted(dir.iterdir()) if f.name != 'index.html' and not f.name.endswith('.py'))

            txt = f'''<!DOCTYPE html>
<html>
<body>            

{hrefs}

</body>
</html>
'''
            print(txt)
            idx.write(txt)
