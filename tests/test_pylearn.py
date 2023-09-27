from pyarcade_games.pylearn import *
import builtins
import difflib
import sys
import pytest

def test_first_game_message():
    #act
    actual=first_game_message()
    expected=Fore.CYAN + Style.BRIGHT + figlet_format("Welcome to Pylearn Game!")
    #assert
    assert actual == expected
def test_welcoming_picture_to_game():

    # arrange
    with open('pic.txt',mode='r') as file:
        content=file.read()
    expected=content
    # act
    ASCI_art_pic=welcoming_picture_to_game()
    actual=ASCI_art_pic
    #assert
    assert actual == expected
def test_welcoming_text_to_game():
    # arrange
    

    introduction="""                                                  Welcome to Pylearn !
                                I am Dario Thornhill and i will be your instructor in this Game !
                                i will help you to learn programming in a very Easy and nice way !
                                            lets get started"""
    expected=introduction
    # act
    Greeting=welcoming_text_to_game()
    actual=Greeting
    #assert
    assert actual == Greeting
def test_second_game_message():
    #act
    actual=second_game_message()
    expected=Fore.CYAN + Style.BRIGHT + figlet_format("Pylearn Game")
    #assert
    assert actual == expected
def test_lessons_and_questions_mode1():
    # act
    actual=len(lessons_and_questions_mode1())
    expected=5
    # assert
    assert actual==expected

@pytest.mark.skip("todo")
def test_main_method():
    diffs = diff(main(), path="assets/scenario/senario1.txt")
    assert not diffs, diffs


def diff(play, path="", sample=""):
    text = ""
    expected_lines = _parse_expected_lines(path, sample)
    responses = _extract_responses(expected_lines)
    def mock_print(*args):

        nonlocal text

        text += "".join(args) + "\n"

    def mock_input(*args):

        nonlocal text

        if not responses:
            sys.exit(1)

        response = responses.pop(0)

        text += "".join(args) + response + "\n"

        return response
    
    real_print = builtins.print
    real_input = builtins.input

    builtins.print = mock_print
    builtins.input = mock_input

    try:
        main()
    except SystemExit:
        real_print("No problem. System exits are allowed in this app.")

    builtins.print = real_print
    builtins.input = real_input

    return _find_differences(text, expected_lines)
def _parse_expected_lines(path, sample):
    if path:
        with open(path) as f:
            expected_lines = f.read().splitlines()
    else:
        expected_lines = sample.splitlines()

    return expected_lines
def _extract_responses(lines):
    responses = []
    for line in lines:
        if line.startswith(">"):
            response = line.replace("> ", "").strip()
            responses.append(response)
    print(responses)
    return responses
def _find_differences(text, expected_lines):

    actual_lines = text.splitlines()

    diffed = difflib.unified_diff(actual_lines, expected_lines, lineterm="")

    return "\n".join(diffed)
