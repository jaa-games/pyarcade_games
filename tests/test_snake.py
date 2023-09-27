from pyarcade_games.snake_game import y_coordinat , x_coordinat
import curses




def test_y_coordinte_down():
    # Arrange
    expected = 12
    # Actual
    actual = y_coordinat(11 ,curses.KEY_DOWN)
    # Expected
    assert actual == expected


def test_y_coordinte_up():
    # Arrange
    expected = 8
    # Actual
    actual = y_coordinat(9 ,curses.KEY_UP)
    # Expected
    assert actual == expected



def test_x_coordinte_right():
    # Arrange
    expected = 6
    # Actual
    actual = x_coordinat(5 ,curses.KEY_RIGHT)
    # Expected
    assert actual == expected    

def test_x_coordinte_left():
    # Arrange
    expected = 59
    # Actual
    actual = x_coordinat(60,curses.KEY_LEFT)
    # Expected
    assert actual == expected       