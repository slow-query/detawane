#!/usr/bin/env python

import argparse
import json
import os
from datetime import datetime

from googleapiclient.discovery import build

YOUTUBE_API_KEY = os.environ["YOUTUBE_API_KEY"]


class Channel:
    def __init__(self, id, title):
        self.id = id
        self.title = title


class Video:
    def __init__(self, channel, id, title, start_at, chat_id):
        self.channel = channel
        self.id = id
        self.title = title
        self.start_at = start_at
        self.chat_id = chat_id


def dump(video):
    return {
        "id": video.id,
        "title": video.title,
        "start_at": str(video.start_at),
        "chat_id": video.chat_id,
        "channel": {"id": video.channel.id, "title": video.channel.title},
    }


def fetch_by_channel(channel_id):
    youtube_client = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

    res = (
        youtube_client.search()
        .list(part="id", channelId=channel_id, eventType="upcoming", type="video")
        .execute()
    )
    video_ids = [x["id"]["videoId"] for x in res["items"]]

    videos = []
    for video_id in video_ids:
        res = (
            youtube_client.videos()
            .list(part="snippet, liveStreamingDetails", id=video_id)
            .execute()
        )
        start_at = datetime.strptime(
            res["items"][0]["liveStreamingDetails"]["scheduledStartTime"],
            "%Y-%m-%dT%H:%M:%S%z",
        )
        chat_id = res["items"][0]["liveStreamingDetails"]["activeLiveChatId"]
        title = res["items"][0]["snippet"]["title"]
        channel_title = res["items"][0]["snippet"]["channelTitle"]
        channel = Channel(channel_id, channel_title)
        videos.append(Video(channel, video_id, title, start_at, chat_id))

    return videos


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("channel_id", type=str, help="channel id")
    args = parser.parse_args()

    videos = fetch_by_channel(args.channel_id)
    print(json.dumps([dump(video) for video in videos], indent=2, ensure_ascii=False))
