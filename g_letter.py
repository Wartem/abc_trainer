import constants
from game import Game
from strings_on_screen import StringImage
from letter_handler import LetterHandler

'''
Potential issues:


In the __init__ method, self.string_image is initialized with 
the self.string_in_use variable, which is set to the result of 
self.letter_handler.set_letter_in_use(). However, this variable is 
only set once in the __init__ method, so the image will always display 
the same letter. Instead, the self.string_in_use variable should be updated whenever 
the user enters a correct letter.

In the handle_correct_key_pressed method, 
the line no_more_letters = len(self.letter_handler.letters_to_add) == 0 and 
len(self.letter_handler.available_letters) == 0 is commented out. It is unclear why this 
line is commented out, but it seems like it might be important to check if there are no more letters to display.

In the check_if_correct method, self.extra_chars[key_pressed] should be 
self.extra_chars[key_pressed.lower()], since key_pressed is already converted to uppercase.

In the handle_key_pressed method, the if condition that checks if the 
user entered the correct letter should call the handle_correct_key_pressed 
method regardless of whether there are more letters to display or not. 
Otherwise, if the user enters the correct letter on the last letter, 
the game will not progress to the win state.
'''

class GameLetterMix(Game):
    def __init__(self):
        super().__init__()
        self.mode_name = self.trans.tr('Letter mix', self.lang)
        
        self.letter_handler = None
        self.set_letter_handler()
        
        self.string_in_use = self.letter_handler.set_letter_in_use()
        self.string_image = StringImage(self.font_path, self.string_in_use, self.screen, 1800, 0, 0, self.background_color, self.text_color)
        
        
    def set_letter_handler(self):
        self.letter_handler = LetterHandler(self.user_name[:4], 4, 7, self.lang, self.repetitions, self.letter_case, self.excluded_chars)
        
        
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
        
        if (not more_letters or key_pressed == "") and self.progress != constants.PROGRESS_WIN:
            self.win()

            return 
            
        else:
            #if self.instructions:    
            self.tts.queue_text(f"{key_pressed}", True)
            
            self.string_in_use = self.letter_handler.set_letter_in_use()
            
            if self.string_in_use:
                if self.instructions:
                    self.tts.queue_text(self.trans.tr('Take', self.lang)) 
                    self.tts.queue_text(self.string_in_use)
                self.draw()
                    
                
                self.string_image = StringImage(self.font_path, self.string_in_use, self.screen, 1800, 0, 0, self.background_color, self.text_color)
            
            else:
                self.handle_correct_key_pressed("")
                #self.letter_handler.check_add_letter_counter()
                #self.win()
                

    def check_if_correct(self, key_pressed):
        if key_pressed.upper() == self.string_in_use.upper():
            return True

        if key_pressed.lower() in self.extra_chars and self.extra_chars[key_pressed.lower()] == key_pressed:
            return True
        
                
    def handle_key_pressed(self, key_pressed):
        if self.check_if_correct(key_pressed):
            self.handle_correct_key_pressed(key_pressed)
            return
            
        self.tts.queue_text(f"{self.trans.tr('Try', self.lang)} {self.string_in_use}", True)
        self.letter_handler.correct_counter = 0