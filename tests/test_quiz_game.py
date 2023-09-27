"""
Quiz Game Tests
"""
import textwrap
from assets.helpers import create_example_fixture
from assets.helpers import keys
from pyarcade_games.quiz_game import *
import builtins
import difflib
import pytest
import sys

example_app = create_example_fixture('assets/answers_mock.py')

def test_display():
    msg="."
    actual=display(msg,"small")
    expected='   \n   \n _ \n(_)\n   \n'
    assert actual==expected

def test_get_score_happy_path():
    user_answers ={'howPass': 'Through droplets that come from your mouth and nose when you cough or breathe out', 'isPositve': 'No – not everyone with COVID-19 has symptoms', 'symptoms': 'All of the above', 'HIV': 'No – people who adhere to antiretroviral treatment (ART) and have a high CD4 count aren’t more at risk', 'peopleInDanger': 'Older people – especially those aged 70 and above', 'isCured': 'No – but most people get better by themselves', 'isProtect': 'Yes – normal soap and water or hand sanitizer is enough', 'protectHIV': 'All of the above', 'maskWorn': 'All of the above', 'distance': 'You stop going to crowded places and visiting other people’s houses'}
    user_answers = [j for j in user_answers.values()]
    correct_answers = [
        'Through droplets that come from your mouth and nose when you cough or breathe out',
        'No – not everyone with COVID-19 has symptoms',
        'All of the above',
        'No – people who adhere to antiretroviral treatment (ART) and have a high CD4 count aren’t more at risk',
        'Older people – especially those aged 70 and above',
        'No – but most people get better by themselves',
        'Yes – normal soap and water or hand sanitizer is enough',
        'All of the above',
        'All of the above',
        'You stop going to crowded places and visiting other people’s houses',]
    actual=get_score(correct_answers,user_answers)
    expected=10
    assert actual==expected

def test_get_score_normal_path():
    user_answers={'howPass': 'In sexual fluids, including semen, vaginal fluids or anal mucous', 'isPositve': 'No – not everyone with COVID-19 has symptoms', 'symptoms': 'All of the above', 'HIV': 'No – people who adhere to antiretroviral treatment (ART) and have a high CD4 count aren’t more at risk', 'peopleInDanger': 'Older people – especially those aged 70 and above', 'isCured': 'Yes – Hot drinks can cure COVID-19', 'isProtect': 'No – Washing your hands doesn’t stop COVID-19', 'protectHIV': 'Exercise regularly, eat well and look after their mental health', 'maskWorn': 'In small shops', 'distance': 'You stop talking to the people you live with'}
    user_answers = [j for j in user_answers.values()]
    correct_answers = [
        'Through droplets that come from your mouth and nose when you cough or breathe out',
        'No – not everyone with COVID-19 has symptoms',
        'All of the above',
        'No – people who adhere to antiretroviral treatment (ART) and have a high CD4 count aren’t more at risk',
        'Older people – especially those aged 70 and above',
        'No – but most people get better by themselves',
        'Yes – normal soap and water or hand sanitizer is enough',
        'All of the above',
        'All of the above',
        'You stop going to crowded places and visiting other people’s houses',]
    actual=get_score(correct_answers,user_answers)
    expected=4
    assert actual==expected
    
def test_get_score_sad_path():
    user_answers ={}
    user_answers = [j for j in user_answers.values()]
    correct_answers = [
        'Through droplets that come from your mouth and nose when you cough or breathe out',
        'No – not everyone with COVID-19 has symptoms',
        'All of the above',
        'No – people who adhere to antiretroviral treatment (ART) and have a high CD4 count aren’t more at risk',
        'Older people – especially those aged 70 and above',
        'No – but most people get better by themselves',
        'Yes – normal soap and water or hand sanitizer is enough',
        'All of the above',
        'All of the above',
        'You stop going to crowded places and visiting other people’s houses',]
    actual=get_score(correct_answers,user_answers)
    expected=0
    assert actual==expected

def test_get_answers(example_app):
    example_app.expect(textwrap.dedent("""\
        ? 1. How is COVID-19 passed on?  (Use arrow keys)
         ❯ In sexual fluids, including semen, vaginal fluids or anal mucous
           By drinking unclean water
           Through droplets that come from your mouth and nose when you cough or breathe
           All of the above"""))
    example_app.write(keys.ENTER)


@pytest.mark.skip("todo")
def test_main_method():
    diffs = diff(main(), path="assets/scenario/senario2.txt")
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
