'''
    author: Mason Twemlow
    date: 15/08/2025
    version: 1
    description: This is going to be battle code
'''

#-------------libraries------------------

import random 


#-------------functions-------------------
hp = 100 # our hitpoints
dff = 13 # our defense 

en_hp = 100 # enemies hitpoints
en_dff = 13 # enemies defense

#------------main routine-----------------
while(hp > 0 and en_hp > 0): # checking if both are alive 
    attack = input('''
        Enter your attack: 
        [s]word 
        [a]xe 
        [h]eal
    ''') # Asking the user for a letter
    if(attack =='s'):
        pass 
    elif(attack == 'a'):
        pass 
    elif(attack == 'h'):
        pass 