#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Write the final_grades function here
import csv


def final_grades(grades_filename:str)->dict[str, tuple[float, str]]:
    """
    takes a csv file of students id number and grades in different components in the class 
    under the name grades_filename
    
    grades students and requires each component to be passed individually in order to pass the class
    returns students final grade and which component they failed, if any 
    """
    
    
    #end= {}
    #components= {}

    end: dict[str, tuple[float, str]] = {}
    components: dict[str, list[str]] = {}
    
    firstrow=True
    finalgrades= final_grades
    with open(grades_filename, newline='') as f:
        rdr= csv.DictReader(f)

        for row in rdr:
            if firstrow:
                for each in row:
                    if each != "Student ID":
                        c= each[0]
                        if c not in components:
                            components[c]= []
                        components[c].append(each)
                firstrow= False
                
            studentid=row["Student ID"]
            
            cgrades= {}
            for c in components:
                total= 0.0
                count= 0
                for unit in components[c]:
                    total+= float(row[unit])
                    count+= 1
                cgrades[c]= total / count
                
            grademin = None
            compmin=""

            for comp in cgrades:
                grade= cgrades[comp]
                if grade <50:
                    if grademin is None or grade <grademin:
                        grademin= grade
                        compmin= comp
                        
            if grademin is not None:
                final_grade= grademin
                end[studentid]= (final_grade, compmin)
            else:
                total= 0.0
                count=0
                for grade in cgrades.values():
                    total += grade
                    count += 1
                final_grade=total/count
                end[studentid]=(float(final_grade),"")

    return end
#print(final_grades("student_units_course1.csv"))
## Here are some tests. Add your own tests as well; don't just count on ours!
assert abs(final_grades("student_units_course1.csv")["260765"][0] - 91.384) < 0.001, "Passing grade"
assert final_grades("student_units_course1.csv")["260765"][1] == "", "Passing grade has no component"
assert abs(final_grades("student_units_course2.csv")["782154"][0] - 46.3) < 0.001, "Failing grade"
assert final_grades("student_units_course2.csv")["782154"][1] == "R", "Failing grade has failed component"

assert abs(final_grades("student_units_course1.csv")["835176"][0] - 82.754) < 0.001
assert final_grades("student_units_course1.csv")["835176"][1] == ""


# In[ ]:




