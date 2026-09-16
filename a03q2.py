#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Write the list_stats function here

def list_stats(x:list)->dict:
    """
    takes a list of numbers as x and tells you the mean, median, mode, max, and min of your list 
    """
    #list cant be empty
    assert len(x)>0
    sum = 0.0
    
    #loops over x and sums all values
    for val in x:
        sum = sum + val      
    mean = sum/len(x)
    
    #gets a copy of x and sorts it from least to greatest
    xcopy=sorted(x)
    #splits list in half
    middle= (len(xcopy)+1)//2
    half1=xcopy[:middle]
    half2=xcopy[middle:]
    
    #if x is odd it takes the middle value is median
    #is x is even it averages the two middle values
    if len(xcopy)%2==0:
        median= (half1[-1]+half2[0])/2
    else:
        median= half1[-1]
        
    #loops over x and counts if there are repeated values
    countmax=0.0
    for number in x:
        count=0.0
        #loops over all numbers then compares those numbers back to the list to see if any repeated
        for othernumber in x:
            if number==othernumber:
                count=count+1
        #when the count goes up the mode updates
        if count >countmax:
            countmax=count
            mode=number
    #gets first and last values in the sorted copy to get min and max        
    xcopy=sorted(x)
    min=xcopy[0]
    max=xcopy[-1]
    
    end={}
    end["mean"]=mean
    end["median"]=median
    end["mode"]=mode
    end["max"]=max
    end["min"]=min
    #print(x)
    return end


## Here are some tests. Add your own tests as well; don't just count on ours!
test_list = [3.0, 1.0, 4.0, 1.0, 5.0, 9.0] # In order, [1, 1, 3, 4, 5, 9]

print(list_stats(test_list))
assert abs(list_stats(test_list)["mean"] - 3.83333333) < 0.001, "Mean of test list"
assert abs(list_stats(test_list)["median"] - 3.5) < 0.001, "Median of an even-length list"
assert abs(list_stats(test_list)["mode"] - 1.0) < 0.001
assert abs(list_stats(test_list)["max"] - 9.0) < 0.001

