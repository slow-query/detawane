# upcoming_videos

upcoming_videos is script that gets upcoming videos from specified chanenl list.

set environments.

```
cp .envrc.sample .envrc
```

run script, and output [json file](./../../resource/2434_upcoming_video_list.json).

```shell
./run.sh
```

## Issue

Occurs an error when channel list is full, because quota of youtube api is few.

workaround is that halves channel list.
