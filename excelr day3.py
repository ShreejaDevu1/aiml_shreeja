#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Write a Python program that takes a student's marks in three subjects as input.
#If the average is greater than or equal to 90, print "Grade: A".
#if the average is between 80 and 89, print "Grade: B".
#f the average is between 70 and 79, print "Grade: C".
#Otherwise, print "Grade: Fail".
mathematics = float(input("Enter marks for mathematics: "))
english = float(input("Enter marks for english: "))
science = float(input("Enter marks for science: "))

average = (mathematics + english + science) / 3
if average >= 90:
    print("Grade: A")
elif 80 <= average < 90:
    print("Grade: B")
elif 70 <= average < 80:
    print("Grade: C")
else:
    print("Grade: Fail")


# In[ ]:




