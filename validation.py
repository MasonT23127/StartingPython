# --------achieved level input-------------------------------
print('Achieved Level Input')

name = input('Enter your name: ') #str
age = int(input('Enter your age: ')) #int
height= float(input('Enter your height: ')) #float



#---------merit level input - boundaries (limit)------------

print('Merit Level Input - Boundaries (Limit)')
name = input('Enter your name: ')
if (len(name) >= 2 and len(name) <= 30):
    if(name in ['a', 'b', 'c']): # or namem.isalpha())
        print('Valid name')

age =int(input('Enter your age: ')) 
if(age >= 1 and age <= 130):
    print('Valid age')

#---------------Excellence level input - valids--------------

print('Excellence Level Input - Valids')

while (True):
    try:
        age = int(input('Enter your age: '))
        if(age >= 1 and age <= 130): # if(age.isdigit() ):#isnumeric()):
            break
    except: 
        print('Invalid input. Please enter a valid age between 1 and 130.')
        continue 
