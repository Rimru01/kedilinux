if [ "$(id -un)" = kedi ] && [ "$(tty)" = /dev/tty1 ] && [ -z "$DISPLAY" ]; then
    startx /usr/bin/startlxqt
fi
