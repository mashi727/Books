import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

win = pg.GraphicsLayoutWidget(show=True)
win.resize(400,350)
win.setWindowTitle('pyqtgraph example: Histogram')
plt1 = win.addPlot()

## make interesting distribution of values
vals = np.hstack([np.random.normal(size=500), np.random.normal(size=260, loc=4)])

## compute standard histogram
y,x = np.histogram(vals, bins=np.linspace(-3, 8, 40))

## Using stepMode="center" causes the plot to draw two lines for each sample.
## notice that len(x) == len(y)+1
plt1.plot(x, y, stepMode="center", fillLevel=0, fillOutline=True, brush=(0,0,255,150))


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    QtGui.QApplication.instance().exec_()

