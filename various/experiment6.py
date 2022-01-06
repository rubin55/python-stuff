from dbus_next.aio import MessageBus

import asyncio

loop = asyncio.get_event_loop()


async def main():
    bus = await MessageBus().connect()

    introspection = await bus.introspect('org.gnome.Shell', '/org/gnome/Shell')

    obj = bus.get_proxy_object('org.gnome.Shell', '/org/gnome/Shell', introspection)
    properties = obj.get_interface('org.freedesktop.DBus.Properties')

    def on_properties_changed(interface_name, changed_properties, invalidated_properties):
        for changed, variant in changed_properties.items():
            print(f'property changed: {changed} - {variant.value}')

    print(properties)
    await loop.create_future()

loop.run_until_complete(main())
