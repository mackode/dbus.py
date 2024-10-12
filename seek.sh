#!/bin/zsh

while :; do
  dbus-send --type=method_call --dest=org.mpris.MediaPlayer2.qmmp /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Seek int64:-100000
  sleep 1
done

