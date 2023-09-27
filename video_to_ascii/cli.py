"""This module contains a CLI interface"""

from . import player

def top(file,strategy):

    try:
        player.play(file, strategy)
    except (KeyboardInterrupt):
        pass

if __name__ == '__main__':
    top()
