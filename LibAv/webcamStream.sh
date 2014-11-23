#!/bin/sh
#avserver -f avserver.conf
avserver
avconv  -f video4linux2 -i /dev/video1 http://localhost:8090/feed1.ffm