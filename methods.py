#!/usr/bin/env python3

import dbus

bus = dbus.SessionBus()
dbus_daemon = bus.get_object("org.freedesktop.DBus", "/")
dbus_iface = dbus.Interface(dbus_daemon, dbus_interface="org.freedesktop.DBus")

names = dbus_iface.ListNames()
for name in names:
    if name.startswith("org.mpris.MediaPlayer2"):
        print(name)

