#!/usr/bin/env python
# coding: utf-8

# In[2]:


## Constants
PASTE_LITRES_PER_SQUARE_METRE = 0.15
PASTE_LITRES_PER_BUCKET = 4.0
WALLPAPER_SQUARE_METRES_PER_ROLL = 5.0


## Write the wallpaper_price function here
import math

def wallpaper_price(width:float, height:float, paste_price:int, wallpaper_price:int)->int:
    """
    Given a width and height value for a wall, this function returns the cost in cents 
    that it would take to apply wallpaper to it. 
    paste_price is the given price for a bucket of paste in cents
    wallpaper_price is the given price for a roll of wallpaper in cents
    """
    #ensuring no negative values
    assert width>= 0
    assert height>= 0
    assert paste_price>= 0 
    assert wallpaper_price>= 0
    
    Area= width*height
    
    Lneeded= Area *(PASTE_LITRES_PER_SQUARE_METRE)
    ##cant buy a fraction of a whole bucket and when you need ANY amount more than 
    #a whole number you have to buy the next integer amount up
    Buckets= math.ceil(Lneeded / (PASTE_LITRES_PER_BUCKET))
    CostPaste= Buckets*(paste_price)
    #cant buy fractions of rolls
    Rolls=math.ceil(Area / (WALLPAPER_SQUARE_METRES_PER_ROLL))
    CostWP= Rolls*wallpaper_price
    
    CostTotal= CostWP+CostPaste
    return CostTotal


## Here are some tests. Add your own tests as well; don't just count on ours!
assert wallpaper_price(1, 1, 1, 1)== 2, "very small wall very low cost"
assert wallpaper_price(10, 50, 450, 3500)== 358550
assert wallpaper_price(0, 0, 450, 3500) == 0, "No price for no wall!"
assert wallpaper_price(1, 1, 450, 3500) == (450+3500), "Small wall requires only one of each."


# In[ ]:




