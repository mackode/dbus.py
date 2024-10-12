#!/usr/bin/env python3

import dbus

def seek(bus, name, seek_interval):
    player = bus.get_object(name, "/org/mpris/MediaPlayer2")
    player_iface = dbus.Interface(player, dbus_interface="org.mpris.MediaPlayer2.Player")
    player_iface.Seek(seek_interval * 1e6)

bus = dbus.SessionBus()
dbus_daemon = bus.get_object("org.freedesktop.DBus", "/")
dbus_iface = dbus.Interface(dbus_daemon, dbus_interface="org.freedesktop.DBus")

names = dbus_iface.ListNames()
for name in names:
    if name.startswith("org.mpris.MediaPlayer2"):
        seek(bus, name, -10)

