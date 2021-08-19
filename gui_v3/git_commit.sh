#! /bin/bash
cd ~/Archive
git add .
Date=$(date '+%Y-%m-%d %T')
git commit -am "Jetson Nano ${Date}"
