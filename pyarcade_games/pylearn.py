"""
Pylearn Game
"""
from video_to_ascii.cli import top
import time
import os
from termcolor import cprint 
from pyfiglet import figlet_format
import tty
import sys
import termios
from pyarcade_games.save_data import save_data, retrive_value

from colorama import Fore, Style

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def first_game_message():
    """
    its a function to display a welcoming to the game in asci art , and it works in the beginning of the game only

    arguments:
    input -> None
    Output -> asci_art_message
    """
    start_message = Fore.CYAN + Style.BRIGHT + figlet_format("Welcome to Pylearn Game!")
    
    return(start_message)


def second_game_message():
    """
    its a function to display the name of the game with a nice style at the top of The terminal to add more beauty , and it works inside the game it self not in the beginning

    arguments:
    input -> None
    Output -> asci_art_message
    """
    start_message = Fore.CYAN + Style.BRIGHT + figlet_format("Pylearn Game")
    return(start_message)



def welcoming_picture_to_game():
    """
    Function to display the image of the instructor in ASCI art
    arguments=>None
    Return=>string
    """
    # loading the picture of instructor in ASCI ART
    with open('pic.txt',mode='r') as file:
        content=file.read()
    return(content)


def welcoming_text_to_game():
    """
    Function to display the introduction about the instructor
    arguments=>None
    Return=>string
    """
    introduction="""                                                  Welcome to Pylearn !
                                I am Dario Thornhill and i will be your instructor in this Game !
                                i will help you to learn programming in a very Easy and nice way !
                                                lets get started"""
    return(introduction)





    
def sense_user_input():
    """
    A function to sense the variation in the command line so that if the user press any key the user will be redirected to the next question
    """

    print("Press On any key to be directed to the questions.")

    orig_settings = termios.tcgetattr(sys.stdin)

    tty.setcbreak(sys.stdin)
    x = 0

    x=sys.stdin.read(1)[0]


    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
    return ''


def compare_user_question_with_expected_words(user_question):
    counter=0
    key_words1=['I WANT TO ASK','I WOULD LIKE TO ASK','I WANT TO ASK YOU','CAN I ASK YOU','I WANT TO ASK ABOUT','CAN I ASK ABOUT','CAN I ASK']

    key_words_for_lesson0=['PROGRAMMING','PYTHON','LESSON1','LESSON 1']
    key_words_for_lesson1=['PRINT','LESSON2','LESSON 2']
    key_words_for_lesson2=['ESCAPE CHARACTERS','ESCAPE CHARACTER','LESSON3','LESSON 3']
    key_words_for_lesson3=['VARIABLE NAMES','VARIABLE','LESSON4','LESSON 4']
    key_words_for_lesson4=['INPUT','INPUT IN PYTHON','INPUT STATEMENT','LESSON5','LESSON 5']
    special_case_words=[]
    special_case_words.extend(key_words_for_lesson0)
    special_case_words.extend(key_words_for_lesson1)
    special_case_words.extend(key_words_for_lesson2)
    special_case_words.extend(key_words_for_lesson3)
    special_case_words.extend(key_words_for_lesson4)
    # compare between user question and expected words
    while counter < 20:
        
        for item in special_case_words:
            if item not in user_question.upper():
                # indicates how many items is not in user question from the original list
                counter+=1
        if counter == 20:
            print('')
            print('You must ask about one of the lessons and you did\'nt , ask about a specific lesson ..')
            print('')
            user_question=input('Question: ')
            user_question=user_question
            print('')
        if counter < 20:
            return user_question
        counter=0
        
    return True

