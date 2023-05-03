#import os
#import sys

#from pathlib import Path

# Add the project's root directory to sys.path
#root_dir = Path(__file__).resolve().parent
#sys.path.insert(0, str(root_dir))

#sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

#parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
#sys.path.insert(0, parent_dir)


from main_menu import start

if __name__ == "__main__":
    start()
    
    """ import sys
    import os


    if getattr(sys, 'frozen', False):
        bundle_dir = sys._MEIPASS
    else:
        bundle_dir = os.path.dirname(os.path.abspath(__file__))

    parent_dir = os.path.abspath(os.path.join(bundle_dir, '..'))
    sys.path.insert(0, parent_dir)

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    from AlphabetGame.Main.main_menu import start


    if __name__ == "__main__":
        start() """