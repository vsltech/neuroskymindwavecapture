import numpy as np
import matplotlib.pyplot as plt
import mindwave, time


then = time.time()
now = time.time()

plt.axis([-2000, 2000, 0, 50])
plt.ion()

headset = mindwave.Headset('COM10', 'CC0E')
time.sleep(2)

headset.connect()
print "Connecting..."

while headset.status != 'connected':
    time.sleep(0.5)
    if headset.status == 'standby':
        headset.connect()
        print "Retrying connect..."
print "Connected."

while True:
    #time.sleep(.5)
    print "Attention: %s, Meditation: %s, Raw: %s" % (headset.attention, headset.meditation, headset.raw_value)
    now = time.time()
    duration = now - then
    duration_sec = duration % 60
    x = str(headset.raw_value)
    y = str(duration_sec)
    plt.scatter(x, y)
    plt.pause(0.05)

while True:
    plt.pause(0.05)

