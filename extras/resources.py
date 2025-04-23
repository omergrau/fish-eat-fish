import os
import sys

def load_resource(filename):
    if 'js' in sys.modules:
        path = os.path.join('extras', filename)
    elif hasattr(sys, '_MEIPASS'):
        path = os.path.join(sys._MEIPASS, filename)
    else:
        path = os.path.join(os.path.dirname(__file__), filename)
    return path


def entry_load():
     ocean=load_resource("ocean.png")
     lose_video_game = load_resource("lose_video-game.wav")
     main_game_music = load_resource("game-music-loop.wav")
     return ocean,lose_video_game,main_game_music