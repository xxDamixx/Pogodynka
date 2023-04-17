 #Autor: Popławski Damian
 # -*- coding: utf-8 -*-
 #! /bin/sh
# /etc/init.d/skrypt
 
### BEGIN INIT INFO
# Provides:          Skrypt
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Skrypt
# Description:       Skrypt
### END INIT INFO

case "$1" in
  start)
    echo "Starting skrypt"
    # run application you want to start
    python /usr/local/sbin/program.py &
    ;;
  stop)
    echo "Stopping skrypt"
    # kill application you want to stop
    killall python
    ;;
  *)
    echo "Usage: /etc/init.d/skrypt{start|stop}"
    exit 1
    ;;
esac
 
exit 0
