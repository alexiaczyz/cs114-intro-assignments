#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
## Write the is_prime function here
def is_prime(n:int)->bool:
    """
    takes integer n and checks: is it true that n is a prime number?
    """
    #negtive numbers dont have factors
    assert n>= 0 
    
    #any number between 0 and 1 isnt prime
    if n<=1:
        return False
    
    #prime numbers can be found by divding it by number x
    #x ranges from 2 to the sqrt of that number n
    #if any of these division result in no remainder, n is not prime 
    x=2   
    #iterates through 2 -> √n
    for x in range(2, int(math.sqrt(n))+1):
        #when it is true that there is no remainder, its false that n is prime
        return not(n%x==0)
    
    return True
    

## Here are some tests. Add your own tests as well; don't just count on ours!
assert not is_prime(1), "1 is not prime"
assert is_prime(2), "2 is prime"
assert is_prime(3), "is prime"
assert not is_prime(4), "is not prime"
assert is_prime(5), "is prime"


# In[ ]:




