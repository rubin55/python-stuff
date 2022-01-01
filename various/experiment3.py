import pulsectl
pulse = pulsectl.Pulse()

for source in pulse.source_list():
    print(f"Source {source.index} mute state is: {source.mute}")
    pulse.mute(source)


for source in pulse.source_list():
    print(f"Source {source.index} mute state is: {source.mute}")
