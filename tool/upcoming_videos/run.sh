#!/bin/bash

CURRENT_DIR=$(cd $(dirname $0); pwd)
ROOT_DIR=${CURRENT_DIR}/../..
RESOURCE_DIR=${ROOT_DIR}/resource
CHANNEL_LIST_FILE=${RESOURCE_DIR}/2434_channel_list.json

python main.py ${CHANNEL_LIST_FILE} > ${RESOURCE_DIR}/2434_upcoming_video_list.json
