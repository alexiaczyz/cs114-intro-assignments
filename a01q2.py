#!/usr/bin/env python
# coding: utf-8

# In[6]:


from math import sqrt


## Here are the hypotenuse and distance functions we wrote in class:
def manhattan_distance(x1:float,y1:float,x2:float,y2:float)->float:
    """
    returns the manhattan distance between points (x1,y1) and (x2,y2)
    """
    xtotal= abs(x1 - x2)
    ytotal= abs(y1 -y2)
    DistanceTotal= abs(xtotal) + abs(ytotal)
    return DistanceTotal

def hypotenuse(a: float, b: float) -> float:
    """
    Return the hypotenuse of a right triangle with side lengths a and b.
    """
    return sqrt(a**2 + b**2)

assert abs(hypotenuse(3, 4) - 5) < 0.001, "3-4-5 triangle"
assert abs(hypotenuse(-1, 1) - sqrt(2)) < 0.001, "Negative side lengths OK"

def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Return the distance between the two points (x1, y1) and (x2, y2).
    """
    xd = x2 - x1
    yd = y2 - y1
    return hypotenuse(xd, yd)

assert abs(distance(0, 0, 1, 1) - sqrt(2)) < 0.001, "Root-two distance"
assert abs(distance(1, 2.6, -2, 6.6) - 5) < 0.001, "3-4-5 distance"


## Write the manhattan_error function here

def manhattan_error(x1:float, y1:float, x2:float, y2:float)->float:
    """
    Calculates the error between manhattan distance and the straight
    line distance between two points (x1,y1) and (x2,y2)
    """
    end=( abs((manhattan_distance(x1, y1, x2, y2)) - (distance(x1, y1, x2, y2)))/(distance(x1, y1, x2, y2)))
    return end

## Here are some tests. Add your own tests as well; don't just count on ours!
assert abs(manhattan_error(1, 2, 3, 10) - 0.212) < 0.001
assert abs(manhattan_error(2,9,8,0) - 0.387) < 0.001

assert abs(manhattan_distance(1, 2, 3, 4) - 4) < 0.001, "test 1"
assert abs(manhattan_distance(5, -6, 7, -8) - 4) < 0.001, "test 2"

assert abs(manhattan_error(0, 0, 0, 13579.246) - 0) < 0.001, "With motion in only one axis, they're the same"
assert abs(manhattan_error(0, 0, 1, 1) - ((2-sqrt(2))/sqrt(2))) < 0.001, "Error ratio for a 1/1 angle is root 2"


# In[ ]:




