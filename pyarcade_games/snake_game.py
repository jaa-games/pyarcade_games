"""
Snake Game Module
"""

import curses
from random import randint
import random
from colorama import Fore,  Style
import pyfiglet
import os
from pyarcade_games.save_data import save_data, retrive_value
import readchar




def main():

    """
    Function that start Snake game and displays the screen with playfiled,snake,and food.

    Args:
        None

    OutPut : 
        screen with snake , food and player score    
    """

    curses.initscr()
    
    #creat a new window using curses library contain 25 lines and 80 col , and the window coordinate =(2,20)
    win = curses.newwin(25 , 80 , 2, 20)

    #using the keypad arrow key to control the snake
    win.keypad(1)

    curses.noecho()
    curses.curs_set(0)

    #To draw the boarder
    win.border(0)
    win.nodelay(1)

    
    # Snake and Food :set the data structures to keep track of the snake and the food.
    # hint : the first coordinate is y so the snake is in the same row
    snake = [(4, 10) , (4 , 9) , (4,8)]
    food=(10,20)


    # game logic :

    score= 0
    Highest_Score = 0


    ESC = 27
    key = curses.KEY_RIGHT


    # Tuple contain different type of food
    food_ch = ('🍕' , '🍔' , '🍩' , '🍉' ,'🍎' )
    foodch =random.choice(food_ch)

    while key != ESC:

        """
         loop to add characters to the board and
         to control the snake direction
        
        """
        win.addstr(0 , 70 ,   " Score " + str(score) +' ' ) 
        # win.addstr(0 , 80 ," Highest_Score " + str(Highest_Score) +' ' ) 
        win.addstr(0 , 1 ,'🐍' ) 

        #to increase the speed when the snake gets bigger based on the length of the snake 
        win.timeout(150 - (len(snake)) //5 + len(snake)//10 % 120)

       
        #get the next key and set the event if the user didn't press any arrow to the prev key
        prev_key = key

        event = win.getch()
        key= event if event != -1 else prev_key



        # calculate the next coordinate 

        y = snake[0][0]
        x = snake[0][1]
        y = y_coordinat(y , key)
        x = x_coordinat(x , key)

      

        
            
        if key not in [curses.KEY_RIGHT , curses.KEY_LEFT , curses.KEY_UP , curses.KEY_DOWN , ESC]:
            key = prev_key


        snake.insert(0 , (y ,x))

        # check if the snake hit the border

        if y == 0 : break
        if y== 24 : break
        if x == 0 :break
        if x== 79 :break


        # check if the snake runs over itself :
        if snake[0] in snake[1:] : break


        #  check if the snake eat the food to increase the score and to delete the food 
        # generate another food with different coordinate:

        if snake[0] == food :
            score+=1
            if Highest_Score <= score :
             Highest_Score=score
            
            food=()
            foodch =random.choice(food_ch)

            while food == ():
                # get a random coordinate for the food
                food = (randint(1,23) , randint(1,78))

                # check that the random coordinate not on the snake coordinate
                if food in snake :
                    food =()

            win.addch(food[0] , food[1] , foodch)

        else :
            # move the snake to delete the current coordinate 
            last = snake.pop()
            win.addch(last[0] , last[1] , ' ')

        win.addch(snake[0][0] , snake[0][1] , '☀' )               

        

        for c in snake :
            win.addch(c[0] , c[1] , '☀')

        win.addch(food[0] , food[1] ,foodch)

    # close the window if the snake is died
    curses.endwin()



    # print the Lose and score messages 
    
    Lose_meassage = Fore.RED+ Style.BRIGHT + pyfiglet.figlet_format("You Lose ")

    score_meassage = Fore.BLUE+ Style.BRIGHT + pyfiglet.figlet_format(f"Score : {score} ")
    existing_score = retrive_value("snake_score")
    if existing_score and existing_score > score:
        pass
    else:
        save_data("snake_score",score)
    print(Lose_meassage)
    print( score_meassage)

    clear_console()
    #ask the user if he would to play again
    
    print('You lose the game Try again ? y for yes and n for no..')
    char=readchar.readchar()
    if char == 'y':
        # from hangman import clear_console
        clear_console()
        main()
    else :
        from main import start_application
        clear_console()
        print("Back to main menu..")
        start_application()    
        


def y_coordinat (y , key):
    """
    function to calculate the next y coordinate.

    Args : 
        y coordinate (int) and key (pressed arrow key )
    Output :
        return the new y coordinate    
    """
    if key == curses.KEY_DOWN:
            y+=1

    elif key == curses.KEY_UP:
            y-=1    

    return y



def x_coordinat ( x , key):

    """
    function to calculate the next x coordinate.
    Args:
        x coordinate and key (pressed arrow key )
    Output :
        return the new x coordinate 

    """

    if key == curses.KEY_LEFT:
         x -=1

    elif key == curses.KEY_RIGHT:
         x +=1    

    return x

     
def clear_console():
    """Clear Console:
      Clear the command line from all the inputs and outputs printed in it
    Args:
        None
    Output:
        Remove all lines from the console
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


# print(Style.BRIGHT + f"Highest_Score : {Highest_Score} ")

if __name__ == "__main__":
    main()