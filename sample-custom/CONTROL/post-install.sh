#!/bin/sh

APKG_PKG_DIR=/usr/local/AppCentral/sample-custom-apk

case "$APKG_PKG_STATUS" in

	install)
		# post install script here
		;;
	upgrade)
		# post upgrade script here (restore data)
		# cp -af $APKG_TEMP_DIR/* $APKG_PKG_DIR/etc/.
		;;
	*)
		;;

esac

exit 0