def user_ask_instructor(indicator):
    """
    this function will give the user the ability to ask the instructor a questioos

    argumnets:
    input->nothing
    output-> more explanation about specific lesson
    """
    more_explanation_lesson={

    'LESSON0':""" lesson 1 - Programming - Extra information:
    Computer programming is the process of designing and building an executable computer program to accomplish a specific computing result or to perform a specific task. Programming involves tasks such as: analysis, generating algorithms, profiling algorithms' accuracy and resource consumption, and the implementation of algorithms in a chosen programming language (commonly referred to as coding).[1][2] The source code of a program is written in one or more languages that are intelligible to programmers, rather than machine code, which is directly executed by the central processing unit. The purpose of programming is to find a sequence of instructions that will automate the performance of a task (which can be as complex as an operating system) on a computer, often for solving a given problem. Proficient programming thus often requires expertise in several different subjects, including knowledge of the application domain, specialized algorithms, and formal logic.""" 

    ,'LESSON1':"""lesson 2 - print() - Extra information:
    The print() function prints the specified message to the screen, or other standard output device.

    The message can be a string, or any other object, the object will be converted into a string before written to the screen.""" 


    ,'LESSON2': """lesson 3 - Escape Characters -  Extra information:
    To insert characters that are illegal in a string, use an escape character.

    An escape character is a backslash \ followed by the character you want to insert.

    An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
    Example
    You will get an error if you use double quotes inside a string that is surrounded by double quotes:
    txt = "We are the so-called "Vikings" from the north." """,


    'LESSON3':"""lesson 4 - variables - Extra information:
    A Python variable is a reserved memory location to store values. In other words, a
    variable in a python program gives data to the computer for processing.
    Every value in Python has a datatype. Different data types in Python are Numbers,
    List, Tuple, Strings, Dictionary, etc. Variables can be declared by any name or even
    alphabets like a, aa, abc, etc
    Example
    any_thing= 'hello' """ ,


    'LESSON4':"""lesson 5 - input() - Extra information:
    The Python input() and raw_input() functions are used to collect user input. input() has replaced raw_input() in Python 3 and onward. Both functions return a user input as a string.
    For example, you may want to ask a user their age so you can determine whether they should be allowed to use your site. Or you may want to ask a user to input their name so you can determine its length. Whatever data you need from a user, you’ll need to find a way to get it in some fashion.

    That’s where the Python input() function comes in. Input(), a built-in function in Python, allows coders to receive information through the keyboard, which they can process in a Python program. In this tutorial, we are going to break down the basics of Python input()."""}

    key_words1=['I WANT TO ASK','I WOULD LIKE TO ASK','I WANT TO ASK YOU','CAN I ASK YOU','I WANT TO ASK ABOUT','CAN I ASK ABOUT','CAN I ASK']

    key_words_for_lesson0=['PROGRAMMING','PYTHON','LESSON1','LESSON 1']
    key_words_for_lesson1=['PRINT','LESSON2','LESSON 2']
    key_words_for_lesson2=['ESCAPE CHARACTERS','ESCAPE CHARACTER','LESSON3','LESSON 3']
    key_words_for_lesson3=['VARIABLE NAMES','VARIABLE','LESSON4','LESSON 4']
    key_words_for_lesson4=['INPUT','INPUT IN PYTHON','INPUT STATEMENT','LESSON5','LESSON 5']
    special_case_words=[]
    special_case_words.extend(key_words_for_lesson0)
    special_case_words.extend(key_words_for_lesson1)
    special_case_words.extend(key_words_for_lesson2)
    special_case_words.extend(key_words_for_lesson3)
    special_case_words.extend(key_words_for_lesson4)


    os.system('clear')
    print('         I think now its a good time to take questions from you ...       ')
    time.sleep(2)
    print(Fore.RESET +'')
    top('assets/participation.mp4','filled-ascii')
    os.system('clear')
    print("""       Do You Have any Questions   ?
            A -Yes
            B -No
            """)
    user_question=''
    user_confirmation=input('> Answer:')
    while user_confirmation.upper() != 'YES' and user_confirmation.upper() != 'NO':
        print('Its a Yes or No question , Just answer with one of Them !')
        user_confirmation=input('> Answer:')
    if user_confirmation.upper() == 'YES':
        print('     Go a head   ....  ')
        print('')
        user_question=input('> Question: ')
        user_question=user_question.upper()
        print('')
        for item in key_words1:
            user_question=user_question.upper()
            question_check=user_question.find(item)
            while question_check >= 0:
                #to add the item in the end of the list so that it will be checked again if the user repeated the same
                key_words1.extend(key_words1[key_words1.index(item):])
                print('')
                print(f' Please Just dont Waste my time saying \"{item}\" ! , go ahead and ask about specific lesson ..')
                print('')
                user_question=input('> Question: ')
                user_question=user_question.upper()
                question_check=user_question.find(item)

        user_final_answer=compare_user_question_with_expected_words(user_question)
        user_question=user_final_answer



        os.system('clear')
        welcoming_picture_to_game()


        for item in key_words_for_lesson0:
            if item in user_question.upper():
                print(second_game_message())
                print(more_explanation_lesson['LESSON0'])
                print('')
                sense_user_input()
                os.system('clear')

        for item in key_words_for_lesson1:
            if item in user_question.upper():
                print(second_game_message())
                print(more_explanation_lesson['LESSON1'])
                print('')
                sense_user_input()
                os.system('clear')

        for item in key_words_for_lesson2:
            if item in user_question.upper():
                print(second_game_message())
                print(more_explanation_lesson['LESSON2'])
                print('')
                sense_user_input()
                os.system('clear')

        for item in key_words_for_lesson3:
            if item in user_question.upper():
                print(second_game_message())
                print(more_explanation_lesson['LESSON3'])
                print('')
                sense_user_input()
                os.system('clear')

        for item in key_words_for_lesson4:
            if item in user_question.upper():
                print(second_game_message())
                print(more_explanation_lesson['LESSON4'])
                print('')
                sense_user_input()
                os.system('clear')
                    
    

    elif user_confirmation.upper() == 'NO':
        pass
    else:
        print('')
 

def lessons_and_questions_mode1():
    """
    This function contain the whole lessons for mode1 for this game and all of the questions and the answers
    
    arguments=>None
    Return=>list
    """
    lessons_questions_answers=[

    {'lesson0':"""Lesson 1 - Programming :
     Programming is the process of creating a set of instructions that tell a computer how to perform a task. Programming can be done using a variety of computer programming languages, such as JavaScript, Python, and C++""",

    'question0':"""Python is a:
    A- Development environment

    B- Set of editing Tools

    C- Programming Language""",
    'answer0':'C'},


    {'lesson1':"""Lesson 2 - print :
     Let\'s start off by creating a short program that displays (Hi!).In Python, we use the print statement to output text. """,
    'question1':"""Select the correct option to output "Hi".
    A- count('Hi')

    B- cprint('Hi')

    C- print('hi')
    
    D- print('Hi')""",
    'answer1':'D'} ,
    
    {'lesson2':"""Lesson 3 - Escape Characters:
    Some characters can\'t be directly included in a string which is the text between two single or double quotation marks. For instance, double quotes can\'t be directly included in a double quote string; this would cause it to end prematurely.Characters like these must be escaped by placing a backslash before them.Double quotes only need to be escaped in double quote strings, and the same is true for single quote strings. """,

    'question2':"""Which of the following command will output a string containing single quote.
    A- print('Just say "Good morning"')

    B- print('I'm learning!')

    C- print('I\\'m learning!')
    
    D- print('Welcome to programming world!')""",
    'answer2':'C'},

    {'lesson3':"""Lesson 4 - variable :
    A variable allows you to store a value by assigning it to a name, which can be used to refer to the value later in the program.To assign a variable, use one equals sign : Example(user = "James"  )
    Certain restrictions apply in regard to the characters that may be used in Python variable names. The only characters that are allowed are letters, numbers, and underscores. Also, they can\'t start with numbers.Not following these rules results in errors. """,

    'question3':"""Which of these is a valid variable name in Python?

    A- a-variable-name

    B- A_VARIABLE_NAME

    C- a variable name
    
    D- a.variable.name""",
    'answer3':'B'},
    {'lesson4':"""Lesson 5 - input : 

    To get input from the user in Python, you can use the intuitively named input function.
    For example, a game can ask for the user's name and age as input and use them in the game.

The input function prompts the user for input, and returns what they enter as a string (with the contents automatically escaped).The input statement needs to be followed by parentheses.""",

    'question4':"""What is the type of 'X' reagrding the following command:
    X=input('How old are you?')


    A- string

    B- boolean 

    C- integer
    
    D- Float""",
    'answer4':'A'}]
    return(lessons_questions_answers)



