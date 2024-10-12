#!/bin/zsh

dbus-send --type=method_call --dest=org.mpris.MediaPlayer2.qmmp /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause

