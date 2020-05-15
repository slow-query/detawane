#!/usr/bin/env python
# coding: utf-8

import json
from pyquery import PyQuery

query = PyQuery('https://nijisanji.ichikara.co.jp/member/')
member_urls = [element.get('href') for element in list(query("#liver_list a"))]

member_list = []
for member_url in member_urls:
    query = PyQuery(member_url)

    member_name_raw = query('title').text()
    member_name = member_name_raw.split(' ')[0]

    channel_url_raw = query('.elementor-social-icon-youtube')[0].get('href')
    channel_url = channel_url_raw.split('?')[0]

    member_list.append({ 'name': member_name, 'url': channel_url })

print(json.dumps(sorted(member_list, key = lambda x: x['name']), indent = 2, ensure_ascii = False))
