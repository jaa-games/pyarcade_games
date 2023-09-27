"""
Main Game Module
"""
from colorama import Fore, Style
from PyInquirer.prompt import prompt
import sys
import os
import pyfiglet

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def start_application():
    """
    Application Start Method
    """
    
    question = [
        {
            "type": "list",
            "name": "game",
            "message": "Choose A Game To Play.",
            "choices": [
                "Hang Man",
                "Quiz Game",
                "Snake",
                "Pylearn",
                "View Scores",
                "Quit"
            ],
        }
    ]
    
    
    # play Game Video
    from video_to_ascii.cli import top
    top('assets/dancing_man.mp4','filled-ascii')
    # play Game Video
    clear_console()
    
    print(Fore.CYAN + Style.BRIGHT + pyfiglet.figlet_format("PyArcade Games"))

    
    answer = prompt(question).get("game")
    if answer == "Hang Man":
        from pyarcade_games.hangman import start_hangman_game
        start_hangman_game()
    elif answer == "Quiz Game":
        from pyarcade_games.quiz_game import main
        main()
    elif answer == "Snake":
        from pyarcade_games.snake_game import main
        main()
    elif answer == "Pylearn":
        from pyarcade_games.pylearn import main
        main()
    elif answer == "View Scores":
        from assets.scores_menu import view_scores
        view_scores()
    elif answer == "Quit":
        quit_game()
        

def quit_game():
    print(f"{Fore.RED} Quiting Game....")
    sys.exit()



if __name__ == "__main__":
    start_application()