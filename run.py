#!/usr/bin/env python3

# Import the tkinter fix to patch the ScreenChanged error (optional - only needed for GUI)
try:
    import tkinter_fix
except ModuleNotFoundError:
    pass  # tkinter not available; GUI will not work but CLI mode will

from modules import core

if __name__ == '__main__':
    core.run()
