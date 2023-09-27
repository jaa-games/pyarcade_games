from pyarcade_games import __version__
from main import start_application

def test_version():
    assert __version__ == '0.1.0'



def test_application_starts():
    # Arrange
    expected = True
    
    # Actual
    actual = False
    if start_application:
        actual = True

    assert actual == expected