''' 
    author: Mason Twemlow
    date: 14/08/25
    description: Five question quiz.
'''

# make a quiz with 5 questions
# store each question in a list
# store answers the questions in same list or another one

# ask the user each questions nad keep a total of correct answers.
# must use a function and one list obviously

#-------- functions --------
'''
def main():
    score = 0
    question1 = 'What is 5+5?'
    answer1 = '10'
    question2 = 'What is 2x10?'
    answer2 = '20'

    while True:
        name = input('Enter your name: ')
        if len(name) >= 2 and len(name) <= 25 and name != '' and name.isalpha():
            break
        else:
            print('Your name was invalid, 2-25 characters and no special characters')
    print('Hello ' + name + ' welcome to the math quiz, and will get harder and harder. The first question is... ')
    print(question1)
    useranswer1 = input('Your answer: ') 
    if useranswer1 == answer1:
        print('Correct!')
        score += 1
    else:
        print('Incorrect, the answer was ' + answer1)
    print('Your score is now ' + str(score))    

    print(question2)
    useranswer2 = input('Your answer: ') 
    if useranswer2 == answer2:
        print('Correct!')
        score += 1
    else:
        print('Incorrect, the answer was ' + answer2)
    print('Your score is now ' + str(score))
    

#---------main routine----------------
if __name__ == "__main__":
    main()



'''
#---- function----
def ask_user_questions(question, answer):
    guess = input(question)
    if(guess == answer):
        print('You got it right')
        return True
    else: 
        print('You got it wrong')
        return False 

def amain():
    questions = ['What is your name? ',
                 'What is your job? ', 
                 'What is your schools name? ']
    answers = ['Mason', 'Student', 'Otago Boys Highschool']
    correct_answers = 0 
    wrong_answers = 0
    for i in range(len(questions)):
        if ask_user_questions(questions[i], answers[i]):
            correct_answers += 1
        else: 
            wrong_answers += 1
        print(f'You got {correct_answers} correct and {wrong_answers} wrong.')
        

if __name__ == "__main__":
    amain()
    