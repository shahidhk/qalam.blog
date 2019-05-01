import yaml
import re
import os

yaml_file = 'site/static/admin/config.yml'
dir = 'site/content/categories'
index_file = '_index.md'
matter = """---
title: {}
---
"""

def slugify(value):
   slug = value.lower()
   slug = re.sub(r'[^a-z0-9 ]+', '', slug)
   slug = slug.replace(' ', '-')
   return slug

def main():
    with open(yaml_file, 'r') as stream:
        config = yaml.safe_load(stream)

        categories = config['collections'][0]['fields'][2]['options']
        
        for c in categories:
            d = os.path.join(dir, slugify(c))
            f = os.path.join(d, index_file)
            if not os.path.exists(d):
                os.makedirs(d)
            if not os.path.exists(f):
                with open(f, 'w') as w:
                    w.write(matter.format(c))

if __name__=='__main__':
    main()

