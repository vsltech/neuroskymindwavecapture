import mindwave, time

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
    time.sleep(.5)
    print "Attention: %s, Meditation: %s, Raw: %s" % (headset.attention, headset.meditation, headset.raw_value)

