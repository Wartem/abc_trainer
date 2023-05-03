import pygame
import os
import sys

import constants
from strings_on_screen import StringImage   
from read_word_file import read_words_from_file
from game import Game
from word import Word
from translator import Translator
from settings import Settings

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
        self.caption = Settings.r_instructions()[self.lang]["Caption"]
        self.mt_words_txt = self.menu_texts[self.lang_code]["Words"]
        
        pygame.display.set_caption(f"{self.mt_words_txt} - {self.caption}")
        
        
    def init_extended(self):
        
        self.draw_mode_welcome()
        self.tts.queue_text(self.mode_name, False)
        self.play_new_word()
        
    
    def play_new_word(self):
        #self.tts.queue_text(self.tr('Press')) # Tryck på
        #self.tts.queue_text("Skriv ordet")
        self.tts.queue_text(self.trans.tr('Write word', self.lang))
        self.tts.queue_text(self.word.name())
        
        if self.instructions: 
            #self.tts.queue_text("Ta bokstaven")
            self.tts.queue_text(self.trans.tr('Take letter', self.lang))
            self.tts.queue_text(self.word.current_char())
        
    
    def next_word(self):
        try:
            self.draw()
            #self.string_image = StringImage("", self.screen)

            return Word(self.words.pop(0).replace(" ", ""))
            
        except:
            self.tts.queue_text(self.trans.tr('Passed', self.lang))
            self.tts.queue_text(f"{self.user_name}!")
            self.tts.queue_text(self.trans.tr('Very good', self.lang))
            
            self.progress = constants.PROGRESS_WIN
            
            #raise CustomException()
            
            self.word = None
            
    
    def init_new_word(self):
        print("Next word")
        #self.draw()
        #self.tts.queue_text("BRA!")
        self.tts.queue_text(self.trans.tr('Good', self.lang))
        if self.instructions:
            
            self.tts.queue_text(f"{self.user_name}!")
            self.tts.queue_text(f"{self.trans.tr('Wrote word', self.lang)} {self.word.name()}")
        
        self.string_image = StringImage(self.font_path, self.word.name(), self.screen, 1800, 0, 0, self.background_color, self.text_color)
        
        self.word = self.next_word()

        if self.word:
            #if self.instructions:    
            self.play_new_word()
                #self.draw()
                # TODO: Make the last completed word go away/ empty screen. 
                #self.string_image = StringImage("", self.screen, self.font.title(), 1800, 0, 0, self.background_color, self.text_color)
                
        
    def next_char(self):
        try:
            self.word.next_char()
            return True
            
        except:
            self.init_new_word()
            return False
    
    
    def handle_correct_key_pressed(self, key_pressed):
        #if self.instructions:    
        self.tts.queue_text(f"{key_pressed}", True)
        
        if self.next_char():
    
            if self.instructions:
                self.tts.queue_text(self.trans.tr('Take', self.lang))
                self.tts.queue_text(self.word.current_char())
                #self.draw() ???
                
            self.string_image = StringImage(self.font_path, self.word.sub_view(), self.screen, 1800, 0, 0, self.background_color, self.text_color)
            
        else:
            #self.string_image = StringImage("", self.screen)
            #self.draw()
            pass
        
        
    def check_if_correct(self, key_pressed):
        if key_pressed.upper() == self.word.current_char().upper():
            return True
        
        current = self.word.current_char().lower()
        
        print(current, key_pressed)

        if current in self.extra_chars and self.extra_chars[current] == key_pressed.lower():
            return True
        
                
    def handle_key_pressed(self, key_pressed):
        if self.word:
            if self.check_if_correct(key_pressed):
                self.handle_correct_key_pressed(key_pressed)
                self.draw()
                
                return
                
            self.tts.queue_text(f"{self.trans.tr('Try', self.lang)} {self.word.current_char()}", True)
    