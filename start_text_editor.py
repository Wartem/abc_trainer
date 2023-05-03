import subprocess

def open_with_nano(file_path, editor='nano'):
    """
    Opens the specified text file in the specified text editor.
    
    Arguments:
    file_path -- the path to the text file to be opened
    editor -- the text editor to use (defaults to 'nano')
    """
    try:
        subprocess.run([editor, file_path])
    except FileNotFoundError:
        print(f"{editor} is not installed on this system.")
        
        
        
import webbrowser

def open_with_webbrowser(file_path):
    """
    Opens the specified text file in the default text editor.
    
    Arguments:
    file_path -- the path to the text file to be opened
    """
    try:
        webbrowser.open(file_path)
    except:
        print("Unable to open file in default text editor.")
        #ToDo: Add a dialog box giving user instructions on how to open the .txt file