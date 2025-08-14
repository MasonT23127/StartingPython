def intro(name):
    print(f'''
          Hello {name} Welcome to the the project.''')

def name_info():
    name = input('Enter your first name: ')
    return name 



#--------main routine--------
name = name_info()
intro(name)