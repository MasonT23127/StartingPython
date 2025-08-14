'''

author: Mason Twemlow
date: 17/07/2025
description: This is script is about conditions
version: 1.0

'''

#------ Libararies ------
import random # from random import randint *

#------- Functions ------


#------Main Routine -----
name = input('Enter your first name: ') #store value Bob 
age = int(input('Enter your age: ')) #input value age

print('Hello, ' + name ) #print hello then name

if(age <18 and age > 11):
    print('Your at high school')
elif(age > 0 and age < 12):
    print('Your at primary school')
else:
    print('Your old')