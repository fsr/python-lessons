#!/usr/bin/env python3

import json
import os
import subprocess
from collections import OrderedDict

reveal_config = OrderedDict()
template = []
index = ''


def main():
    global index
    if not os.path.isdir('html'):
        print('Please run ./install.sh first')
        exit()
    load()
    for title in reveal_config:
        source = reveal_config[title]['source']
        theme = reveal_config[title]['theme']
        destination = 'html/{source}.html'.format(source=source)
        subprocess.call(['pandoc', '-t', 'revealjs', '-s',
                         '--template', 'md/template.html',
                         'md/{}.md'.format(source), '--no-highlight',
                         '--variable', 'theme={}'.format(theme),
                         '--variable', 'pagetitle={}'.format(title),
                         '-o', 'html/{}.html'.format(source)])
        index += index_link.format(link=source + '.html', title=title)
    generated_index = index_content.format(links=index)
    new_index = ''
    for line in template:
        new_index += line.replace('{content}', generated_index)
    with open('html/index.html', 'w') as indexfile:
        indexfile.write(new_index)


def load():
    global reveal_config, template
    try:
        with open('reveal.json') as json_data:
            configdata = json.load(json_data)
            for i in range(1, len(configdata) + 1):
                search = str(i) if i > 9 else '0' + str(i)
                for title in configdata:
                    if configdata[title]['source'].startswith(search):
                        reveal_config[title] = configdata[title]
    except FileNotFoundError:
        print('No reveal.json found.')
        exit()
    try:
        with open('src/index.html') as template_file:
            template = template_file.readlines()
    except FileNotFoundError:
        print('No src/index.html found.')
        exit()


index_content = '''<section><h1 class="title">Index</h1><ul>{links}</ul></section>'''

index_link = '''<li><a href="{link}">{title}</a></li>\n'''


if __name__ == '__main__':
    main()
