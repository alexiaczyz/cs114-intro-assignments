#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Write the digit_count function here
def digit_count(n:int)->int:
    """
    takes integer n and tells you how many digits are in n
    """
    
    #counter only runs after 0 so that loop knows when to stop, but 0 is one digit
    if n==0:
        return 1
    
    #n and -n have the same amount of digits
    n=abs(n)
    
    #start counting at 0
    c=0
    while n>0:
        #n is in base 10 so as you divide by 10, it brings n to the next digit
        #by taking the int of this, it ignores the decimal remainder (the digit already counted)
        n=int(n/10)
        c+=1
    return c


## Here are some tests. Add your own tests as well; don't just count on ours!
assert digit_count(0) == 1, "0 is one digit"
assert digit_count(-2900) == 4, "4-digit number"
assert digit_count(22980) == 5
assert digit_count(123456789) == 9


# In[ ]:




