#!/usr/bin/env python
# coding: utf-8

# In[4]:


## Write the grade_curve function here
import csv
def grade_curve(filename:str)->dict:
    """
    takes a csv file of students names and their grade under filename 
    and returns a dict of them graded on a curve with a standard bell curve
    """
    #create empty lists to sort the name from the grade from the csv
    name=[]
    grade=[]
    #open csv and sort
    with open(filename) as f:
        rdr=csv.DictReader(f)
        for row in rdr:
            name.append(row["Name"])
            grade.append(float(row["Score"]))
#empty list for the data after its been sorted by grade 
    end=[]
    x=len(grade)

    for i in range(x):
        end.append([grade[i], name[i]])

    def score(gradee):
        return gradee[0]

    end.sort(key=score , reverse=True)

    EndGrades=[]
    EndNames=[]

    for item in end:
        EndGrades.append(item[0])
        EndNames.append(item[1])

 #creating sizes for the grade groups
    Aamount=round(0.1*x)
    Bamount=round(0.2*x)
    Camount=round(0.4*x)
    Damount=round(0.2*x)
    Famount=x-(Aamount+Bamount+Camount+Damount)

    enddict={}
    I=0

    for i in range(I, I+Aamount):
        enddict[EndNames[i]] = "A"
    I=I+Aamount

    for i in range(I, I+Bamount):
        enddict[EndNames[i]] = "B"
    I=I+Bamount

    for i in range(I, I+Camount):
        enddict[EndNames[i]] = "C"
    I=I+Camount

    for i in range(I, I+Damount):
        enddict[EndNames[i]] = "D"
    I=I+Damount

    for i in range(I, I+Famount):
        enddict[EndNames[i]] = "F"
    I=I+Famount

    return enddict

## Here are some tests. Add your own tests as well; don't just count on ours!
assert grade_curve("student_scores.csv")["Ivy Earl"] == "B", "96.6 gets a B"
assert grade_curve("student_scores.csv")["Liam Moore"] == "F", "70.7 gets an F"

assert grade_curve("student_scores.csv")["Aaliyah Chen"] == "B"
assert grade_curve("student_scores.csv")["Paul Rodriguez"] == "F"


# In[ ]:




