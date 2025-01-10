#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1)Write a Python program that performs the following tasks:
#1. Ask the user to enter a positive integer `n`.
#2. Use a `for` loop to print all numbers from `1` to `n` on separate lines.
#3. Use a `while` loop to calculate the sum of all numbers from `1` to `n` and print the result.
n = int(input("Enter a positive integer: "))
print("Numbers from 1 to", n, "using a for loop:")
for i in range(1, n + 1):
    print(i)
sum_of_numbers = 0
i = 1
while i <= n:
    sum_of_numbers += i
    i += 1
print(f"The sum of numbers from 1 to {n} is: {sum_of_numbers}")


# In[3]:


#2)Write a Python program that includes a user-defined function to perform the following tasks:
#1. Define a function named calculate_square that takes a single argument `n` and returns the square of `n`.
#2. In the main program, ask the user to input a positive integer.
#3. Call the calculate_square function with the user-provided number and display the result.
def calculate_square(n):
    return n ** 2
try:
    n = int(input("Enter a positive integer: "))
    if n < 0:
        print("Please enter a positive integer.")
    else:
        result = calculate_square(n)
        print(f"The square of {n} is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")



# In[ ]:




