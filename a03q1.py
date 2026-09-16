#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Write the interleave function here


def interleave(x: list)-> list:
    """
    takes a list x filled with any type values, and interleaves these values
    """
    
    ##len(x)+1 so that first half gets the bigger part when x is odd
    middle= (len(x)+1)//2
    half1=x[:middle]
    half2=x[middle:]

    
    #clear original list
    while len(x)>0:
        x.pop()

    
    # adds the first value from the first half of list then adds the first value from the second half   
    for i in range(middle):
        x.append(half1[i])
        if i<len(half2):
            x.append(half2[i])
            
            
    return x

#def reverseInterleave(deck: list) -> list:   
#    return deck[::2] + deck[1::2]
#print(reverseInterleave([1, 2, 3, 4, 5, 6]))

## Here are some tests. Add your own tests as well; don't just count on ours!
assert interleave([1, 2, 3, 4, 5, 6]) == [1, 4, 2, 5, 3, 6], "int list of even length"
assert interleave([
    "brave", "world", "has", "people", "it", "new", "that", "such", "in"
]) == [
    "brave", "new", "world", "that", "has", "such", "people", "in", "it"
], "str list of odd length"
assert interleave([2,2,9,8,0]) == [2,8,2,0,9]
assert interleave([1,"two",3,4,"five","six"]) == [1,4,"two","five",3,"six"]

