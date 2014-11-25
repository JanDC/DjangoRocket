#!/bin/sh
sudo pkill avserver
#avserver -f avserver.conf &
avserver &
sleep 2
sudo avconv  -f video4linux2 -i /dev/video0 http://localhost:8090/feed1.ffm
