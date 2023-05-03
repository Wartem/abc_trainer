from game import Game

import constants
from strings_on_screen import StringImage
from letter_handler import LetterHandler


class GameAllOnce(Game):
    def __init__(self):
        super().__init__()
        self.mode_name = self.trans.tr('In order', self.lang)
        
        if self.letter_case == "Both":
            self.letter_case = "Both In Order"
        
        self.letter_handler = None
        self.set_letter_handler()
        
        self.string_in_use = self.letter_handler.set_letter_in_use()
        self.string_image = StringImage(self.font_path, self.string_in_use, self.screen, 1800, 0, 0, self.background_color, self.text_color)
        
        
    def set_letter_handler(self):
        self.letter_handler = LetterHandler("", 1, 9999, self.lang, 1, self.letter_case, self.excluded_chars)
        
        
    def init_extended(self):
        self.draw_mode_welcome()
        self.tts.queue_text(self.mode_name, False)
        
        if self.instructions:    
            self.tts.queue_text(self.trans.tr('Press', self.lang)) 
            self.tts.queue_text(self.string_in_use)
    
    
    def win(self):
            self.tts.queue_text(self.trans.tr('Passed', self.lang))
            self.tts.queue_text(f"{self.user_name}!")
            self.tts.queue_text(self.trans.tr('Very good', self.lang))
            self.progress = constants.PROGRESS_WIN
    
    
    def handle_correct_key_pressed(self, key_pressed):
        more_letters = True
            
        if not self.letter_handler.available_letters and not self.letter_handler.letters_to_add:
            more_letters = False
            
        else:
            self.letter_handler.check_add_letter_counter()
        
        if not more_letters and self.progress != constants.PROGRESS_WIN:
            self.win()
            
        else:
            self.tts.queue_text(f"{key_pressed}", True)
            self.string_in_use = self.letter_handler.set_letter_in_use()
            
            if self.string_in_use:
                if self.instructions:
                    self.tts.queue_text(self.trans.tr('Take', self.lang))
                    self.tts.queue_text(self.string_in_use)
                self.draw() 
                
                self.string_image = StringImage(self.font_path, self.string_in_use, self.screen, 1800, 0, 0, self.background_color, self.text_color)
            
            else:   
                self.win()    
              
                
    def handle_key_pressed(self, key_pressed):
        if key_pressed.upper() == self.string_in_use.upper():
            self.handle_correct_key_pressed(key_pressed)
            return
            
        self.tts.queue_text(f"{self.trans.tr('Try', self.lang)} {self.string_in_use}", True)
        self.letter_handler.correct_counter = 0