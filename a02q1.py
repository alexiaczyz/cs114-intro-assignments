#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
## Write the complete_triangle function here
def complete_triangle(a:float,b: float, h: float, A:float, B:float)-> float:
    """
    Takes info about a right angle triangle in the form of 
    a= 1st non hyponeuse side lenght, b= 2nd non hyponeuse side lenght, h= hypotenuse length
    A= angle opposide to side a (in radians) , B= angle opposide to side b (in radians)
    
    enter in the elements of a right triangle and enter your unknown as 0, 
    this returns the missing value
    """
    #H=(math.pi/2)
    if a==0:
        a= h*math.sin(A)
        return a
    elif b==0:
        b= h*math.cos(A)
        return b
    elif h==0:
        h=math.sqrt((a**2)+(b**2))
        return h
    elif A==0:
        A=math.asin(a/(h))
        return A
    else:
        B=math.acos(a/(h))
        return B

print(complete_triangle(3, 0, 5, 0.64350110, 0.92729521))

## Here are some tests. Add your own tests as well; don't just count on ours!
assert abs(complete_triangle(3, 0, 5, 0.64350110, 0.92729521) - 4) < 0.001, "3-4-5 triangle"
assert abs(complete_triangle(1, 1, math.sqrt(2), 0.78539816, 0) - 0.78539816) < 0.001, "Equilateral triangle"

assert abs(complete_triangle(0, 9, 9.219, 0.21867, 1.35213) - 2) < 0.001, "my triangle"
assert abs(complete_triangle(3, 5, 0, 0.54042, 1.03038) - 5.83095) < 0.001, "my second triangle"


# In[ ]:




