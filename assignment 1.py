#!/usr/bin/env python
# coding: utf-8

# # 1.) Write a Python program to find average of three numbers entered by the user.

# In[1]:


x=int(input("Enter 1st number"))
y=int(input("Enter 2nd number"))
z=int(input("Enter 3rd number"))
sum=x+y+z
average=sum/3  #since there are three numbers
print("Average: ",average)


# # 2.) Write a python program to compute a person's income tax.

# In[5]:


Gross_Income=float(input("enter gross amount in dollar($): "))
no_of_dependents=int(input("enter the number of dependents: " ))
dependent_deduction=3000
tax_rate=0.2
standard_deduction=10000
taxable_income=Gross_Income-standard_deduction-(dependent_deduction*no_of_dependents)
tax=taxable_income*tax_rate
print(tax)


# # 3.) Write a python program to store different data type values into a list. (For an
# example: Student [SID, Name, Gender, Course Name, CGPA]).

# In[6]:

sid=int(input(""))
name=input("")
Gender=input("")
Course_Name=input(" ")
CGPA=float(input(""))
list=[]
list.append(sid)
list.append(name)
list.append(Gender)
list.append(Course_Name)
list.append(CGPA)
list


# # 4.) Write a python program to enter marks of 5 students into a list and display
# them in sorted manner.

# In[8]:


stud1=75
stud2=65
stud3=55
stud4=44
stud5=88
marks=[]
marks.append(stud1)
marks.append(stud2)
marks.append(stud3)
marks.append(stud4)
marks.append(stud5)
s=sorted(marks)
print(s)

# # 5. List: color ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# a. Write a Python program to print a specified list after removing 4th element.
# Expected output: color [Red', 'Green', 'White', 'Pink', 'Yellow']

# In[5]:


color=['Red','Green','White','Black','Pink','Yellow']  #index starts from 0(red on 0th index)
                                                        #similarly black on 3rd index
C=color.pop(3)  # pop function used to delete particular element
print(color)


# # b. Remove ‘Black’ and ‘Pink’ from the list and replace them with ‘Purple’.

# In[ ]:


color=['Red','Green','White','Black','Pink','Yellow']
color[3:5]=['purple'] # since list is mutable 
print(color)


# In[ ]:




