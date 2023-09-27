"""
Hangman Game Module

"""
from colorama import Fore, Style
import random
import pyfiglet
import os
import string
import readchar
from pyarcade_games.save_data import save_data, retrive_value
default_tries = 6
hangman_states = [
f'''{Fore.GREEN}{Style.BRIGHT}
  +---+
  |   |
      |
      |
      |
      |
========={Fore.RESET}
''', 
f'''{Fore.GREEN}
  +---+
  |   |
  O   |
      |
      |
      |
========={Fore.RESET}
''', 
f'''{Fore.YELLOW}{Style.BRIGHT}
  +---+
  |   |
  O   |
  |   |
      |
      |
========={Fore.RESET}
''', 
f'''{Fore.YELLOW}
  +---+
  |   |
  O   |
 /|   |
      |
      |
========={Fore.RESET}
''', 
f'''{Fore.RED}
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========={Fore.RESET}
''', 
f'''{Fore.RED}
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========={Fore.RESET}
''', 
f'''{Fore.LIGHTRED_EX}
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========={Fore.RESET}
'''
]
words_bank = []
with open("assets/hangman_words.txt") as file:
    words_bank = file.readlines()

def start_hangman_game(tries=default_tries, word=words_bank[random.randint(0,len(words_bank)-1)],x=random.randint(1,2)):
    """Start Hangman Game
    Args:
        number of tries ([int]): [number of tries user has to guess the correct word]
        word ([string]): [word to search in]
    Returns: 
        None
    """
    clear_console()
    number_of_tries = tries
    word=word
    hangman_state = 0
    start_message = Fore.RED + Style.BRIGHT + pyfiglet.figlet_format("Hangman")
    print(start_message)
    print(Fore.GREEN + "Game Rules: ")

    print(f"1: You have {tries} tries to guess the correct letters of a randomized word")
    print(f"2: If you input a correct letter, the Hangman will stay in his current state without losing any of the tries you have.")
    print(f"3: If you input a wrong letter, then the hangman state will update and you will lose 1 try ")
    
    random_num = x
    if random_num == 1:
      print(f"{Fore.RESET}Hint: the word ends with {word.strip()[-1]}")
    else:
      print(f"{Fore.RESET}Hint: the word starts with {word[0]}")
    modified_word = list(underscorify_word(word))

    while number_of_tries > 0:
        if "".join(modified_word).strip() != word.strip():  
          print(f"{Fore.RESET}Word is made of {len(word.strip())} letters")
          print(" ","".join(modified_word))

          user_input = input("Take a guess: ").lower()
          while (len(user_input) != 1) or (user_input not in string.ascii_lowercase):
            print(f"{Fore.RED}Please enter a single letter.{Fore.RESET}")
            user_input = input("Take a guess: ").lower()
          
          if check_if_char_in_word(user_input,word):
            for i, letter in enumerate(word):
              if letter != "_" and user_input == letter:
                modified_word[i] = letter
          else:
            number_of_tries -= 1
            hangman_state += 1
            if number_of_tries==0 :
              clear_console()
              fail_message = Fore.RED + Style.BRIGHT + pyfiglet.figlet_format("FAILED!")
              print(fail_message)
              print(f"{Fore.RESET}You ran out of tries {Fore.RED}{Style.BRIGHT}:({Fore.RESET}")
              print(f"Correct word was {Fore.RED}{word.strip()}{Fore.RESET}")
              print("------------------------------------------------")
              print("------------------------------------------------")
              replay_or_quit()
              break
          clear_console()
          print(Fore.RESET + hangman_states[hangman_state])
        elif "".join(modified_word).strip() == word.strip():
          clear_console()
          win_message = Fore.GREEN + Style.BRIGHT + pyfiglet.figlet_format("Congratz")
          print(win_message)
          print(f"{Fore.RESET}You have sucessfully guessed the word!")
          score = (tries-number_of_tries)+1
          
          existing_score = retrive_value("hangman_score")
          if existing_score and existing_score < score:
            pass
          else:
            save_data("hangman_score",score)
          
          print(f"Score: Beaten the game with only {(tries-number_of_tries)+1} try(s)")
          print("------------------------------------------------")
          print("------------------------------------------------")
          break

def replay_or_quit():
  """Prompts the user with input asking if they should play again or not.
  Args:
    None
  Returns:
    None
  """
  print("Would you like to exit (e) or back to main menu (b) or play again (y) ?")
  char=readchar.readchar()
  
  if char == "y":
    start_hangman_game(6,words_bank[random.randint(0,len(words_bank)-1)])
  elif char == "b":
    from main import start_application
    start_application()
  elif char=="e":
    os.system('exit')
    
    


def check_if_char_in_word(char: str,word: str):
  """Check if Character in Word

  Args:
      char ([char]): [character to be searched for]
      word ([string]): [word to search in]
  Returns:
      True or False
  """
  if char.lower() in word.lower():
      return True
  return False


def underscorify_word(word: str):
  """Turn word letters into underscores
    e.g (word) => (____)

  Args:
      word ([str]): [word to be underscorified]

  Returns:
      [str]: [underscorified word]
  """
  modified_word = ""
  _word = word.lower().strip()
  for i in _word:
    if i in string.ascii_lowercase:
      modified_word+= "_"
    else:
      return None
  return modified_word.strip()
  

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
