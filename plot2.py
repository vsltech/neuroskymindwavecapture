import time
import mindwave, time
import pyqtgraph as pg
import numpy as np
import mindwave, time
then = time.time()

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



x = np.arange(100)
y = np.arange(100)
x[0] = 0.0000
y[0] = 0.0000

pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')
pw = pg.plot()
while True:
    time.sleep(0.5)
    i = 0
    now = time.time()
    duration = now - then
    duration_scale = duration * 10
    x[i] = headset.raw_value
    y[i] = duration_scale
    print x[i],y[i]
    i = i+1
    pw.plot(x, y, pen=pg.mkPen('b', width=2), label= 'EEG RAW Data', clear=False)
    pg.QtGui.QApplication.processEvents()
