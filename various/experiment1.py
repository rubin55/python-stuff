# dbus-monitor --session "type='signal',sender=':1.11',destination=':1.41',path='/org/gnome/Shell',interface='org.gnome.Shell',member='AcceleratorActivated'"
# dbus-monitor --session "type='method_call',sender=':1.41',destination=':1.11',path='/org/gnome/Shell',interface='org.gnome.Shell',member='ShowOSD'"

import dbus
from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop


def signal_handler(*args, **kwargs):
    for i, arg in enumerate(args):
        print("arg:%d        %s" % (i, str(arg)))
    print('kwargs:')
    print(kwargs)
    print('---end----')


DBusGMainLoop(set_as_default=True)
bus = dbus.SessionBus()
bus.add_signal_receiver(signal_handler,
                        signal_name=None,
                        dbus_interface=None,
                        bus_name=None,
                        path=None)

loop = GLib.MainLoop()
loop.run()
