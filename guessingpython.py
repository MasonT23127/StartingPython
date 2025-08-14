import random 

def guessing():
    #get users name

    
    while(True):
        try:
            name = input('Enter your name: ')
            if(len(name)>= 2 and len <= 25 and name!= '' and name.alpha()):
                break 
        except:
            print('Your name was invalid, 2-25 characters, no special characters') 
    
    #make a random number
    rand = random.randint(1,10)
    #make a variable to store.number of guesses
    guesses = 0
    #create a loop until it is guessed
    while(True):
        
        while(True):
            try: 
                guess= int(input('Enter your guess: '))
                if(guess >= 1 and guess <= 10 and guess != None):
                    break
            except:
                print('Your input was incorrect.')
        
        if(guess ==rand):
            print(f'You guessed correctly in {guesses} guesses.')
            break
        else: print("Incorrect, try again.")
        guess =+ 1 



#------------- main program ---------------
guessing()