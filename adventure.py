'''
    author: Mason Twemlow
    date: 15/08/2025
    version: 1
    description: This is going to be battle code
'''

#-------------libraries------------------

import random # Get a random integer, shuffle, ...


#-------------functions-------------------
hp = 100 # our hitpoints
dff = 13 # our defense 

en_hp = 100 # enemies hitpoints
en_dff = 13 # enemies defense

#------------main routine-----------------
while(hp > 0 and en_hp > 0): # checking if both are alive 
    
    # This loops checks for user input validation. They can only select s, a, or h.
    while(True): 
        try: 
            attack = input('''
                Enter your attack: 
                [s]word 
                [a]xe 
                [h]eal
            ''') # Asking the user for attack
            if(attack[0].lower() == 's' or attack[0].lower() == 'a' or attack[0].lower() == 'h'): # Validate the input. 
                break 
            else: 
                print('Invalid, enter "s", "a" or "h" ')
        except: 
            print('Invalid, try again.')
        

    # Normalize input to lowercase and use only the first character
    action = attack[0].lower()

    # Checking the user input 
    if(action == 's'): # When the user enters s for sword attack
        rand = random.randint(1,20)
        if(rand > en_dff):
            damage = random.randint(1,20)
            print(f'You attack with sword doing {damage} damage')
            en_hp -= damage 
       
    elif(action == 'a'): 
        pass 
    elif(action == 'h'):
        pass 