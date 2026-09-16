#!/usr/bin/env python
# coding: utf-8

# In[2]:


## This function is provided for your testing convenience. You may use it if you wish.
import csv

def csv_to_list(csv_file: str) -> list[dict[str, str]]:
    """
    takes a csv_file and converts to a list
    """
    with open(csv_file) as fh:
        rdr = csv.DictReader(fh)
        return list(rdr)

assert len(csv_to_list("nino34.csv")) == 909, "Entire file converted into list"
assert csv_to_list("nino34.csv")[0]["YR"] == "1950", "First year is as in the original file"

#print(csv_to_list("nino34.csv"))

## Write the csv_running_average function here

def csv_running_average(outputfile:str, inputfile:str, field:str)->list:
    """
    takes inputfile which is a csv file with at least one collumn of number values under a 
    feildname of user picked "field", creates an outputfile with user defined name and copies the original 
    csv inputfile but with a new collumn named "Running average of field" comuputes this running average and
    puts it into the output file and also returns a list of those values
    """
    with open(inputfile) as inp:
        rdr = csv.DictReader(inp)
        fieldnames= list(rdr.fieldnames or [])
        runningaveragef= f"Running average of {field}"
        fieldnames.append(runningaveragef)
    
        rows=[]
        vals=[]
        for row in rdr:
            rows.append(row)
            vals.append(float(row[field]))
    #modified original running average
    summ= 0.0
    for i in range(len(vals)):
        summ= summ+vals[i]
        vals[i] = summ/(i+1)

    #create new file and writes in old data and the new collumn
    with open(outputfile,"w") as o:
        end= csv.DictWriter(o, fieldnames)
        end.writeheader()
       
        i=0
        while i <len(rows):
            row=rows[i]
            row[runningaveragef] =vals[i]
            end.writerow(row)
            i=i+1
        return vals

print(csv_running_average("nino34-yra.csv","nino34.csv","YR"))
## Here are some tests. Add your own tests as well; don't just count on ours!
assert(abs(csv_running_average("nino34-mon.csv", "nino34.csv", "MON")[-1] - 6.485) < 0.001)
assert(abs(csv_running_average("nino34-ANOM.csv", "nino34.csv", "ANOM")[-1] - 0.011) < 0.001)



assert abs(csv_running_average("nino34-yra.csv", "nino34.csv", "YR")[-1] - 1987.376) < 0.001, "Average year (pointlessly) is 1987.376"
assert abs(csv_running_average("nino34-tra.csv", "nino34.csv", "TOTAL")[-1] - 26.906) < 0.001, "Average temperature is 26.906"
assert abs(float(csv_to_list("nino34-yra.csv")[-1]["Running average of YR"]) - 1987.376) < 0.001, "Average year in written file is 198.376"
assert abs(float(csv_to_list("nino34-tra.csv")[-1]["Running average of TOTAL"]) - 26.906) < 0.001, "Average temperature in written file is 26.906"


# In[ ]:




