#!/bin/sh

. /etc/script/lib/command.sh

APKG_PKG_DIR=/usr/local/AppCentral/sample-custom-apk
PID_FILE=/var/run/demo-web-server.pid

JAVA_CMD=/usr/local/bin/java

case $1 in

	start)
		# start script here
		cd $APKG_PKG_DIR/lib/
		$JAVA_CMD WebServer $APKG_PKG_DIR/webapp/ 7777 > /dev/null &
		echo $! > $PID_FILE
		;;

	stop)
		# stop script here
		kill -9 `cat $PID_FILE` 2> /dev/null
		rm -rf $PID_FILE
		;;

	*)
		echo "usage: $0 {start|stop}"
		exit 1
		;;
		
esac

exit 0
