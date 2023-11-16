from casioplot import *

def line(x1,y1,x2,y2):
  dx1=x2-x1
  dy1=y2-y1
  x=x1
  y=y1
  p1=(2*dy1)-dx1
  
  while (x<=x2):
    set_pixel(x,y)
    
    if y1<=y2:  
      if x1<x2:              
        if p1>=0:
          p1+=2*(dy1-dx1)
          x+=1
          y+=1
        if p1<0:
          x+=1
          p1+=(2*dy1)
      
    if y1>y2:  
      if x1<x2:              
        if p1>0:
          p1-=(2*dx1)
          x+=1
          y-=1
        if p1<=0:
          x+=1
          p1-=(2*dy1-dx1)      

def vline(x1,y1,y2):
  y=y1
  x=x1
  while (y<=y2):
    set_pixel(x,y)
    y+=1
    
   
show_screen()
