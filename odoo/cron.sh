#!/bin/sh
cd "$(dirname "$0")";
CWD="$(pwd)"
echo $CWD
python cron.py