def start_lessons_and_questions(lessons_and_questions_mode1):
    
    lessons_questions_info=lessons_and_questions_mode1()

    total_marks=0
    questions_time_indicator=0


    for num in range(len(lessons_questions_info)):
        os.system('clear')
        # print instructor picture
        print(Fore.RESET +welcoming_picture_to_game())
        # print lessons
        print(lessons_questions_info[num][f'lesson{num}'])
        print('')
        sense_user_input()
        #starts calculating time from the following line
        os.system('clear')
        start = time.time()
        print(second_game_message())
        print(lessons_questions_info[num][f'question{num}'])
        user_answer=input('> Answer: ')
        # check for the time that the user took to answer
        
        while (time.time() - start) > 5:
            os.system('clear')
            questions_time_indicator+=1
            print("""Are you sure ?
            A -Yes
            B -No
            """)
            user_confirmation=input('> Answer:')
            while user_confirmation.upper() != 'YES' and user_confirmation.upper() != 'NO':
                print('Its a Yes or No question , Just answer with one of Them !')
                user_confirmation=input('> Answer:')
            if user_confirmation.upper() == 'YES':
                break
            else:
                start = time.time()
                print(lessons_questions_info[num][f'question{num}'])
                user_answer=input('> Answer: ')

        if  questions_time_indicator % 2 == 0 and questions_time_indicator > 0:
                user_ask_instructor(questions_time_indicator)
                questions_time_indicator=0




        if user_answer.upper()==lessons_questions_info[num][f'answer{num}']:
            total_marks+=20
        else:
            pass
    print( cprint(figlet_format(f'Your Total marks is : {total_marks}  Out of 100', font='doom'),
    'white', 'on_blue', attrs=['bold']) ) 
    print('')
    user_repeat_or_close_the_game=input('If you want to play again press Y if you want to quit press Q  >')
    while user_repeat_or_close_the_game.upper() != 'Y' and user_repeat_or_close_the_game.upper() != 'Q':
        print('You can answer only by Y or Q !!')
        user_repeat_or_close_the_game=input('>')
    if user_repeat_or_close_the_game.upper() == 'Y':
        main()
    elif user_repeat_or_close_the_game.upper() == 'Q':
        from main import start_application
        os.system('clear')
        os.system('exit')
    existing_score = retrive_value("pylearn_score")
    if existing_score and existing_score > total_marks:
        pass
    else:
        save_data("pylearn_score",total_marks)
    return cprint(figlet_format(f'Your Total marks is : {total_marks}  Out of 100', font='doom'),
    'white', 'on_blue', attrs=['bold'])



def before_user_start_game():
    print('To start this game just Type in \'Go\' !')
    user_select=input('> ')
    while(user_select.upper() != 'GO'):
        print('please type in \'Go\' to start !')
        user_select=input('> ')
    os.system('clear')
    return ''
    






def main():
    clear_console()
    print(first_game_message())
    time.sleep(2)
    print(Fore.RESET + welcoming_picture_to_game()  )
    print(welcoming_text_to_game())
    print(before_user_start_game())
    return(start_lessons_and_questions(lessons_and_questions_mode1))
