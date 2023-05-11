import pygame
import os

import constants
from strings_on_screen import StringImage   
from read_word_file import read_words_from_file
from game import Game
from word import Word
from translator import Translator
from settings import Settings

'''
The code is defining a class GameWords that inherits from the Game class. The class has several methods including __init__, 
init_extended, play_new_word, next_word, init_new_word, next_char, handle_correct_key_pressed, check_if_correct, and handle_key_pressed.

In the __init__ method, the class initializes variables such as mode_name, settings, lang_code, path, and words. It also sets the 
caption for the pygame display.

The init_extended method calls draw_mode_welcome to display instructions to the user. The play_new_word method plays 
audio to prompt the user to write a word. If instructions are set to True, it prompts the user to take a letter and 
speaks the current character of the word.

The next_word method removes the first word from the list of words and returns a Word instance for the word removed. 
If there are no more words left, it queues audio to congratulate the user on their progress and sets progress to constants.PROGRESS_WIN.

The init_new_word method queues audio to congratulate the user on writing the previous word if instructions are set to True. 
It then creates a StringImage object to display the remaining characters of the new word and sets self.word to the next word.

The next_char method attempts to move to the next character in the word by calling the next_char method of the Word object. 
If this raises an exception, it calls init_new_word and returns False, otherwise it returns True.

The handle_correct_key_pressed method queues audio to speak the key pressed, moves on to the next character by calling next_char, 
and updates the StringImage object with the remaining characters of the word.

The check_if_correct method checks if the key pressed is correct by checking if it matches the upper case of the current 
character in the word or if it matches a character in the extra_chars dictionary.

Lastly, the handle_key_pressed method handles a key press event. It checks if the audio queue is empty and the 
current word is completely viewed to initiate audio. If the key pressed is correct, it calls handle_correct_key_pressed. 
Otherwise, it queues audio to prompt the user to try again.
'''

'''
Potential issues:

The tts object is not initialized in the __init__ method, which will 
cause an AttributeError when the init method is called.
The menu_texts attribute is not defined, which will cause a NameError 
when trying to access self.menu_texts[self.lang_code]["Words"] in the __init__ method.
There is a commented out line that uses the tr method, but it is 
misspelled as self.tr instead of self.trans.tr.
The check_if_correct method assumes that extra_chars is defined and 
contains a mapping of characters to their correct counterparts, but it is not 
defined in the code provided. This will cause a NameError when the method is called.
There is an unused variable trans in the __init__ method.
To fix these issues:

Add self.tts = TTS(self.lang, False) in the __init__ method to initialize the tts object.
Define the menu_texts attribute or remove the reference to it in the __init__ method.
Change self.tr to self.trans.tr in the play_new_word method.
Define the extra_chars attribute or remove the reference to it in the check_if_correct method.
Remove the trans variable from the __init__ method.

'''

class GameWords(Game):
    def __init__(self):
        super().__init__()
        self.mode_name = self.trans.tr('Words', self.lang)

        settings = Settings.r_setup() 
        trans = Translator()
        lang_code = trans.get_code(settings["language"])
        
        path = os.path.join("words", f"words_{lang_code}.txt")
        self.words = read_words_from_file(path)
        
        if self.letter_case == "UPPER":
            self.words = [c.upper() for c in self.words]
            
        elif self.letter_case == "lower":
            self.words = [c.lower() for c in self.words]

        self.word = self.next_word()
        
        # Caption
        pygame.display.set_caption(f"{self.caption} - {self.mode_name}")
        
        
    def init_extended(self):
        
        self.draw_mode_welcome()
        self.tts.queue_text(self.mode_name, False)
        self.play_new_word()
        
    
    def play_new_word(self):
        self.tts.queue_text(self.trans.tr('Write word', self.lang))
        self.tts.queue_text(self.word.name())
        
        if self.instructions: 
            self.tts.queue_text(self.trans.tr('Take letter', self.lang))
            self.tts.queue_text(self.word.current_char())
        
    
    def next_word(self):
        try:
            self.draw()
            
            return Word(self.words.pop(0).replace(" ", ""))
            
        except:
            self.tts.queue_text(self.trans.tr('Passed', self.lang))
            self.tts.queue_text(f"{self.user_name}!")
            self.tts.queue_text(self.trans.tr('Very good', self.lang))
            
            self.progress = constants.PROGRESS_WIN
            
            self.word = None
            
    
    def init_new_word(self):
        ###print("Next word")
        self.tts.queue_text(self.trans.tr('Good', self.lang))
        if self.instructions:
            
            self.tts.queue_text(f"{self.user_name}!")
            self.tts.queue_text(f"{self.trans.tr('Wrote word', self.lang)} {self.word.name()}")
        
        self.string_image = StringImage(self.font_path, self.word.name(), self.screen, 1800, 0, 0, self.background_color, self.text_color)
        
        self.word = self.next_word()

        if self.word:
            self.play_new_word()
                # TODO: Make the last completed word go away/ empty screen. 

                
        
    def next_char(self):
        try:
            self.word.next_char()
            return True
            
        except:
            self.init_new_word()
            return False
    
    
    def handle_correct_key_pressed(self, key_pressed):  
        self.tts.queue_text(f"{key_pressed}", True)
        
        if self.next_char():
    
            if self.instructions:
                self.tts.queue_text(self.trans.tr('Take', self.lang))
                self.tts.queue_text(self.word.current_char())
                
            self.string_image = StringImage(self.font_path, self.word.sub_view(), self.screen, 1800, 0, 0, self.background_color, self.text_color)
            
        else:
            pass
        
        
    def check_if_correct(self, key_pressed):
        if key_pressed.upper() == self.word.current_char().upper():
            return True
        
        current = self.word.current_char().lower()
        
        ###print(current, key_pressed)

        if current in self.extra_chars and self.extra_chars[current] == key_pressed.lower():
            return True
        
                
    def handle_key_pressed(self, key_pressed):
        
        ###print("self.word.unviewed_chars()", self.word.unviewed_chars())
        
        start = self.tts._audio_queue and self.word._viewable_chars == 0
        
        if self.word and not start:
            if self.check_if_correct(key_pressed):
                self.handle_correct_key_pressed(key_pressed)
                self.draw()
                
                return
                
            self.tts.queue_text(f"{self.trans.tr('Try', self.lang)} {self.word.current_char()}", True)
    