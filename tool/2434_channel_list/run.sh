#!/bin/bash

CURRENT_DIR=$(cd $(dirname $0); pwd)
ROOT_DIR=${CURRENT_DIR}/../..
RESOURCE_DIR=${ROOT_DIR}/resource

python main.py > ${RESOURCE_DIR}/2434_channel_list.json
