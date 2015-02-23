<?php
header('Access-Control-Allow-Origin','*');
exec('streamer -q -c /dev/video0 -o shot.jpeg');
echo 'shot.jpeg?t='.time();
?>


