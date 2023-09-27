from pyarcade_games.hangman import *
import builtins
import difflib
import pytest
import sys

def test_check_if_char_in_word():
    # Arrange
    expected = False
    # Actual
    actual = check_if_char_in_word("r","Mountain")
    # Expected
    assert actual == expected

def test_check_if_char_in_word_two():
    # Arrange
    expected = True
    # Actual
    actual = check_if_char_in_word("o","Global")
    # Expected
    assert actual == expected

def test_check_if_char_in_word_capital_letter():
    # Arrange
    expected = True
    # Actual
    actual = check_if_char_in_word("M","Mountain")
    # Expected
    assert actual == expected

def test_underscorify_word():
    # Arrange
    expected = "_____"
    # Actual
    actual = underscorify_word("store")
    # Expected
    assert actual == expected

def test_underscorify_word_with_num():
    # Arrange
    expected = "_____"
    # Actual
    actual = underscorify_word("store")
    # Expected
    assert actual == expected

def test_underscorify_word_with_num():
    # Arrange
    expected = None
    # Actual
    actual = underscorify_word("co5ol")
    # Expected
    print(actual)
    assert actual == expected

@pytest.mark.skip("todo")
def test_start_hangman_game_method():
    diffs = diff(start_hangman_game(4,"abcd"), path="assets/scenario/senario3.txt")
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
        start_hangman_game(6,"abcd",1)
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
