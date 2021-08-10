#! /bin/bash
ps -af > process_all.txt
awk '/faceScan.py/' process_all.txt > process_particular.txt
kill -9 `awk '{print $2}' process_particular.txt`
echo "Camera Off!!"
