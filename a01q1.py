#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Write the manhattan_distance function here

def manhattan_distance(x1:float,y1:float,x2:float,y2:float)->float:
    """
    returns the manhattan distance between points (x1,y1) and (x2,y2)
    """
    xtotal= abs(x1 - x2)
    ytotal= abs(y1 -y2)
    DistanceTotal= abs(xtotal) + abs(ytotal)
    return DistanceTotal

## Here are some tests. Add your own tests as well; don't just count on ours!
assert abs(manhattan_distance(1, 2, 3, 4) - 4) < 0.001, "test 1"
assert abs(manhattan_distance(5, -6, 7, -8) - 4) < 0.001, "test 2"
assert abs(manhattan_distance(0, -3.14, 3.14, 0) - 6.28) < 0.001, "Computing tau using manhattan_distance"
assert abs(manhattan_distance(-12345.67, -1234.567, -1234.567, -12345.67) - 22222.206) < 0.001, "Positive delta x, negative delta y"


# In[ ]:




