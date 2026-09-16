#!/usr/bin/env python
# coding: utf-8

# In[2]:


## These constants and this helper function are provided if you wish to use them
NORMAL_PUNCTUATION = ",:;.?!"
EM_DASH = "—"
EN_DASH = "–"
OPENING_MARKS = "(“"
CLOSING_MARKS = ")”"

def is_word(s: str) -> bool:
    """
    Returns True if s is a word, in the sense used by the spacer function,
    False otherwise. We consider a string to be a word if either it's longer
    than one character, or it is a single letter or digit.
    """
    return len(s) > 1 or len(s) == 1 and (
        (s[0] >= "A" and s[0] <= "Z") or
        (s[0] >= "a" and s[0] <= "z") or
        (s[0] >= "0" and s[0] <= "9")
    )

assert is_word("I"), "Single letter"
assert is_word("2"), "Single digit"
assert not is_word("."), "Punctuation"
assert is_word("etc."), "Multi-character word"


## Write the spacer function here

#normal punct has one space after IF followed by word
#em dashed have no spaces 
#en dashes one space on each side
#opening mark have a space before UNLESS there is another opening mark before
#closing mark have a space only is followed by word 
#things like i'm canr split up at the ' (' - .)
#
def spacer(token_list:list)->str:
    """
    takes a sentance in the form of each token seperated in a list, input through token_list
    and you will get the list back as a normal sentance structure
    """
    #empty string to add everything onto
    end=  ""
    
    #iterates over the list and examines a current token and the one right after
    for i in range(len(token_list)-1):
        currenttoken= token_list[i]
        nexttoken=token_list[i+1]
        
        ## em dash rule
        if currenttoken in EM_DASH:
            end= end+currenttoken
        
        #normal punctuation rule
        if currenttoken in NORMAL_PUNCTUATION: 
            if is_word(nexttoken)==True:
                end=end+currenttoken+" "
            else:
                end=end+currenttoken
        
        #regular word rule
        if is_word(currenttoken)==True:
            if nexttoken in NORMAL_PUNCTUATION:
                end=end+ currenttoken
            elif is_word(nexttoken)==True:
                end=end+currenttoken+" "
            else:
                end=end+currenttoken
        
        
        #en dash rule
        if currenttoken in EN_DASH:
            end=end+" "+currenttoken+" "
        
        #opening mark rules
        if currenttoken in OPENING_MARKS:
            if currenttoken and nexttoken in OPENING_MARKS:
                end=end+ currenttoken
            else:
                end= end+ " "+ currenttoken
                
        #closing dash rules            
        if currenttoken in CLOSING_MARKS:
            if is_word(nexttoken)==True:
                end= end+ currenttoken + " "
            else:
                end=end+currenttoken
                
    #adds last token back in       
    lasttoken= token_list[-1]  
    end=end+lasttoken
    return end 
        
## Here are some tests. Add your own tests as well; don't just count on ours!
assert spacer(["Sometimes", "I", "like", "to", "mix", "dashes", "—", "like", "this", "–", "just", "to", "annoy","everyone", "!", "!"])== "Sometimes I like to mix dashes—like this – just to annoy everyone!!"


assert spacer( ["When", "your", "technical", "writing", "instructor", "tells", "you", "“", "don’t", "use", "contractions", "”", ",", "check", "the", "actual", "style", "guides", "!", "Don’t", "believe", "the",
"anti-contraction", "propaganda", "!"])== "When your technical writing instructor tells you “don’t use contractions”, check the actual style guides! Don’t believe the anti-contraction propaganda!"

assert spacer(["I’m", "a", "light-hearted", "li’l", "elf", "!"])=="I’m a light-hearted li’l elf!"

assert spacer(["I'm","testing","some","stuff","!","?","–","ahhh"])== "I'm testing some stuff!? – ahhh"

assert spacer(["Alexia", "c","z","y","z",")",")"])=="Alexia c z y z))"
assert spacer(["I", "think", ",", "therefore", "I", "am", "."]) == "I think, therefore I am.", "I think, therefore I am."
assert spacer(["Overusing", "punctuation", ":", "a", "nuisance", ";", "but", "is", "it", "so", "bad", "?"]) == "Overusing punctuation: a nuisance; but is it so bad?", "Several normal punctuation marks."


# In[ ]:





# In[ ]:




