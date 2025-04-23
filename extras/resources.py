import os
import sys

def load_resource(filename):
    if 'js' in sys.modules:
        path = os.path.join('extras', filename)
    elif hasattr(sys, '_MEIPASS'):
        path = os.path.join(sys._MEIPASS, 'extras', filename)
    else:
        path = os.path.join(os.path.dirname(__file__), filename)
    return path