from zlib import *

x1=200
y1=0
x2=300
y2=50
x3=200
y3=100
x4=100
y4=50
x5=100
y5=125
x6=300
y6=125
ix=200
iy=175
x7=200
y7=75

line(x1,y1,x2,y2)
line(x4,y4,x1,y1)
line(x4,y4,x3,y3)
line(x3,y3,x2,y2)
line(x5,y5,ix,iy)
line(ix,iy,x6,y6)
vline(x4,y4,y5)
vline(x3,y3,iy)
vline(x2,y2,y6)
vline(x1,y1,y7)
line(x5,y5,x7,y7)
line(x7,y7,x6,y6)