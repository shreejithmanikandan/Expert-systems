#!/usr/bin/env python
# coding: utf-8

# # EXPERT SYSTEMS

# In[2]:


print("Welcome to the Polio vaccination form")
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if age >= 1:
    print("For the following questions, please enter either 'yes' or 'no'")
    vac = input("Have you received your polio vaccine dose(s)? ")
    trip = input("Have you traveled to a polio-endemic country? ")
else:
    print("You are not old enough to get the vaccine.")

if vac == 'yes' and trip == 'no':
    print("You are already vaccinated against polio.")
elif vac == 'no' and trip == 'no':
    print("You can get your polio vaccine dose(s).")
elif trip == 'yes':
    print("As you have traveled to a polio-endemic country, you may need additional doses of the polio vaccine. Please consult your doctor for more information.")
else:
    print("Invalid input. Please enter either 'yes' or 'no'.")


# In[ ]:





# In[ ]:





# In[ ]:




