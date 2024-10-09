#!/bin/zsh

dbus-send --print-reply --dest=org.freedesktop.DBus /org.freedesktop.DBus.ListNames \
  | grep -Eo 'org.mpris.MediaPlayer2.[^"]+' | nl -ba -s\: -w1

