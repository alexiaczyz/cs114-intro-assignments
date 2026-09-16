#!/usr/bin/env python
# coding: utf-8

# In[10]:


## Write the justify function here
def justify(output_filename:str, input_filename:str)-> list[str]:
    """
    takes a text file under input_filename and gives an output_filename where the text is justified
    (spaced to fill the line)
    """

    with open(input_filename, "r") as f:
        lines= [line.strip() for line in f]
    linelen = max(len(line) for line in lines)

    justifiedlines=[]

    for line in lines:
        parts= line.split()
        partsamount= len(parts)
        if partsamount<= 1:
            paddedline = line + (" " * (linelen - len(line)))
            justifiedlines.append(paddedline)

        else:
            gaps =partsamount -1
            chartotal= sum(len(word) for word in parts)

            spacestotal= linelen -chartotal
            spaces_each=spacestotal //gaps
            remainder=spacestotal %gaps
            assembled = ""
            for i in range(partsamount):
                assembled+= parts[i]

                if i <gaps:
                    gapspaces = spaces_each
                    if i < remainder:
                        gapspaces+= 1

                    assembled +=" " * gapspaces

            justifiedlines.append(assembled)
    with open(output_filename, "w") as f:
        for line in justifiedlines:
            f.write(line +"\n")

    return justifiedlines


## Here are some tests. Add your own tests as well; don't just count on ours!
assert justify("tmp.txt", "a-tale-of-two-cities.txt")[106:115:3] == [
    "It  was  the  best  of  times,  it  was  the worst of times, it was the age of",
    "season  of  Darkness,  it  was  the  spring  of  hope,  it  was  the winter of",
    "short,  the  period  was  so  far  like  the  present period, that some of its"
], "First lines of A Tale of Two Cities"
assert justify("tmp.txt", "frankenstein.txt")[1558:1561] == [
    "shutters,      I     beheld     the     wretch—the     miserable     monster     whom     I     had",
    "created.    He   held   up   the   curtain   of   the   bed;   and   his   eyes,   if   eyes   they",
    "may    be    called,    were   fixed   on   me.   His   jaws   opened,   and   he   muttered   some"
], "Crucial moment of Frankenstein"

assert justify("tmp.txt", "frankenstein.txt")[2298:2299] == ['“I    do    not    know    what    you    mean,”    replied    my    brother,    in    accents   of']
assert justify("tmp.txt", "frankenstein.txt")[200:201] ==['already    engaged    appear   to   be   men   on   whom   I   can   depend   and   are   certainly']


# In[ ]:




