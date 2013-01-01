#!/bin/bash

cd ~/selenv
export DISPLAY=:0
Sel_ver=selenium-server-standalone-2.28.0.jar
Xvfb=$(ps aux | awk '{if ($11 == "Xvfb") print $12}')
Selen=$(ps aux | grep -v grep | grep $Sel_ver | awk '{print $2}')
Selen_count=$(echo $Selen | wc -w)

if [[ "$Xvfb" != ":99" || $Selen_count < 2 ]] 
  then
    killall Xvfb
    kill $Selen
    nohup xvfb-run java -jar $Sel_ver &
fi

/usr/bin/zabbix_sender -z 127.0.0.1 -i <(bin/python syw.py)
