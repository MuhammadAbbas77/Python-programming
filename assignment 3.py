#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Program make a simple calculator
# This function adds two numbers 
def add(x, y):
   return x + y
# This function subtracts two numbers 
def subtract(x, y):
   return x - y
# This function multiplies two numbers
def multiply(x, y):
   return x * y
# This function divides two numbers
def divide(x, y):
   return x / y
# this func power numbers
def power(x, y):
    return x ** y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
# Take input from the user 
choice = input("Enter choice(1/2/3/4/5): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
elif choice == '5':
   print(num1,"**",num2,"=", power(num1,num2))
else:
   print("Invalid input")


# 

# In[2]:


# numeric values in list using for loop
list1 = [11,20,23,9,5,8] 
print("Numeric values in list")
for num in list1: 

    if num >= 0: 
       print("",num) 
    


# In[3]:


# to add a key to a dictionary
d= {0:10, 2:20}  
print(d)  
d.update({3:30})  
print(d)  


# In[4]:


# to sum all the numeric items in a dictionary
my_dict = {'data1':100,'data2':100,'data3':250}
print(sum(my_dict.values()))


# In[27]:



# duplicates values from a list  
# of integers 
def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated 
  
# Driver Code 
list1 = [10, 20, 30, 20, 20, 30, 40,  
         50, -20, 60, 60, -20, -20] 
print (Repeat(list1)) 


# In[32]:


# if a given key already exists in a dictionary
d = {1: 9, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_exist(x):
  if x in d:
      print('Key is exist in the dictionary')
  else:
      print('Key is not exist in the dictionary')
is_key_exist(5)
is_key_exist(10)


# In[ ]:




