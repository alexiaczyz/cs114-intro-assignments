#!/usr/bin/env python
# coding: utf-8

# In[2]:


from unittest.mock import Mock
import typing
## Write the trajectory function here


def trajectory(xv:float, yv:float, xa:float, ya:float, tx:float, tw:float, ty:float, th:float,delta:float, cb:typing.Callable)->bool:
    """
    takes a rockets initial velocity components as (xv,yv)
    takes a rockets initial acceleration components as (xa,ya)
    takes targets corner to be positioned at (x,y)=(tx,ty)
    target is tw units wide and tw units tall
    
    trajectory tells you if its true that the rocket hits the target!
    """
    
    GRAVITY = -9.8
    #starts at origin
    x=0.0
    y=0.0
    
    #hits target when:
    #tx<= x <= (tx+tw) and ty<= y <= (ty+th)
    
    #loops while rocket is either above the ground or hasnt hit target yet 
    while y>=0 and not(tx<= x <= (tx+tw) and ty<= y <= (ty+th)):
    #ITERATING VELOCITY    
    #v=v0+aΔt
    #in the x direction:  vx=vx0 + xa(Δt)
        xv=xv+(xa*delta)
    #in the y direction:  vy=vy0 + ya(Δt)
        yv=yv+((ya+GRAVITY)*delta)
    
    #ITERATING POSITION
        x=(xv*delta) +x
        y=(yv*delta) +y
    
        cb(x,y)
    #returns if target was hit
    return (tx<= x <= (tx+tw) and ty<= y <= (ty+th))



## Here are some tests. Add your own tests as well; don't just count on ours!
assert trajectory(10, 10, 0, 0, 1, 1, 1, 1, 0.001, Mock()), "Simple hit"
assert not trajectory(10, 10, 0, 0, 3, 1, 1, 1, 0.001, Mock()), "Simple miss"
assert trajectory(10, 10, -8.5, 0, 3, 1, 1, 1, 0.001, Mock())
assert not trajectory(10, 10, -8.5, 0, 3, 1, 0.00001, 0.00001, 0.001, Mock()),"smallest target ever"


# In[ ]:




