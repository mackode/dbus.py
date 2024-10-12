#!/usr/bin/env python3

import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

def signal_received(iface_name, changed, invalidated, name):
    if iface_name == "org.mpris.MediaPlayer2.Player" and changed.get("PlaybackStatus") == "Playing":
        print("Application %s is playing" % name)

DBusGMainLoop(set_as_default=True)

bus = dbus.SessionBus()
bus.add_signal_receiver(path="/org/mpris/MediaPlayer2", dbus_interface="org.freedesktop.DBus.Properties", signal_name="PropertiesChanged", handler_function=signal_received, sender_keyword="name")

loop = GLib.MainLoop()
loop.run()

