#! /bin/bash
ps -af > process_all.txt
awk '/rqt/' process_all.txt > process_particular.txt
kill -9 `awk '{print $2}' process_particular.txt`
echo "RQT Off!!"
