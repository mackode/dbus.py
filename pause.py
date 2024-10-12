#!/usr/bin/env python3

import dbus

def pause_playback(bus, name):
    player = bus.get_object(name, "/org/mpris/MediaPlayer2")
    player_iface = dbus.Interface(player, dbus_interface="org.mpris.MediaPlayer2.Player")
    player_iface.Pause()

bus = dbus.SessionBus()
dbus_daemon = bus.get_object("org.freedesktop.DBus", "/")
dbus_iface = dbus.Interface(dbus_daemon, dbus_interface="org.freedesktop.DBus")

names = dbus_iface.ListNames()
for name in names:
    if name.startswith("org.mpris.MediaPlayer2"):
        pause_playback(bus, name)

