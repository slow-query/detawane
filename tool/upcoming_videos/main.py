#!/usr/bin/env python
# NOTE: Youtube Data API v3の1日のリクエスト上限値が小さいため100件程度で上限に達する。

import argparse
import os
import json
import upcoming_video

parser = argparse.ArgumentParser()
parser.add_argument('file_path', type=str, help='channel list file')
args = parser.parse_args()

fp = open(args.file_path, 'r')
channels = json.load(fp)

output = []
for channel in channels:
    # NOTE: 公式ページから取得したURLに最後に/がついているものが存在した
    id = channel['url'].split('/')[-1] or channel['url'].split('/')[-2]
    name = channel['name']

    videos = upcoming_video.fetch_by_channel(id)
    output.append({
        'id': id,
        'name': name,
        'videos': [upcoming_video.dump(video) for video in videos]
    })

print(json.dumps(output, indent=2, ensure_ascii=False))
