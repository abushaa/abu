from pylab import plot, clf, ion, draw
from matplotlib import mlab
import math

a=[15]

T=mlab.frange(-20, 20, 0.01)
ion()
for i in range (100):
    x=[math.sin(a[0]*t+i/5) for t in T]
    y=[math.cos(2*t) for t in T]
    clf()
    plot(x,y)
    draw()
