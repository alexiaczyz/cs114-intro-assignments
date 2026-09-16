#!/usr/bin/env python
# coding: utf-8

# In[2]:


## Write the valid_word_ladder function here
GOOD_WORD_LADDER = ["folks", "folds", "foods", "fools"]
BAD_WORD_LADDER = ["ronin", "rosin", "rosit", "roset", "roses"]
mywordladder= ["cat","sat","sit"]
myotherwordladder= ["complete", "compete", "wrong"]
Myotherwordladder= ["complete", "competed", "wrong"]

def valid_word_ladder(lexicon_file:str, word_ladder:list)->(tuple[bool,tuple[str,str]]):
    """
    give a list of words that make a word ladder as "word_ladder", returns if your word ladder is valid by saying True or False,
    and telling you the two first entries where you list is invalid
    input acceptable words in text file lexicon_file
    """
    #converts lexicon file to a list 
    lexicon=[]
    with open(lexicon_file) as lex:
        for line in lex:
            lexicon.append(line.strip())
            #print(lex)
      #iterates over the word ladder list in pairs of the current word and the one after it 
        for i in range(len(word_ladder)-1):
            x=word_ladder[i]
            y=word_ladder[i+1]
           # print(x,y)
        
        #checks if length is not equal and if each word is in the lexicon
            if len(x)!= len(y):
                return (False,(x,y))
            
            if y not in lexicon:
                return (False,(x,y))
            
            #loops over with a count of how many letters are changed between current and next
            else: 
                count=0
                for ii in range(len(x)):
                    if x[ii] != y[ii]:
                        count=count+1
                if count > 1:
                    return (False, (x,y))
        return (True,(word_ladder[0],word_ladder[-1]))
            

## Here are some tests. Add your own tests as well; don't just count on ours!
GOOD_WORD_LADDER = ["folks", "folds", "foods", "fools"]
assert valid_word_ladder("moby-words.txt", GOOD_WORD_LADDER)[0], "folks to fools valid word ladder"
BAD_WORD_LADDER = ["ronin", "rosin", "rosit", "roset", "roses"]
assert not valid_word_ladder("moby-words.txt", BAD_WORD_LADDER)[0], "ronin to roses invalid word ladder"
assert valid_word_ladder("moby-words.txt", BAD_WORD_LADDER)[1] == ("rosin", "rosit"), "rosit is not a word"

assert valid_word_ladder("moby-words.txt", mywordladder)[0]
assert valid_word_ladder("moby-words.txt", mywordladder)[1]== ("cat","sit")

assert not valid_word_ladder("moby-words.txt", myotherwordladder)[0]
assert valid_word_ladder("moby-words.txt", myotherwordladder)[1]== ("complete","compete") , "wrong size"

assert not valid_word_ladder("moby-words.txt", Myotherwordladder)[0]
assert valid_word_ladder("moby-words.txt", Myotherwordladder)[1]== ("complete","competed") , "incorrect letter swapping"


# In[ ]:




